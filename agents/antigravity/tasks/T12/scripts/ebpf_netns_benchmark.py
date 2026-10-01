#!/usr/bin/env python3
"""
ebpf_netns_benchmark.py — Microsegmentation Policy Enforcement & Convergence Benchmark
Mô phỏng và đo lường chi phí độ trễ theo lớp chính sách (L3 vs L4 vs L7)
và thời gian hội tụ khi workload thay đổi danh tính động cho đề tài RL-T2-EBPF-SEG.

Không phụ thuộc package ngoài (chỉ dùng Python standard library: time, random, statistics, json, csv).
"""

import sys
import time
import random
import statistics
import json

def generate_policy_rules(n_rules):
    """Sinh n_rules chính sách mô phỏng cho L3, L4, L7."""
    rules = []
    for i in range(n_rules):
        rules.append({
            "id": f"rule-{i:04d}",
            "src_cidr": f"10.244.{random.randint(1, 20)}.{random.randint(1, 254)}/32",
            "dst_cidr": f"10.244.{random.randint(21, 40)}.{random.randint(1, 254)}/32",
            "protocol": random.choice(["TCP", "UDP"]),
            "port": random.choice([80, 443, 8080, 9090, 5432, 6379]),
            "l7_action": "ALLOW",
            "l7_path_prefix": random.choice(["/api/v1/orders", "/api/v1/auth", "/metrics", "/healthz", "/static"]),
            "l7_method": random.choice(["GET", "POST", "PUT", "DELETE"])
        })
    return rules

def evaluate_l3_bpf_map(rules, packet):
    """Mô phỏng tra cứu eBPF LPM Trie / Hash Map (L3)."""
    t0 = time.perf_counter_ns()
    # eBPF map lookup is O(1) hash or O(W) LPM trie
    match = False
    for r in rules:
        if r["dst_cidr"] == packet["dst_ip"]:
            match = True
            break
    t1 = time.perf_counter_ns()
    return match, (t1 - t0) / 1000.0  # microseconds

def evaluate_l4_tc_filter(rules, packet):
    """Mô phỏng tra cứu eBPF TC filter (L3 + L4 5-tuple)."""
    t0 = time.perf_counter_ns()
    match = False
    for r in rules:
        if r["dst_cidr"] == packet["dst_ip"] and r["port"] == packet["dst_port"] and r["protocol"] == packet["protocol"]:
            match = True
            break
    t1 = time.perf_counter_ns()
    return match, (t1 - t0) / 1000.0  # microseconds

def evaluate_l7_proxy(rules, packet):
    """Mô phỏng tra cứu eBPF socket redirection + L7 Envoy proxy inspection."""
    t0 = time.perf_counter_ns()
    # L7 requires parsing HTTP request headers & matching URI/Method
    match = False
    for r in rules:
        if (r["dst_cidr"] == packet["dst_ip"] and 
            r["port"] == packet["dst_port"] and 
            r["l7_method"] == packet["http_method"] and 
            packet["http_path"].startswith(r["l7_path_prefix"])):
            match = True
            break
    t1 = time.perf_counter_ns()
    return match, (t1 - t0) / 1000.0  # microseconds

def benchmark_layers():
    results = {}
    rule_counts = [10, 100, 1000]
    iterations = 500

    print("=== [1] ĐO CHI PHÍ THEO LỚP CHÍNH SÁCH (L3 vs L4 vs L7) ===")
    print(f"Lặp lại {iterations} lần cho mỗi cấu hình quy tắc:")

    for n in rule_counts:
        rules = generate_policy_rules(n)
        test_packets = []
        for _ in range(iterations):
            test_packets.append({
                "src_ip": f"10.244.{random.randint(1, 20)}.{random.randint(1, 254)}/32",
                "dst_ip": random.choice(rules)["dst_cidr"] if random.random() > 0.3 else "10.244.99.99/32",
                "protocol": "TCP",
                "dst_port": random.choice([80, 443, 8080]),
                "http_method": random.choice(["GET", "POST", "PUT"]),
                "http_path": "/api/v1/orders/123"
            })

        l3_times = [evaluate_l3_bpf_map(rules, p)[1] for p in test_packets]
        l4_times = [evaluate_l4_tc_filter(rules, p)[1] for p in test_packets]
        l7_times = [evaluate_l7_proxy(rules, p)[1] for p in test_packets]

        def stats(arr):
            arr_sorted = sorted(arr)
            return {
                "median_us": statistics.median(arr),
                "p90_us": arr_sorted[int(len(arr_sorted) * 0.90)],
                "p99_us": arr_sorted[int(len(arr_sorted) * 0.99)],
                "mean_us": statistics.mean(arr),
                "stdev_us": statistics.stdev(arr) if len(arr) > 1 else 0.0
            }

        results[f"rules_{n}"] = {
            "L3": stats(l3_times),
            "L4": stats(l4_times),
            "L7": stats(l7_times)
        }

        print(f"\n--- Quy mô {n} quy tắc ---")
        print(f"L3 (eBPF Map lookup)     : p50={results[f'rules_{n}']['L3']['median_us']:.2f} µs | p90={results[f'rules_{n}']['L3']['p90_us']:.2f} µs | p99={results[f'rules_{n}']['L3']['p99_us']:.2f} µs")
        print(f"L4 (eBPF TC 5-tuple)     : p50={results[f'rules_{n}']['L4']['median_us']:.2f} µs | p90={results[f'rules_{n}']['L4']['p90_us']:.2f} µs | p99={results[f'rules_{n}']['L4']['p99_us']:.2f} µs")
        print(f"L7 (eBPF Proxy redirect) : p50={results[f'rules_{n}']['L7']['median_us']:.2f} µs | p90={results[f'rules_{n}']['L7']['p90_us']:.2f} µs | p99={results[f'rules_{n}']['L7']['p99_us']:.2f} µs")

    return results

def benchmark_convergence_window():
    """Mô phỏng vòng lặp động: Workload Identity Churn (Pod restart/IP change) -> eBPF Map Update -> Convergence."""
    print("\n=== [2] ĐO THỜI GIAN HỘI TỤ ĐỘNG (CONVERGENCE WINDOW - RQ1/RQ3) ===")
    node_counts = [3, 5, 10]
    iterations = 50
    churn_results = {}

    for nodes in node_counts:
        convergence_times = []
        for _ in range(iterations):
            t_event = time.perf_counter_ns()
            # Mô phỏng thời gian CNI Agent nhận thông báo K8s Watch Event và nạp bpf_map_update_elem trên từng nút
            # Mô hình thực tế: IO socket IPC + eBPF map syscall per node
            node_latencies = []
            for node_id in range(nodes):
                t_node_start = time.perf_counter_ns()
                # syscall bpf(BPF_MAP_UPDATE_ELEM) + RCU sync
                time.sleep(random.uniform(0.0005, 0.0018)) # 0.5ms - 1.8ms per node
                t_node_end = time.perf_counter_ns()
                node_latencies.append((t_node_end - t_event) / 1e6) # ms
            t_converged = max(node_latencies)
            convergence_times.append(t_converged)

        churn_results[f"nodes_{nodes}"] = {
            "median_ms": statistics.median(convergence_times),
            "p90_ms": sorted(convergence_times)[int(len(convergence_times) * 0.90)],
            "p99_ms": sorted(convergence_times)[int(len(convergence_times) * 0.99)],
            "min_ms": min(convergence_times),
            "max_ms": max(convergence_times)
        }
        print(f"Số nút N={nodes:2d}: Hội tụ toàn cụm p50={churn_results[f'nodes_{nodes}']['median_ms']:.2f} ms | p90={churn_results[f'nodes_{nodes}']['p90_ms']:.2f} ms | max={churn_results[f'nodes_{nodes}']['max_ms']:.2f} ms")

    return churn_results

if __name__ == "__main__":
    random.seed(20261001)
    res_layers = benchmark_layers()
    res_churn = benchmark_convergence_window()
    print("\nBenchmark completed successfully.")
