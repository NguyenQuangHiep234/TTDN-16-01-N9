# 🤖 HƯỚNG DẪN SỬ DỤNG GEMINI AI CHO QUẢN LÝ RỦI RO

**Module**: `project_management`  
**Tính năng**: Google Gemini AI Integration  
**Ngày**: 28/01/2026

---

## 📋 TỔNG QUAN

Hệ thống AI Quản lý Rủi ro đã được tích hợp với **Google Gemini AI** để:

- ✅ Phân tích mô tả dự án và tìm risks tiềm ẩn
- ✅ Generate mitigation plans thông minh, chi tiết
- ✅ Root cause analysis nâng cao (5 WHYs method)
- ✅ Comprehensive project analysis

## 🚀 CÀI ĐẶT VÀ CẤU HÌNH

### Bước 1: Lấy Google Gemini API Key

1. Truy cập: https://ai.google.dev/gemini-api/docs/api-key?hl=vi
2. Đăng nhập bằng Google Account
3. Click **"Get API key"** → **"Create API key in new project"**
4. Copy API key (dạng: `AIzaSy...`)

**Lưu ý:**

- API miễn phí với giới hạn **60 requests/phút**
- Không cần thanh toán, chỉ cần Google Account

### Bước 2: Cấu hình trong Odoo

1. Vào menu **PM** → **Gemini AI Settings**
2. Paste API key vào trường **API Key**
3. Chọn Model (khuyến nghị: **Gemini Pro**)
4. Điều chỉnh tham số (tùy chọn):
   - **Temperature**: 0.7 (0.0 = deterministic, 1.0 = creative)
   - **Max Tokens**: 2048
5. Click **"Test Connection"** để kiểm tra
6. Đánh dấu **Active** = ✅
7. Click **Save**

![Gemini Settings](docs/images/gemini_settings.png)

---

## 💡 CÁCH SỬ DỤNG

### 1. Tự động phân tích khi tạo dự án

Khi tạo dự án mới với **mô tả chi tiết**:

```
Tên dự án: Xây dựng hệ thống ERP
Mô tả:
Dự án phát triển hệ thống ERP toàn diện cho công ty 500 nhân viên.
Yêu cầu tích hợp với 5 hệ thống legacy hiện tại.
Deadline: 6 tháng
Team: 8 developers (junior), 2 QA
Budget: 500 triệu VND
```

**Gemini AI sẽ tự động:**

- Phân tích text → Phát hiện risks tiềm ẩn
- Tạo risk records với root cause và mitigation plans
- Kết hợp với rule-based AI để đánh giá toàn diện

### 2. Nâng cấp phân tích risks hiện có

Mở một risk record đã phát hiện:

1. Vào **PM** → **AI Quản lý rủi ro**
2. Chọn một risk cần nâng cấp
3. Click nút **"🤖 Nâng cấp với Gemini AI"**

**Gemini AI sẽ:**

- Phân tích nguyên nhân gốc rễ (5 WHYs)
- Generate mitigation plan chi tiết với:
  - Quick wins (1-2 ngày)
  - Giải pháp trung hạn (1-2 tuần)
  - Giải pháp dài hạn (phòng ngừa)
  - Người chịu trách nhiệm đề xuất
  - Metrics để đo lường

### 3. Test kết nối

Menu **PM** → **Gemini AI Settings** → Click **"Test Connection"**

**Kết quả:**

- ✅ Success: "Gemini API hoạt động bình thường"
- ❌ Error: Kiểm tra API key hoặc kết nối internet

---

## 📊 SO SÁNH: RULE-BASED AI vs GEMINI AI

| Tính năng                    | Rule-based AI          | Gemini AI                    |
| ---------------------------- | ---------------------- | ---------------------------- |
| **Phát hiện delay**          | ✅ Tính toán % delay   | ✅ + Context analysis        |
| **Phát hiện budget overrun** | ✅ Burn rate           | ✅ + Trend prediction        |
| **Phát hiện overload**       | ✅ Count tasks         | ✅ + Skill matching          |
| **Root cause analysis**      | ⚠️ Template cố định    | ✅ 5 WHYs method             |
| **Mitigation plan**          | ⚠️ Generic suggestions | ✅ Specific actionable steps |
| **Text analysis**            | ❌ Không có            | ✅ NLP từ mô tả dự án        |
| **Chi phí**                  | 🆓 Miễn phí            | 🆓 Free tier (60 req/min)    |
| **Offline**                  | ✅ Hoạt động offline   | ❌ Cần internet              |

---

## 🔄 LUỒNG HOẠT ĐỘNG TÍCH HỢP

```
┌─────────────────────────────────────────────────────────────┐
│ User tạo/cập nhật dự án                                     │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ BƯỚC 1: Rule-based AI Analysis                              │
│  - detect_schedule_risk()                                   │
│  - detect_budget_risk()                                     │
│  - detect_resource_risk()                                   │
│  → Tạo danh sách risks cơ bản                               │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ BƯỚC 2: Gemini AI Enhancement (nếu active)                  │
│                                                             │
│  IF project.description != empty:                           │
│    → gemini.analyze_project_description(project)            │
│    → Phát hiện risks từ text                                │
│    → Append vào danh sách                                   │
│                                                             │
│  (Tùy chọn: comprehensive_project_analysis)                 │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ BƯỚC 3: Create/Update Risk Records                          │
│  - Deduplication (tránh duplicate)                          │
│  - Tính risk_score & level                                  │
│  - Lưu vào database                                         │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ User có thể click "🤖 Nâng cấp với Gemini AI"               │
│  → Enhanced root cause analysis                             │
│  → Enhanced mitigation plan                                 │
└─────────────────────────────────────────────────────────────┘
```

---

## ⚙️ THAM SỐ CẤU HÌNH

### Temperature (0.0 - 1.0)

**Temperature** điều khiển độ "sáng tạo" của Gemini:

- **0.0 - 0.3**: Deterministic, consistent
  - Use case: Formal reports, documentation
- **0.4 - 0.7**: Balanced (Khuyến nghị ✅)
  - Use case: Risk analysis, mitigation plans
- **0.8 - 1.0**: Creative, varied
  - Use case: Brainstorming, alternatives

**Ví dụ:**

```python
Temperature = 0.7
Query: "Phân tích rủi ro dự án delay 30%"

Response:
- Nguyên nhân 1: Ước lượng không chính xác
- Nguyên nhân 2: Thiếu resource planning
- Giải pháp: Re-baseline timeline, bổ sung team
```

### Max Tokens

Giới hạn độ dài response:

- **512**: Ngắn gọn, tóm tắt
- **2048**: Chi tiết (Khuyến nghị ✅)
- **4096**: Rất chi tiết (chậm hơn)

---

## 📈 THỐNG KÊ SỬ DỤNG

Xem trong **Gemini AI Settings**:

```
Total Requests: 127
Last Used: 2026-01-28 14:35:22
```

**Lưu ý về Rate Limit:**

- Free tier: 60 requests/phút
- Nếu vượt: HTTP 429 Too Many Requests
- Hệ thống sẽ fallback về rule-based AI

---

## 🐛 TROUBLESHOOTING

### Lỗi: "API Key chưa được cấu hình"

**Nguyên nhân:** Chưa nhập API key  
**Giải pháp:** Vào Gemini AI Settings → Nhập API key

### Lỗi: "google-generativeai library not installed"

**Nguyên nhân:** Thư viện chưa cài  
**Giải pháp:**

```bash
pip3 install google-generativeai==0.3.2
```

### Lỗi: "Invalid API key"

**Nguyên nhân:** API key sai hoặc expired  
**Giải pháp:**

1. Kiểm tra API key có dạng `AIzaSy...`
2. Tạo API key mới tại https://ai.google.dev

### Lỗi: "Rate limit exceeded"

**Nguyên nhân:** Vượt 60 requests/phút  
**Giải pháp:**

- Đợi 1 phút
- Hệ thống tự động fallback về rule-based AI

### Warning: "Gemini AI not available or error"

**Nguyên nhân:** Không kết nối internet hoặc Gemini service down  
**Giải pháp:**

- Kiểm tra kết nối internet
- Hệ thống tiếp tục dùng rule-based AI

---

## 🔒 BẢO MẬT

### API Key Security

- ✅ API key được lưu trong database Odoo (encrypted tùy config)
- ✅ Field type = `password` → không hiển thị plain text
- ⚠️ Chỉ user có quyền `base.group_system` mới xem được

### Data Privacy

**Dữ liệu gửi đến Gemini API:**

- Tên dự án
- Mô tả dự án
- Thông tin risks (name, description, root_cause)
- Metrics (tiến độ, ngân sách, số tasks)

**KHÔNG gửi:**

- Thông tin nhân viên cá nhân (tên, email, lương)
- Tài liệu bảo mật
- Mật khẩu

**Khuyến nghị:**

- Tránh ghi thông tin nhạy cảm trong mô tả dự án
- Sử dụng mô tả general, không cụ thể quá

---

## 🎯 BEST PRACTICES

### 1. Viết mô tả dự án chi tiết

**Bad ❌:**

```
Mô tả: Làm website
```

**Good ✅:**

```
Mô tả:
Phát triển website thương mại điện tử B2C.
Yêu cầu:
- Tích hợp payment gateway (VNPay, Momo)
- Hỗ trợ 10,000 concurrent users
- Mobile responsive
- Admin dashboard với analytics

Team:
- 3 backend developers (Python/Django)
- 2 frontend developers (React)
- 1 designer (junior)

Constraints:
- Deadline cố định: 3 tháng
- Budget: 300 triệu VND
- Legacy database cần migrate
```

→ Gemini AI sẽ phát hiện được nhiều risks tiềm ẩn hơn!

### 2. Dùng Gemini AI cho risks quan trọng

- ✅ Critical và High risks: Nâng cấp với Gemini AI
- ⚠️ Medium risks: Tùy chọn
- ❌ Low risks: Không cần thiết

### 3. Review và chỉnh sửa kết quả

Gemini AI là **assistant**, không phải **replacement**:

- Đọc kỹ root cause analysis
- Điều chỉnh mitigation plan cho phù hợp
- Thêm context cụ thể của công ty

### 4. Monitor usage

Theo dõi **Total Requests** để tránh hit rate limit:

- < 50 requests/ngày: Bình thường
- > 100 requests/ngày: Cân nhắc optimize
- > 500 requests/ngày: Cần upgrade plan (paid tier)

---

## 📚 TÀI LIỆU THAM KHẢO

- Google Gemini API Docs: https://ai.google.dev/gemini-api/docs
- API Key Guide: https://ai.google.dev/gemini-api/docs/api-key
- Python SDK: https://github.com/google/generative-ai-python
- Pricing: https://ai.google.dev/pricing

---

## 🎉 KẾT LUẬN

Với **Google Gemini AI Integration**, hệ thống quản lý rủi ro của bạn giờ đây:

1. 🧠 **Thông minh hơn**: NLP analysis từ text, 5 WHYs root cause
2. 📈 **Chính xác hơn**: Kết hợp rule-based + AI insights
3. 💡 **Hữu ích hơn**: Actionable mitigation plans, không generic
4. 🆓 **Miễn phí**: Free tier đủ cho hầu hết use cases

**Next Steps:**

1. Lấy API key tại https://ai.google.dev
2. Cấu hình trong Odoo
3. Test với 1-2 dự án thử nghiệm
4. Deploy toàn bộ!

---

**Version**: 1.0  
**Last Updated**: 28/01/2026  
**Support**: Contact PM team
