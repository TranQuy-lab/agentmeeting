"""Mổ ClientHello THẬT: liệt kê từng extension và số byte."""
import socket, ssl, threading, struct, json

def grab(ctx_kwargs):
    def server(sock, out):
        conn,_ = sock.accept(); conn.settimeout(2.0); data=b""
        try:
            while len(data)<16384:
                b=conn.recv(4096)
                if not b: break
                data+=b
                if len(data)>=5 and len(data)>=5+struct.unpack(">H",data[3:5])[0]: break
        except socket.timeout: pass
        out.append(data); conn.close()
    s=socket.socket(); s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind(("127.0.0.1",0)); s.listen(1); port=s.getsockname()[1]
    out=[]; t=threading.Thread(target=server,args=(s,out)); t.start()
    ctx=ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
    for k,v in ctx_kwargs.items(): setattr(ctx,k,v)
    c=socket.create_connection(("127.0.0.1",port))
    try: c=ctx.wrap_socket(c)
    except Exception: pass
    t.join(timeout=3); s.close()
    try: c.close()
    except Exception: pass
    return out[0]

def parse_ch(raw):
    """raw = record(5) + handshake(4) + ClientHello body."""
    hs = raw[5:]
    assert hs[0]==1, "không phải ClientHello"
    body = hs[4:]
    o=0
    legacy_ver = body[o:o+2]; o+=2
    random_ = body[o:o+32]; o+=32
    sid_len = body[o]; o+=1; sid=body[o:o+sid_len]; o+=sid_len
    cs_len = struct.unpack(">H", body[o:o+2])[0]; o+=2
    cs = body[o:o+cs_len]; o+=cs_len
    comp_len = body[o]; o+=1; comp=body[o:o+comp_len]; o+=comp_len
    ext_total_len = struct.unpack(">H", body[o:o+2])[0]; o+=2
    exts=[]
    end=o+ext_total_len
    while o < end:
        et = struct.unpack(">H", body[o:o+2])[0]; o+=2
        el = struct.unpack(">H", body[o:o+2])[0]; o+=2
        exts.append((et, el)); o+=el
    return dict(hs_len=struct.unpack(">I", b"\x00"+hs[1:4])[0],
                session_id_len=sid_len, cipher_suites_bytes=cs_len,
                n_ciphers=cs_len//2, compression_bytes=comp_len,
                ext_total=ext_total_len, n_ext=len(exts),
                cipher_suites=cs_len, exts=exts)

NAMES={0:"server_name",5:"status_request",10:"supported_groups",11:"ec_point_formats",
       13:"signature_algorithms",16:"ALPN",18:"SCT",21:"padding",23:"extended_master_secret",
       35:"session_ticket",41:"pre_shared_key",43:"supported_versions",44:"cookie",
       45:"psk_key_exchange_modes",51:"key_share",27:"compress_certificate",
       28:"record_size_limit",34:"delegated_credentials",65281:"renegotiation_info"}

for label, kw in [("TLS1.3 only", {"minimum_version": ssl.TLSVersion.TLSv1_3}),
                  ("TLS1.3 + ALPN", {"minimum_version": ssl.TLSVersion.TLSv1_3}),
                  ("default TLS1.2+1.3", {})]:
    raw = grab(kw)
    p = parse_ch(raw)
    print(f"=== {label} : {5+struct.unpack('>H',raw[3:5])[0]} byte trên dây ===")
    print(f"    hs_len={p['hs_len']} | session_id={p['session_id_len']} | cipher_suites={p['cipher_suites']} B ({p['n_ciphers']} suite) | ext_total={p['ext_total']} B / {p['n_ext']} ext")
    for et, el in p['exts']:
        print(f"      ext {et:>5} {NAMES.get(et,'?'):<24} {el:>4} B")
    print()
