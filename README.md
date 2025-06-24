# 🏛️ Hệ Thống Quản Lý Thư Viện

Hệ thống quản lý thư viện đơn giản được xây dựng bằng Python sử dụng lập trình hướng đối tượng (OOP).

## 📋 Tính Năng

### 📚 Quản lý sách
- Thêm/xóa sách
- Tìm kiếm sách theo tiêu đề, tác giả, ISBN
- Xem thông tin chi tiết sách
- Quản lý số lượng bản sách

### 👥 Quản lý thành viên
- Thêm/xóa thành viên
- 3 loại thành viên: Thường, VIP, Sinh viên
- Giới hạn mượn sách khác nhau cho mỗi loại
- Tìm kiếm thành viên

### 📖 Mượn/Trả sách
- Mượn sách với kiểm tra điều kiện
- Trả sách và cập nhật trạng thái
- Theo dõi hạn trả sách
- Lịch sử giao dịch

### 📊 Báo cáo & Thống kê
- Danh sách sách quá hạn
- Thống kê tổng quan thư viện
- Lưu/đọc dữ liệu từ file JSON

## 🗂️ Cấu Trúc File

```
library_management/
├── book.py          # Lớp Book - Quản lý thông tin sách
├── member.py        # Lớp Member - Quản lý thông tin thành viên
├── library.py       # Lớp Library - Logic chính của hệ thống
├── main.py          # Chương trình chính với giao diện console
├── requirements.txt # Thư viện cần thiết
└── README.md        # File hướng dẫn này
```

## 🚀 Cách Chạy

1. **Tải về tất cả các file**
2. **Đảm bảo có Python 3.6+ được cài đặt**
3. **Chạy chương trình:**
   ```bash
   python main.py
   ```

## 🎯 Hướng Dẫn Sử Dụng

### Khởi động lần đầu
- Khi chạy chương trình, hệ thống sẽ hỏi có muốn tạo dữ liệu mẫu không
- Chọn 'y' để có sẵn một số sách và thành viên để test

### Menu chính
```
1. 📚 Quản lý sách
2. 👥 Quản lý thành viên  
3. 📖 Mượn sách
4. 📬 Trả sách
5. 🔍 Tìm kiếm sách
6. 👤 Tìm kiếm thành viên
7. ⚠️  Sách quá hạn
8. 📊 Thống kê
9. 💾 Lưu dữ liệu
0. 🚪 Thoát
```

## 📖 Chi Tiết Các Lớp

### Lớp Book (book.py)
```python
class Book:
    - book_id: ID duy nhất của sách
    - title: Tiêu đề sách
    - author: Tác giả
    - isbn: Mã ISBN
    - publication_year: Năm xuất bản
    - total_copies: Tổng số bản
    - available_copies: Số bản có sẵn
    - borrowed_by: Danh sách ID người mượn
```

**Phương thức chính:**
- `is_available()`: Kiểm tra sách có sẵn
- `borrow_book()`: Mượn sách
- `return_book()`: Trả sách
- `get_info()`: Lấy thông tin chi tiết

### Lớp Member (member.py)
```python
class Member:
    - member_id: ID thành viên
    - name: Họ tên
    - email: Email
    - phone: Số điện thoại
    - membership_type: Loại thành viên
    - borrowed_books: Sách đang mượn
    - borrow_history: Lịch sử mượn
```

**Loại thành viên:**
- **Thường**: 3 sách, 14 ngày
- **VIP**: 10 sách, 30 ngày  
- **Sinh viên**: 5 sách, 21 ngày

**Phương thức chính:**
- `can_borrow()`: Kiểm tra có thể mượn
- `borrow_book()`: Mượn sách
- `return_book()`: Trả sách
- `get_overdue_books()`: Lấy sách quá hạn

### Lớp Library (library.py)
Lớp chính quản lý toàn bộ hệ thống:

**Quản lý sách:**
- `add_book()`: Thêm sách
- `remove_book()`: Xóa sách
- `search_books()`: Tìm kiếm sách

**Quản lý thành viên:**
- `add_member()`: Thêm thành viên
- `remove_member()`: Xóa thành viên
- `search_members()`: Tìm kiếm thành viên

**Giao dịch:**
- `borrow_book()`: Xử lý mượn sách
- `return_book()`: Xử lý trả sách

**Báo cáo:**
- `get_overdue_books()`: Sách quá hạn
- `get_statistics()`: Thống kê
- `save_data()`: Lưu dữ liệu

## 💾 Lưu Trữ Dữ Liệu

- Dữ liệu được lưu dưới dạng JSON
- File mặc định: `library_data.json`
- Bao gồm: thông tin sách, thành viên, lịch sử giao dịch

## 🔧 Mở Rộng

Hệ thống có thể được mở rộng thêm:

1. **Giao diện web** (Flask/Django)
2. **Cơ sở dữ liệu** (SQLite/PostgreSQL)
3. **Báo cáo nâng cao** (Excel, PDF)
4. **Thông báo** (Email, SMS)
5. **Quản lý phạt** (Phí trễ hạn)
6. **Đặt trước sách**
7. **Quản lý nhiều chi nhánh**

## 🐛 Xử Lý Lỗi

- Kiểm tra đầu vào người dùng
- Xử lý lỗi file I/O
- Validation dữ liệu
- Thông báo lỗi rõ ràng

## 📝 Ghi Chú

- Hệ thống sử dụng 100% Python standard library
- Không cần cài đặt thêm package nào
- Phù hợp cho học tập và demo
- Code có comment tiếng Việt để dễ hiểu

## 🤝 Đóng Góp

Có thể cải thiện thêm:
- Unit tests
- Documentation
- Error handling
- Performance optimization
- UI/UX improvements

---
