"""Bắt ClientHello THẬT bằng socket server giả — không cần tcpdump.
Server nhận kết nối, đọc byte đầu tiên client gửi (= ClientHello), rồi đóng.
"""
import socket, ssl, threading, struct, json, sys

def server(sock, out):
    conn, _ = sock.accept()
    conn.settimeout(2.0)
    data = b""
    try:
        while len(data) < 8192:
            b = conn.recv(4096)
            if not b: break
            data += b
            # đủ 5 byte header record + length?
            if len(data) >= 5:
                rec_len = struct.unpack(">H", data[3:5])[0]
                if len(data) >= 5 + rec_len:
                    break
    except socket.timeout:
        pass
    out.append(data)
    conn.close()

def tls_record_len(raw):
    """Trả về (record_len, handshake_msg_len, clienthello_total)."""
    if len(raw) < 5: return None
    rt, ver, rl = struct.unpack(">BHH", raw[:5])
    hs = raw[5:9]
    if len(hs) < 4: return None
    htype, hlen = hs[0], int.from_bytes(hs[1:4], "big")
    return dict(record_type=rt, record_len=rl, hs_type=htype, hs_len=hlen,
                bytes_on_wire=5 + rl)

def measure(label, ctx_kwargs, connect_kwargs):
    s = socket.socket(); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", 0)); s.listen(1)
    port = s.getsockname()[1]
    out = []
    t = threading.Thread(target=server, args=(s, out)); t.start()
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
    for k, v in ctx_kwargs.items(): setattr(ctx, k, v)
    c = socket.create_connection(("127.0.0.1", port))
    try:
        c = ctx.wrap_socket(c, **connect_kwargs)
    except Exception as e:
        pass
    t.join(timeout=3); s.close()
    try: c.close()
    except Exception: pass
    raw = out[0] if out else b""
    info = tls_record_len(raw)
    return dict(label=label, **info) if info else dict(label=label, error="no data", n=len(raw))

results = []
# 1. mặc định: TLS 1.2+1.3, không ALPN, không cache
results.append(measure("default (TLS1.2+1.3, no ALPN, no cache)", {}, {}))
# 2. chỉ TLS 1.3
results.append(measure("TLS1.3 only", {"minimum_version": ssl.TLSVersion.TLSv1_3}, {}))
# 3. TLS1.3 + ALPN h2,http/1.1
results.append(measure("TLS1.3 + ALPN h2,http/1.1", {"minimum_version": ssl.TLSVersion.TLSv1_3},
                       {"server_hostname": "localhost"}))
print(json.dumps(results, indent=2, ensure_ascii=False))
