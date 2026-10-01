import subprocess, os, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def run(*a, **kw):
    r = subprocess.run(a, capture_output=True, **kw)
    if r.returncode != 0:
        raise SystemExit(f"FAIL {a[:3]}...\n{r.stderr.decode()[:400]}")
    return r
def keygen(name, kind):
    if kind == "ecdsa":
        return ["-newkey","ec","-pkeyopt","ec_paramgen_curve:prime256v1"]
    if kind.startswith("rsa"):
        return ["-newkey", kind.replace("rsa","rsa:"), "-pkeyopt", "rsa_keygen_bits:"+kind.replace("rsa","")]
    raise ValueError(kind)

EKU_SERVER = "basicConstraints=critical,CA:FALSE\nkeyUsage=critical,digitalSignature\nextendedKeyUsage=serverAuth"
CA_EXT = "basicConstraints=critical,CA:TRUE\nkeyUsage=critical,keyCertSign,cRLSign"
def chain(tag, kind):
    kg = keygen(tag, kind)
    # root self-signed
    run("openssl","req","-x509",*kg,"-keyout",f"{tag}-root.key","-out",f"{tag}-root.pem",
        "-days","3650","-nodes","-subj",f"/C=VN/O=PQC Lab/CN={tag} Root CA",
        "-addext","basicConstraints=critical,CA:TRUE")
    # intermediate
    run("openssl","req",*kg,"-keyout",f"{tag}-int.key","-out",f"{tag}-int.csr",
        "-nodes","-subj",f"/C=VN/O=PQC Lab/CN={tag} Intermediate")
    open(f"{tag}-ca.ext","w").write(CA_EXT)
    run("openssl","x509","-req","-in",f"{tag}-int.csr","-CA",f"{tag}-root.pem","-CAkey",f"{tag}-root.key",
        "-CAcreateserial","-out",f"{tag}-int.pem","-days","1825","-extfile",f"{tag}-ca.ext")
    # leaf
    run("openssl","req",*kg,"-keyout",f"{tag}-leaf.key","-out",f"{tag}-leaf.csr",
        "-nodes","-subj",f"/C=VN/O=PQC Lab/CN={tag} Leaf")
    open(f"{tag}-leaf.ext","w").write(EKU_SERVER)
    run("openssl","x509","-req","-in",f"{tag}-leaf.csr","-CA",f"{tag}-int.pem","-CAkey",f"{tag}-int.key",
        "-CAcreateserial","-out",f"{tag}-leaf.pem","-days","365","-extfile",f"{tag}-leaf.ext")

def der(p): return len(subprocess.run(["openssl","x509","-in",p,"-outform","DER"],capture_output=True).stdout)

out = {}
for tag, kind in [("ecdsa_p256","ecdsa256"), ("rsa2048","rsa2048"), ("rsa3072","rsa3072")]:
    k = "ecdsa" if kind=="ecdsa256" else kind
    chain(tag, k)
    r,i,l = der(f"{tag}-root.pem"), der(f"{tag}-int.pem"), der(f"{tag}-leaf.pem")
    out[tag] = dict(root=r, inter=i, leaf=l, total=r+i+l)
    print(f"{tag:<12} root={r:>5}  inter={i:>5}  leaf={l:>5}  TỔNG DER={r+i+l:>6}")
print()
print("DER của chuỗi 3 tầng (byte):", json.dumps({k:v['total'] for k,v in out.items()}))
# kích thước phần khoá công khai THẬT trong leaf
for tag in out:
    t = subprocess.run(["openssl","x509","-in",f"{tag}-leaf.pem","-noout","-text"],capture_output=True).stdout.decode()
    for line in t.splitlines():
        if "Public-Key" in line: print(f"  {tag}: {line.strip()}")
