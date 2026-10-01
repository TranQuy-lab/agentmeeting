import subprocess, os, math
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def der(p):
    r = subprocess.run(["openssl","x509","-in",p,"-outform","DER"],capture_output=True)
    assert r.returncode==0 and r.stdout, f"KHÔNG ĐỌC ĐƯỢC {p}"
    return len(r.stdout)
TIERS = [("root","root"), ("inter","int"), ("leaf","leaf")]
SIG = {"ecdsa_p256":(65,72), "rsa2048":(272,256), "rsa3072":(422,384)}
print("=== overhead X.509 ĐO ĐƯỢC (cert_size - pk - sig) ===")
ov={}
for t,(pk,sig) in SIG.items():
    vals={}
    for name,fn in TIERS:
        vals[name]=der(f"{t}-{fn}.pem")-pk-sig
    ov[t]=vals
    print(f"  {t:<12} root={vals['root']:>4}  inter={vals['inter']:>4}  leaf={vals['leaf']:>4}")
R,I,L = ov["ecdsa_p256"]["root"], ov["ecdsa_p256"]["inter"], ov["ecdsa_p256"]["leaf"]
print(f"  => overhead KHÁ ỔN ĐỊNH giữa 3 thuật toán ⇒ dùng mốc root={R} inter={I} leaf={L} để ngoại suy")
print()
FIPS={"ECDSA P-256":(65,72),"RSA-2048":(272,256),"RSA-3072":(422,384),
      "ML-DSA-44":(1312,2420),"ML-DSA-65":(1952,3309),"ML-DSA-87":(2592,4627)}
print("=== chuỗi 3 tầng (DER thật cho 3 dòng đầu; ngoại suy cho ML-DSA) ===")
print(f"{'thuật toán':<12} {'root':>6} {'inter':>6} {'leaf':>6} {'3 tầng':>8} {'TLS Cert msg':>13} {'gói TCP':>8} {'so ECDSA':>9}")
res={}
for alg,(pk,sig) in FIPS.items():
    c=[R+pk+sig, I+pk+sig, L+pk+sig]; tot=sum(c)
    tls=1+3+sum(3+x for x in c)
    res[alg]=(c,tot,tls)
for alg,(c,tot,tls) in res.items():
    real = " (ĐO)" if alg in ("ECDSA P-256","RSA-2048","RSA-3072") else " (ngoại suy)"
    print(f"{alg:<12} {c[0]:>6} {c[1]:>6} {c[2]:>6} {tot:>8} {tls:>13} {math.ceil(tls/1460):>8} {tot/res['ECDSA P-256'][1]:>8.1f}x{real}")
print()
print("=== kiểm chứng chéo: ngoại suy ECDSA/RSA có khớp số ĐO không? ===")
for t,alg in [("ecdsa_p256","ECDSA P-256"),("rsa2048","RSA-2048"),("rsa3072","RSA-3072")]:
    meas = sum(der(f"{t}-{fn}.pem") for _,fn in TIERS)
    est  = res[alg][1]
    print(f"  {alg:<12} ĐO={meas:>5}  NGOẠI SUY={est:>5}  lệch={est-meas:>+4} B  ({abs(est-meas)/meas*100:.1f}%)")
