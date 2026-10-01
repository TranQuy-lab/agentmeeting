#!/usr/bin/env python3
"""
T15-1 — KIEM CHUAN PCAP: scapy (ghi) <-> tshark (doc lai)
Muc tieu: chung minh file pcap do scapy ghi ra duoc tshark doc lai DUNG
          so goi va DUNG truong, khong phai phong doan.

CORPUS VO HAI: 1 truy van DNS cho ten mien reserved "example.invalid"
                (RFC 2606/6761 — khong the phan giai that, khong goi mang).
KHONG goi mang: moi dia chi MAC/IP duoc dat tuong minh nen scapy khong ARP.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"
CORPUS.mkdir(exist_ok=True)
PCAP = CORPUS / "dns_harmless.pcap"

from scapy.all import DNS, DNSQR, Ether, IP, UDP, rdpcap, wrpcap  # noqa: E402

FAILURES = []      # lech GIA TRI that su (sau khi chuan hoa)
REPR_DIFFS = []    # chi lech CACH BIEU DIEN (hex vs thap phan, bool vs int)


def _norm(v):
    """Chuan hoa bieu dien ve dang so nguyen de so sanh GIA TRI, khong so sanh chuoi."""
    if v is None:
        return None
    s = str(v).strip()
    if s.lower() in ("true", "false"):
        return int(s.lower() == "true")
    try:
        return int(s, 0)      # hieu ca '0x1234' va '4660'
    except ValueError:
        return s


def check(label, a, b, normalize=True):
    raw_same = (str(a) == str(b))
    if normalize:
        ok = (_norm(a) == _norm(b))
    else:
        ok = raw_same
    if ok and not raw_same:
        tag = "PASS*"
        REPR_DIFFS.append((label, a, b))
    else:
        tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {label}: scapy={a!r} tshark={b!r}")
    if tag == "PASS*":
        print(f"         ^ chi lech BIEU DIEN, gia tri tuong duong: "
              f"{_norm(a)!r} == {_norm(b)!r}")
    if not ok:
        FAILURES.append(label)
    return ok


def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# ---------------------------------------------------------------- BUOC 1: GHI
section("BUOC 1 — scapy DUNG va GHI file pcap")
print(f"# corpus: {PCAP}")
print("# Ten mien 'example.invalid' thuoc RFC 2606/6761 — reserved, vo hai.")

pkt = (
    Ether(src="02:00:00:00:00:01", dst="02:00:00:00:00:02")
    / IP(src="192.0.2.10", dst="192.0.2.53")   # 192.0.2.0/24 = TEST-NET-1, RFC 5737
    / UDP(sport=40000, dport=53)
    / DNS(id=0x1234, qr=0, opcode=0, rd=1, qdcount=1,
          qd=DNSQR(qname="example.invalid", qtype="A", qclass="IN"))
)
pkt.time = 1700000000.0  # timestamp co dinh => ket qua tai lap duoc

print("\n$ python -c \"...scapy: Ether/IP/UDP/DNS...\"; wrpcap(...)\"")
print(f"  packet built: {pkt.summary()}")
print(f"  packet bytes: {len(bytes(pkt))} byte")
print(f"  packet.show():\n{pkt.show(dump=True)}")

wrpcap(str(PCAP), [pkt])
print(f"  -> da ghi: {PCAP} ({PCAP.stat().st_size} byte)")

# ------------------------------------------------------------- BUOC 2: DOC LAI
section("BUOC 2 — scapy DOC LAI chinh file vua ghi (self round-trip)")
back = rdpcap(str(PCAP))
print(f"  scapy doc lai: {len(back)} goi")
p = back[0]
scapy_fields = {
    "frame_count": len(back),
    "eth_src": p[Ether].src,
    "eth_dst": p[Ether].dst,
    "ip_src": p[IP].src,
    "ip_dst": p[IP].dst,
    "ip_proto": p[IP].proto,
    "udp_sport": p[UDP].sport,
    "udp_dport": p[UDP].dport,
    "dns_id": p[DNS].id,
    "dns_qr": p[DNS].qr,
    "dns_qdcount": p[DNS].qdcount,
    "dns_qname": p[DNS].qd.qname.decode(),
    "dns_qtype": p[DNS].qd.qtype,
    "dns_qclass": p[DNS].qd.qclass,
}
for k, v in scapy_fields.items():
    print(f"    scapy.{k} = {v!r}")

# --------------------------------------------------------------- BUOC 3: TSHARK
section("BUOC 3 — tshark DOC LAI file do scapy ghi")
tshark = shutil.which("tshark") or "tshark"
ver = subprocess.run([tshark, "--version"], capture_output=True, text=True)
print(f"# tshark version: {ver.stdout.splitlines()[0] if ver.stdout else ver.stderr.strip()}")

print(f"\n$ tshark -r {PCAP}")
r = subprocess.run([tshark, "-r", str(PCAP)], capture_output=True, text=True)
print("--- stdout ---")
print(r.stdout.rstrip() or "(rong)")
print("--- stderr ---")
print(r.stderr.rstrip() or "(rong)")
tshark_pkt_lines = [ln for ln in r.stdout.splitlines() if ln.strip()]

FIELDS = ["frame.number", "eth.src", "eth.dst", "ip.src", "ip.dst", "ip.proto",
          "udp.srcport", "udp.dstport", "dns.id", "dns.flags.response",
          "dns.count.queries", "dns.qry.name", "dns.qry.type", "dns.qry.class"]
cmd = [tshark, "-r", str(PCAP), "-T", "fields", "-E", "separator=|"] + [
    a for f in FIELDS for a in ("-e", f)
]
print(f"\n$ {' '.join(cmd)}")
r2 = subprocess.run(cmd, capture_output=True, text=True)
print("--- stdout ---")
print(r2.stdout.rstrip() or "(rong)")
if r2.stderr.strip():
    print("--- stderr ---")
    print(r2.stderr.rstrip())
tshark_row = r2.stdout.strip().split("|") if r2.stdout.strip() else []
tshark_fields = dict(zip(FIELDS, tshark_row))
print("\n--- tshark parsed ---")
for k, v in tshark_fields.items():
    print(f"    tshark.{k} = {v!r}")

# ------------------------------------------------------------- BUOC 4: DOI CHIEU
section("BUOC 4 — DOI CHIEU truong giua scapy va tshark")
print("So goi:")
check("frame_count", len(back), len(tshark_pkt_lines))
check("dns.count.queries", str(scapy_fields["dns_qdcount"]), tshark_fields.get("dns.count.queries"))

print("\nTruong goi:")
check("eth.src", scapy_fields["eth_src"], tshark_fields.get("eth.src"))
check("eth.dst", scapy_fields["eth_dst"], tshark_fields.get("eth.dst"))
check("ip.src", scapy_fields["ip_src"], tshark_fields.get("ip.src"))
check("ip.dst", scapy_fields["ip_dst"], tshark_fields.get("ip.dst"))
check("ip.proto", str(scapy_fields["ip_proto"]), tshark_fields.get("ip.proto"))
check("udp.srcport", str(scapy_fields["udp_sport"]), tshark_fields.get("udp.srcport"))
check("udp.dstport", str(scapy_fields["udp_dport"]), tshark_fields.get("udp.dstport"))
check("dns.id", str(scapy_fields["dns_id"]), tshark_fields.get("dns.id"))
check("dns.flags.response", str(scapy_fields["dns_qr"]), tshark_fields.get("dns.flags.response"))
check("dns.qry.name (bo dau cham cuoi)",
      scapy_fields["dns_qname"].rstrip("."), tshark_fields.get("dns.qry.name"))
check("dns.qry.type", str(scapy_fields["dns_qtype"]), tshark_fields.get("dns.qry.type"))
check("dns.qry.class", str(scapy_fields["dns_qclass"]), tshark_fields.get("dns.qry.class"))

# ---------------------------------------------------------------------- KET LUAN
section("KET LUAN T15-1")
print(json.dumps({"scapy_fields": scapy_fields, "tshark_fields": tshark_fields,
                  "failures_value_mismatch": FAILURES,
                  "repr_only_differences": [{"field": f, "scapy": str(a), "tshark": str(b)}
                                            for f, a, b in REPR_DIFFS]},
                 ensure_ascii=False, indent=2))
print(f"\n  So truong doi chieu        : 14")
print(f"  Lech GIA TRI that su       : {len(FAILURES)}")
print(f"  Chi lech BIEU DIEN (PASS*) : {len(REPR_DIFFS)}")
if REPR_DIFFS:
    print("\n  GHI CHU VE CAC LECH BIEU DIEN (KHONG phai loi du lieu):")
    for f, a, b in REPR_DIFFS:
        print(f"    - {f}: scapy bieu dien {a!r}, tshark bieu dien {b!r} "
              f"=> cung gia tri {_norm(a)!r}")
    print("  => Bai hoc: SO SANH CHUOI THO giua 2 cong cu se bao 'lech' gia.")
    print("     Phai chuan hoa ve gia tri (int(x,0), bool) truoc khi ket luan.")
if FAILURES:
    print(f"\n>>> KET QUA: {len(FAILURES)} LECH GIA TRI THAT SU: {FAILURES}")
    sys.exit(1)
print("\n>>> KET QUA: 0 LECH GIA TRI — scapy<->tshark nhat quan tren 14 truong.")
print("    LUU Y: corpus VO HAI tu tao; KHONG goi mang that.")
