from datetime import datetime, timedelta


class Member:
    """Lớp đại diện cho thành viên thư viện"""

    def __init__(self, member_id, name, email, phone, membership_type="Thường"):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.membership_type = membership_type  # "Thường", "VIP", "Sinh viên"
        self.join_date = datetime.now()
        self.borrowed_books = []  # Danh sách ID sách đang mượn
        self.borrow_history = []  # Lịch sử mượn sách
        self.is_active = True

        # Giới hạn mượn sách theo loại thành viên
        self.max_books = self._get_max_books()
        self.max_days = self._get_max_days()

    def _get_max_books(self):
        """Lấy số sách tối đa có thể mượn theo loại thành viên"""
        limits = {
            "Thường": 3,
            "VIP": 10,
            "Sinh viên": 5
        }
        return limits.get(self.membership_type, 3)

    def _get_max_days(self):
        """Lấy số ngày mượn tối đa theo loại thành viên"""
        limits = {
            "Thường": 14,
            "VIP": 30,
            "Sinh viên": 21
        }
        return limits.get(self.membership_type, 14)

    def can_borrow(self):
        """Kiểm tra xem thành viên có thể mượn sách không"""
        return (self.is_active and
                len(self.borrowed_books) < self.max_books)

    def borrow_book(self, book_id):
        """Mượn sách"""
        if self.can_borrow():
            self.borrowed_books.append({
                'book_id': book_id,
                'borrow_date': datetime.now(),
                'due_date': datetime.now() + timedelta(days=self.max_days)
            })
            return True
        return False

    def return_book(self, book_id):
        """Trả sách"""
        for i, book in enumerate(self.borrowed_books):
            if book['book_id'] == book_id:
                returned_book = self.borrowed_books.pop(i)
                # Thêm vào lịch sử
                self.borrow_history.append({
                    'book_id': book_id,
                    'borrow_date': returned_book['borrow_date'],
                    'return_date': datetime.now(),
                    'due_date': returned_book['due_date']
                })
                return True
        return False

    def get_overdue_books(self):
        """Lấy danh sách sách quá hạn"""
        today = datetime.now()
        overdue = []
        for book in self.borrowed_books:
            if today > book['due_date']:
                overdue.append(book)
        return overdue

    def get_info(self):
        """Lấy thông tin chi tiết của thành viên"""
        return {
            'ID': self.member_id,
            'Tên': self.name,
            'Email': self.email,
            'Điện thoại': self.phone,
            'Loại thành viên': self.membership_type,
            'Ngày tham gia': self.join_date.strftime('%d/%m/%Y'),
            'Trạng thái': 'Hoạt động' if self.is_active else 'Không hoạt động',
            'Số sách đang mượn': len(self.borrowed_books),
            'Giới hạn mượn': self.max_books,
            'Sách quá hạn': len(self.get_overdue_books())
        }

    def __str__(self):
        return f"[{self.member_id}] {self.name} ({self.membership_type}) - {len(self.borrowed_books)}/{self.max_books} sách"