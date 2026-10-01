# Agent: javis

Thư mục territory của agent `javis` (`ag_3bef07fd`, slot 10 theo D-012).
Task con nằm trong `tasks/<task_id>/`.

- **Môi trường:** VM Linux riêng của người dùng (`/home/hatch`), độc lập với máy `/home/noble-tran` của các worker khác — phù hợp vai trò truy hồi/kiểm chứng từ môi trường khác.
- **Skill:** `agentmeet` tại `~/workspace/skills/agentmeet` (bản cài trên VM này).
- **Giới hạn đã khai ở check-in (msg #5):** không có MCP Packet Tracer; thư viện security-agent 817 skill không có trên VM này; SSH key của VM chưa được thêm vào GitHub của người dùng (push qua SSH chưa dùng được tại thời điểm check-in).
