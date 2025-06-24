class Book:
    """Lớp đại diện cho một cuốn sách trong thư viện"""

    def __init__(self, book_id, title, author, isbn, publication_year, copies=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.total_copies = copies
        self.available_copies = copies
        self.borrowed_by = []  # Danh sách ID người mượn

    def is_available(self):
        """Kiểm tra xem sách có sẵn để mượn không"""
        return self.available_copies > 0

    def borrow_book(self, member_id):
        """Mượn sách"""
        if self.is_available():
            self.available_copies -= 1
            self.borrowed_by.append(member_id)
            return True
        return False

    def return_book(self, member_id):
        """Trả sách"""
        if member_id in self.borrowed_by:
            self.available_copies += 1
            self.borrowed_by.remove(member_id)
            return True
        return False

    def get_info(self):
        """Lấy thông tin chi tiết của sách"""
        return {
            'ID': self.book_id,
            'Tiêu đề': self.title,
            'Tác giả': self.author,
            'ISBN': self.isbn,
            'Năm xuất bản': self.publication_year,
            'Tổng số bản': self.total_copies,
            'Có sẵn': self.available_copies,
            'Đang được mượn bởi': self.borrowed_by
        }

    def __str__(self):
        return f"[{self.book_id}] {self.title} - {self.author} ({self.available_copies}/{self.total_copies} có sẵn)"