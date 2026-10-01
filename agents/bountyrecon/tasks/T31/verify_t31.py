#!/usr/bin/env python3
"""verify_t31.py — T31 (BountyRecon)

Chứng minh: mọi vùng NGOÀI các dòng đã sửa là GIỐNG HỆT TỪNG BYTE.

QUY ƯỚC RANH GIỚI (ghi rõ theo yêu cầu D-023 / Admin T31 — Reviewer1 từng lệch 1 ký tự
vì quy ước khác):
  * Tách file thành các DÒNG bằng `str.splitlines()`.
    - Bỏ ký tự kết thúc dòng (\n, \r\n). KHÔNG giữ dấu xuống dòng ở cuối mỗi dòng.
  * Một "vùng" = `"\n".join(dòng_a .. dòng_b)`, hai đầu ĐÓNG (inclusive), 1-based.
    - KHÔNG có ký tự \n ở cuối vùng, TRỪ KHI quy ước ghi rõ là có.
  * Vì vậy để triệt tiêu mọi tranh cãi về 1 ký tự, script in hash của MỖI VÙNG
    theo HAI quy ước: (A) KHÔNG \n cuối, (B) CÓ \n cuối.
    => Nếu cả A và B đều khớp trước/sau thì kết luận KHÔNG phụ thuộc quy ước.
  * Vùng "đã sửa" xác định bằng difflib.SequenceMatcher trên danh sách dòng
    (opcodes 'replace'/'delete'/'insert'), KHÔNG bằng số dòng đoán tay.
"""
import difflib
import hashlib
import subprocess
import sys

FILES = ["security/gitlab/RECON.md", "agents/bountyrecon/tasks/T3/CANDIDATES.md"]


def h(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def load(f, rev):
    if rev == "WORK":
        return open(f, encoding="utf-8").read().splitlines()
    out = subprocess.run(["git", "show", f"{rev}:{f}"], capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit(f"loi git show {rev}:{f}: {out.stderr}")
    return out.stdout.splitlines()


def main():
    print("# verify_t31.py — T31 (BountyRecon)")
    print("# QUY UOC RANH GIOI: dong = splitlines() (bo \\n cuoi dong);")
    print("#   vung = '\\n'.join(dong_a..dong_b), 1-based, hai dau DONG; khong co \\n o cuoi vung.")
    print("#   Moi vung in hash theo 2 quy uoc: (A) khong \\n cuoi, (B) co \\n cuoi.")
    print()
    total_changed = 0
    all_ok = True
    for f in FILES:
        before = load(f, "HEAD")
        after = load(f, "WORK")
        sm = difflib.SequenceMatcher(a=before, b=after, autojunk=False)
        ops = [o for o in sm.get_opcodes() if o[0] != "equal"]
        changed_a, changed_b = set(), set()
        for tag, i1, i2, j1, j2 in ops:
            changed_a.update(range(i1, i2))
            changed_b.update(range(j1, j2))
        total_changed += len(changed_a)

        print("=" * 78)
        print(f"FILE: {f}")
        print(f"  blob TRUOC (HEAD) : {subprocess.run(['git','rev-parse',f'HEAD:{f}'],capture_output=True,text=True).stdout.strip()}")
        print(f"  blob SAU          : {subprocess.run(['git','hash-object',f],capture_output=True,text=True).stdout.strip()}")
        print(f"  so dong TRUOC={len(before)}  SAU={len(after)}")
        print(f"  opcodes khac: {[(o[0],o[1]+1,o[2],o[3]+1,o[4]) for o in ops]}")
        print()
        # liet ke dong da doi
        print("  DONG DA SUA (theo difflib):")
        for tag, i1, i2, j1, j2 in ops:
            print(f"    [{tag}] TRUOC dong {i1+1}..{i2}  ->  SAU dong {j1+1}..{j2}")
            for k in range(i1, i2):
                print(f"      - {before[k][:120]}")
            for k in range(j1, j2):
                print(f"      + {after[k][:120]}")
        print()
        # cac vung KHONG doi
        print("  VUNG KHONG DOI (moi vung phai GIONG HET):")
        blocks = sm.get_matching_blocks()
        for bi, blk in enumerate(blocks):
            if blk.size == 0:
                continue
            xa = before[blk.a:blk.a + blk.size]
            xb = after[blk.b:blk.b + blk.size]
            sa, sb = "\n".join(xa), "\n".join(xb)
            ok_a = h(sa) == h(sb)
            ok_b = h(sa + "\n") == h(sb + "\n")
            all_ok &= ok_a and ok_b
            print(f"    V{bi}: TRUOC dong {blk.a+1}..{blk.a+blk.size} (SAU {blk.b+1}..{blk.b+blk.size}) "
                  f"n={blk.size}")
            print(f"        (A) khong \\n cuoi: {h(sa)} vs {h(sb)}  -> {'GIONG HET' if ok_a else 'KHAC !!'}")
            print(f"        (B) co    \\n cuoi: {h(sa+chr(10))} vs {h(sb+chr(10))}  -> {'GIONG HET' if ok_b else 'KHAC !!'}")
        print()
    print("=" * 78)
    print(f"TONG dong da sua (2 file): {total_changed}")
    print(f"KET LUAN: moi vung khong doi GIONG HET theo CA HAI quy uoc: {all_ok}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
