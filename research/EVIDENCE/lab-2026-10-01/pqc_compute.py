"""Tự dựng ClientHello PQC từ ClientHello THẬT đo được + kích thước FIPS.
Không chép blog: mọi byte đều suy từ cấu trúc đã mổ ở bước trước.
"""
import json
# --- kích thước FIPS (byte) ---
FIPS = {
 "ML-KEM-768 ek": 1184, "ML-KEM-768 ct": 1088,
 "X25519 pk": 32, "P-256 pk": 65,
 "ML-DSA-44 pk": 1312, "ML-DSA-44 sig": 2420,
 "ML-DSA-65 pk": 1952, "ML-DSA-65 sig": 3309,
 "ML-DSA-87 pk": 2592, "ML-DSA-87 sig": 4627,
 "ECDSA P-256 pk": 65, "ECDSA P-256 sig": 72,
 "RSA-2048 pk": 272, "RSA-2048 sig": 256,
}
HYBRID_KS = FIPS["ML-KEM-768 ek"] + FIPS["X25519 pk"]   # key_share payload của X25519MLKEM768

# --- baseline ĐO ĐƯỢC ở bước trước (OpenSSL 3.0.13 / Python 3.12) ---
BASE = {
 "tls13_only": dict(wire=225, hs=216, ext_total=135, n_ext=9, cipher_suites=8,
                    key_share=38, supported_groups=22, sigalgs=30, padding=0, session_id=32),
 "default_12_13": dict(wire=517, hs=508, ext_total=373, n_ext=10, cipher_suites=62,
                       key_share=38, supported_groups=22, sigalgs=42, padding=220, session_id=32),
}
def pqc_variant(b, n_mldsa=3):
    """Thêm X25519MLKEM768 vào key_share + supported_groups, và n_mldsa mã ML-DSA vào sigalgs.
    Extension entry: 2B group + 2B keylen + payload.
    """
    d_ks   = (2+2+HYBRID_KS) - b["key_share"]           # thay entry cũ bằng entry lai? KHÔNG:
    # Go gửi CẢ HAI key share (X25519 và X25519MLKEM768) -> cộng thêm entry mới
    d_ks   = (2+2+HYBRID_KS)                            # entry MỚI, giữ entry cũ
    d_grp  = 2                                          # +1 mã nhóm trong supported_groups
    d_sig  = 2*n_mldsa                                  # +mã thuật toán chữ ký
    d_ext  = d_ks + d_grp + d_sig
    out = dict(b)
    out["key_share"] = b["key_share"] + d_ks
    out["supported_groups"] = b["supported_groups"] + d_grp
    out["sigalgs"] = b["sigalgs"] + d_sig
    out["ext_total"] = b["ext_total"] + d_ext
    out["hs"]  = b["hs"] + d_ext
    out["wire"]= b["wire"] + d_ext
    return out, d_ext

print("=== 1. ClientHello: baseline ĐO ĐƯỢC vs bản PQC TỰ DỰNG ===")
print(f"{'cấu hình':<34} {'baseline':>9} {'PQC':>7} {'+byte':>7}   {'1440B(IPv6)':>12} {'1460B(IPv4)':>12}")
rows={}
for k,b in BASE.items():
    p,d = pqc_variant(b)
    rows[k]=p
    v6 = "VƯỢT %d" % (p['wire']-1440) if p['wire']>1440 else "lọt"
    v4 = "VƯỢT %d" % (p['wire']-1460) if p['wire']>1460 else "lọt"
    print(f"{k:<34} {b['wire']:>9} {p['wire']:>7} {d:>+7}   {v6:>12} {v4:>12}")

print()
print("=== 2. Vì sao 'lọt/vượt' phụ thuộc cấu hình mạng (ngưỡng một gói TCP) ===")
p13 = rows["tls13_only"]["wire"]
for mtu,label in [(1460,"IPv4, không TS"),(1448,"IPv4 + TCP timestamp"),(1440,"IPv6"),(1428,"IPv6 + TS"),(1400,"đường hầm VPN")]:
    print(f"  {label:<24} MTU {mtu:>4}  ->  ClientHello {p13} B : {'VƯỢT %d B'%(p13-mtu) if p13>mtu else 'lọt'}")

print()
print("=== 3. key_share của X25519MLKEM768 — cộng từ FIPS ===")
print(f"  ML-KEM-768 ek {FIPS['ML-KEM-768 ek']} + X25519 {FIPS['X25519 pk']} = {HYBRID_KS} B payload")
print(f"  + 2B group + 2B length = {2+2+HYBRID_KS} B cho một entry key_share")
print(f"  so với entry X25519 thuần: 2+2+{FIPS['X25519 pk']} = {2+2+FIPS['X25519 pk']} B")
print(f"  => một entry lai chiếm ~{(2+2+HYBRID_KS)/(2+2+FIPS['X25519 pk']):.0f} lần entry thuần")

print()
print("=== 4. Chuỗi chứng thư mTLS 3 tầng — byte cho phần khoá CÔNG KHAI + CHỮ KÝ ===")
print(f"{'thuật toán':<14} {'1 tầng (pk+sig)':>17} {'3 tầng':>10} {'so ECDSA P-256':>16}")
base3 = 3*(FIPS["ECDSA P-256 pk"]+FIPS["ECDSA P-256 sig"])
for alg in ["ECDSA P-256","RSA-2048","ML-DSA-44","ML-DSA-65","ML-DSA-87"]:
    one = FIPS[f"{alg} pk"]+FIPS[f"{alg} sig"]
    three = 3*one
    print(f"{alg:<14} {one:>17} {three:>10} {three/base3:>15.1f}x")
print(f"  chênh lệch ML-DSA-65 vs ECDSA P-256 (3 tầng): {3*(FIPS['ML-DSA-65 pk']+FIPS['ML-DSA-65 sig'])-base3} byte")
