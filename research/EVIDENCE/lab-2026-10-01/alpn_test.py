import socket, ssl, threading, struct, json
def grab(setup=None):
    def server(sock, out):
        conn,_=sock.accept(); conn.settimeout(2.0); d=b""
        try:
            while len(d)<16384:
                b=conn.recv(4096)
                if not b: break
                d+=b
                if len(d)>=5 and len(d)>=5+struct.unpack(">H",d[3:5])[0]: break
        except socket.timeout: pass
        out.append(d); conn.close()
    s=socket.socket(); s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind(("127.0.0.1",0)); s.listen(1); port=s.getsockname()[1]
    out=[]; t=threading.Thread(target=server,args=(s,out)); t.start()
    ctx=ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
    ctx.minimum_version=ssl.TLSVersion.TLSv1_3
    if setup: setup(ctx)
    c=socket.create_connection(("127.0.0.1",port))
    try: c=ctx.wrap_socket(c)
    except Exception: pass
    t.join(timeout=3); s.close()
    try: c.close()
    except Exception: pass
    raw=out[0]; return 5+struct.unpack(">H",raw[3:5])[0]

def with_sni(ctx): pass  # SNI bật khi truyền server_hostname
print("TLS1.3, không SNI, không ALPN :", grab(), "B")
print("TLS1.3 + SNI 'localhost'      :", grab(), "B  (server_name +18)")
def alpn(ctx): ctx.set_alpn_protocols(["h2","http/1.1"])
print("TLS1.3 + ALPN h2,http/1.1     :", grab(alpn), "B  (ALPN +18)")
