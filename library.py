from book import Book
from member import Member
from datetime import datetime
import json


class Library:
    """Lớp quản lý thư viện"""

    def __init__(self, name="Thư viện Trung tâm"):
        self.name = name
        self.books = {}  # Dict với key là book_id
        self.members = {}  # Dict với key là member_id
        self.transactions = []  # Lịch sử giao dịch

    # Quản lý sách
    def add_book(self, book_id, title, author, isbn, publication_year, copies=1):
        """Thêm sách mới vào thư viện"""
        if book_id in self.books:
            # Nếu sách đã tồn tại, tăng số lượng
            self.books[book_id].total_copies += copies
            self.books[book_id].available_copies += copies
            return f"Đã thêm {copies} bản của sách '{title}'"
        else:
            # Thêm sách mới
            book = Book(book_id, title, author, isbn, publication_year, copies)
            self.books[book_id] = book
            return f"Đã thêm sách mới: '{title}'"

    def remove_book(self, book_id):
        """Xóa sách khỏi thư viện"""
        if book_id in self.books:
            book = self.books[book_id]
            if len(book.borrowed_by) > 0:
                return f"Không thể xóa sách. Còn {len(book.borrowed_by)} bản đang được mượn"
            del self.books[book_id]
            return f"Đã xóa sách: '{book.title}'"
        return "Không tìm thấy sách"

    def search_books(self, keyword="", by="title"):
        """Tìm kiếm sách theo tiêu đề, tác giả hoặc ISBN"""
        results = []
        keyword = keyword.lower()

        for book in self.books.values():
            if by == "title" and keyword in book.title.lower():
                results.append(book)
            elif by == "author" and keyword in book.author.lower():
                results.append(book)
            elif by == "isbn" and keyword in book.isbn:
                results.append(book)
            elif by == "all" and (keyword in book.title.lower() or
                                  keyword in book.author.lower() or
                                  keyword in book.isbn):
                results.append(book)

        return results

    # Quản lý thành viên
    def add_member(self, member_id, name, email, phone, membership_type="Thường"):
        """Thêm thành viên mới"""
        if member_id in self.members:
            return f"Thành viên với ID {member_id} đã tồn tại"

        member = Member(member_id, name, email, phone, membership_type)
        self.members[member_id] = member
        return f"Đã thêm thành viên: {name}"

    def remove_member(self, member_id):
        """Xóa thành viên"""
        if member_id in self.members:
            member = self.members[member_id]
            if len(member.borrowed_books) > 0:
                return f"Không thể xóa thành viên. Còn {len(member.borrowed_books)} sách chưa trả"
            del self.members[member_id]
            return f"Đã xóa thành viên: {member.name}"
        return "Không tìm thấy thành viên"

    def search_members(self, keyword=""):
        """Tìm kiếm thành viên theo tên hoặc email"""
        results = []
        keyword = keyword.lower()

        for member in self.members.values():
            if (keyword in member.name.lower() or
                    keyword in member.email.lower()):
                results.append(member)

        return results

    # Quản lý mượn/trả sách
    def borrow_book(self, member_id, book_id):
        """Mượn sách"""
        # Kiểm tra thành viên
        if member_id not in self.members:
            return "Không tìm thấy thành viên"

        # Kiểm tra sách
        if book_id not in self.books:
            return "Không tìm thấy sách"

        member = self.members[member_id]
        book = self.books[book_id]

        # Kiểm tra điều kiện mượn
        if not member.can_borrow():
            return f"Thành viên không thể mượn thêm sách (đã mượn {len(member.borrowed_books)}/{member.max_books})"

        if not book.is_available():
            return f"Sách '{book.title}' hiện không có sẵn"

        # Thực hiện mượn sách
        if member.borrow_book(book_id) and book.borrow_book(member_id):
            # Ghi lại giao dịch
            transaction = {
                'type': 'borrow',
                'member_id': member_id,
                'member_name': member.name,
                'book_id': book_id,
                'book_title': book.title,
                'date': datetime.now(),
                'due_date': member.borrowed_books[-1]['due_date']
            }
            self.transactions.append(transaction)

            return f"Đã mượn sách '{book.title}' cho {member.name}"

        return "Có lỗi xảy ra khi mượn sách"

    def return_book(self, member_id, book_id):
        """Trả sách"""
        # Kiểm tra thành viên
        if member_id not in self.members:
            return "Không tìm thấy thành viên"

        # Kiểm tra sách
        if book_id not in self.books:
            return "Không tìm thấy sách"

        member = self.members[member_id]
        book = self.books[book_id]

        # Thực hiện trả sách
        if member.return_book(book_id) and book.return_book(member_id):
            # Ghi lại giao dịch
            transaction = {
                'type': 'return',
                'member_id': member_id,
                'member_name': member.name,
                'book_id': book_id,
                'book_title': book.title,
                'date': datetime.now()
            }
            self.transactions.append(transaction)

            return f"Đã trả sách '{book.title}' từ {member.name}"

        return "Thành viên này không mượn sách này"

    # Báo cáo và thống kê
    def get_overdue_books(self):
        """Lấy danh sách sách quá hạn"""
        overdue_list = []
        for member in self.members.values():
            overdue_books = member.get_overdue_books()
            for overdue_book in overdue_books:
                book = self.books[overdue_book['book_id']]
                overdue_list.append({
                    'member': member,
                    'book': book,
                    'days_overdue': (datetime.now() - overdue_book['due_date']).days,
                    'due_date': overdue_book['due_date']
                })
        return overdue_list

    def get_statistics(self):
        """Lấy thống kê thư viện"""
        total_books = sum(book.total_copies for book in self.books.values())
        available_books = sum(book.available_copies for book in self.books.values())
        borrowed_books = total_books - available_books

        active_members = sum(1 for member in self.members.values() if member.is_active)
        members_with_books = sum(1 for member in self.members.values() if len(member.borrowed_books) > 0)

        overdue_count = len(self.get_overdue_books())

        return {
            'Tổng số đầu sách': len(self.books),
            'Tổng số bản sách': total_books,
            'Sách có sẵn': available_books,
            'Sách đang được mượn': borrowed_books,
            'Tổng số thành viên': len(self.members),
            'Thành viên hoạt động': active_members,
            'Thành viên đang mượn sách': members_with_books,
            'Sách quá hạn': overdue_count,
            'Tổng giao dịch': len(self.transactions)
        }

    def save_data(self, filename="library_data.json"):
        """Lưu dữ liệu thư viện vào file"""
        data = {
            'library_name': self.name,
            'books': {},
            'members': {},
            'transactions': []
        }

        # Lưu sách
        for book_id, book in self.books.items():
            data['books'][book_id] = book.get_info()

        # Lưu thành viên
        for member_id, member in self.members.items():
            member_data = member.get_info()
            member_data['borrowed_books'] = member.borrowed_books
            member_data['borrow_history'] = member.borrow_history
            data['members'][member_id] = member_data

        # Lưu giao dịch (chuyển datetime thành string)
        for transaction in self.transactions:
            trans_data = transaction.copy()
            trans_data['date'] = transaction['date'].isoformat()
            if 'due_date' in transaction:
                trans_data['due_date'] = transaction['due_date'].isoformat()
            data['transactions'].append(trans_data)

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return f"Đã lưu dữ liệu vào {filename}"
        except Exception as e:
            return f"Lỗi khi lưu dữ liệu: {str(e)}"

    def __str__(self):
        stats = self.get_statistics()
        return f"""{self.name}
Sách: {stats['Tổng số đầu sách']} đầu, {stats['Tổng số bản sách']} bản ({stats['Sách có sẵn']} có sẵn)
Thành viên: {stats['Tổng số thành viên']} ({stats['Thành viên hoạt động']} hoạt động)
Giao dịch: {stats['Tổng giao dịch']}"""