
/* T15 — bo rule kiem chuan. Corpus VO HAI do ForensicsMal tu tao. */

rule t15_marker_alpha
{
    meta:
        y_don_do = "PHAI khop A; PHAI KHONG khop B/C/D/E (case-sensitive)"
    strings:
        $m = "FORENSICSMAL_T15_MARKER_ALPHA"
    condition:
        $m
}

rule t15_url_invalid
{
    meta:
        y_don_do = "PHAI khop B; PHAI KHONG khop A/C/D"
    strings:
        $u = /https?:\/\/[a-z0-9.\-]+\.invalid(\/[^\s]*)?/
    condition:
        $u
}

rule t15_case_insensitive
{
    meta:
        y_don_do = "PHAI khop CA A va C (nocase); PHAI KHONG khop D"
    strings:
        $m = "forensicsmal_t15_marker_alpha" nocase
    condition:
        $m
}

rule t15_absent_string
{
    meta:
        y_don_do = "KHONG duoc khop BAT KY file nao (bay bat duong tinh gia)"
    strings:
        $x = "THIS_MARKER_MUST_NOT_EXIST_ANYWHERE_T15"
    condition:
        $x
}

rule t15_mz_header_pe
{
    meta:
        y_don_do = "KHONG duoc khop file van ban nao (bay duong tinh gia); corpus khong co PE"
    condition:
        uint16(0) == 0x5A4D
}

rule t15_elf_magic
{
    meta:
        y_don_do = "PHAI khop E (ELF); KHONG khop file van ban"
    condition:
        uint32(0) == 0x464C457F
}

rule t15_boundary_marker
{
    meta:
        y_don_do = "PHAI khop F (marker STRADDLE moc chunk 4KB) — bay AM TINH GIA"
    strings:
        $m = "FORENSICSMAL_T15_MARKER_ALPHA"
    condition:
        $m
}

rule t15_wide_marker
{
    meta:
        y_don_do = "PHAI khop G (UTF-16LE); KHONG khop A (ASCII)"
    strings:
        $m = "FORENSICSMAL_T15_MARKER_ALPHA" wide
    condition:
        $m
}
