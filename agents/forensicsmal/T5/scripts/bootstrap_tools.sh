#!/usr/bin/env bash
# bootstrap_tools.sh — Dựng môi trường công cụ pháp y Python KHÔNG cần sudo
#
# Tác giả: ForensicsMal (ag_82f7cb07) — task T5
# Bối cảnh: máy này KHÔNG có `pip`/`ensurepip` và `sudo` đòi mật khẩu,
#           nhưng CÓ `uv` tại ~/.local/bin/uv ⇒ dựng venv riêng là khả thi.
#           Kiểm chứng thô: EVIDENCE/tool_inventory_raw.txt
#
# Dùng:  bash bootstrap_tools.sh [thư_mục_venv]
# Mặc định thư mục venv: ~/forensicsmal-tooling/.venv  (KHÔNG nằm trong repo ⇒ không bị commit)

set -euo pipefail

VENV_DIR="${1:-$HOME/forensicsmal-tooling/.venv}"
export PATH="$HOME/.local/bin:$PATH"

echo "[*] Kiểm tra uv..."
if ! command -v uv >/dev/null 2>&1; then
  echo "[!] THIẾU uv. Không tự cài được (sudo cần mật khẩu). Báo Admin." >&2
  exit 1
fi
uv --version

echo "[*] Tạo venv tại: $VENV_DIR"
uv venv "$VENV_DIR" --python 3.12

echo "[*] Cài gói pháp y (pefile, yara-python, scapy, capstone, oletools, volatility3)..."
uv pip install --python "$VENV_DIR/bin/python" \
  pefile yara-python scapy capstone oletools volatility3

echo "[*] Kiểm chứng phiên bản..."
"$VENV_DIR/bin/python" - <<'PY'
import importlib
for name, attr in [("pefile","__version__"),("scapy","__version__"),
                   ("capstone","__version__"),("volatility3","__version__")]:
    try:
        m = importlib.import_module(name)
        print(f"  {name}: {getattr(m, attr, 'ok')}")
    except Exception as e:
        print(f"  {name}: LỖI {e}")
for name in ("yara","oletools"):
    try:
        importlib.import_module(name); print(f"  {name}: ok")
    except Exception as e:
        print(f"  {name}: LỖI {e}")
PY

cat <<EOF

[+] Xong. Dùng công cụ qua:
      $VENV_DIR/bin/python
      $VENV_DIR/bin/vol        # volatility3 CLI (nếu cài thành công)

[!] LƯU Ý AN TOÀN:
    - KHÔNG chạy mẫu malware trên máy thật. Phân tích động cần môi trường cô lập ĐÃ XÁC MINH.
    - Gói hệ thống (binwalk, foremost, sleuthkit, yara CLI, zeek, exiftool) KHÔNG cài được
      nếu không có sudo/Admin. Ghi thẳng "thiếu" trong báo cáo, KHÔNG suy diễn thay.
EOF
