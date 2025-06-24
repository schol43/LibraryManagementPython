from library import Library
from datetime import datetime


def print_menu():
    """Hiển thị menu chính"""
    print("\n" + "=" * 50)
    print("🏛️  HỆ THỐNG QUẢN LÝ THƯ VIỆN")
    print("=" * 50)
    print("1.  📚 Quản lý sách")
    print("2.  👥 Quản lý thành viên")
    print("3.  📖 Mượn sách")
    print("4.  📬 Trả sách")
    print("5.  🔍 Tìm kiếm sách")
    print("6.  👤 Tìm kiếm thành viên")
    print("7.  ⚠️  Sách quá hạn")
    print("8.  📊 Thống kê")
    print("9.  💾 Lưu dữ liệu")
    print("0.  🚪 Thoát")
    print("-" * 50)


def print_book_menu():
    """Menu quản lý sách"""
    print("\n📚 QUẢN LÝ SÁCH")
    print("-" * 30)
    print("1. Thêm sách mới")
    print("2. Xóa sách")
    print("3. Danh sách tất cả sách")
    print("4. Thông tin chi tiết sách")
    print("0. Quay lại")


def print_member_menu():
    """Menu quản lý thành viên"""
    print("\n👥 QUẢN LÝ THÀNH VIÊN")
    print("-" * 30)
    print("1. Thêm thành viên mới")
    print("2. Xóa thành viên")
    print("3. Danh sách tất cả thành viên")
    print("4. Thông tin chi tiết thành viên")
    print("0. Quay lại")


def manage_books(library):
    """Quản lý sách"""
    while True:
        print_book_menu()
        choice = input("Chọn chức năng: ").strip()

        if choice == "1":
            # Thêm sách mới
            print("\n➕ THÊM SÁCH MỚI")
            book_id = input("ID sách: ").strip()
            title = input("Tiêu đề: ").strip()
            author = input("Tác giả: ").strip()
            isbn = input("ISBN: ").strip()
            try:
                year = int(input("Năm xuất bản: "))
                copies = int(input("Số lượng bản (mặc định 1): ") or "1")
                result = library.add_book(book_id, title, author, isbn, year, copies)
                print(f"✅ {result}")
            except ValueError:
                print("❌ Năm xuất bản và số lượng phải là số")

        elif choice == "2":
            # Xóa sách
            print("\n🗑️  XÓA SÁCH")
            book_id = input("ID sách cần xóa: ").strip()
            result = library.remove_book(book_id)
            print(f"✅ {result}")

        elif choice == "3":
            # Danh sách sách
            print("\n📋 DANH SÁCH TẤT CẢ SÁCH")
            if not library.books:
                print("Chưa có sách nào trong thư viện")
            else:
                for book in library.books.values():
                    print(f"  {book}")

        elif choice == "4":
            # Thông tin chi tiết sách
            print("\n🔍 THÔNG TIN CHI TIẾT SÁCH")
            book_id = input("ID sách: ").strip()
            if book_id in library.books:
                book_info = library.books[book_id].get_info()
                for key, value in book_info.items():
                    print(f"  {key}: {value}")
            else:
                print("❌ Không tìm thấy sách")

        elif choice == "0":
            break
        else:
            print("❌ Lựa chọn không hợp lệ")


def manage_members(library):
    """Quản lý thành viên"""
    while True:
        print_member_menu()
        choice = input("Chọn chức năng: ").strip()

        if choice == "1":
            # Thêm thành viên mới
            print("\n➕ THÊM THÀNH VIÊN MỚI")
            member_id = input("ID thành viên: ").strip()
            name = input("Họ tên: ").strip()
            email = input("Email: ").strip()
            phone = input("Số điện thoại: ").strip()
            print("Loại thành viên:")
            print("1. Thường (3 sách, 14 ngày)")
            print("2. VIP (10 sách, 30 ngày)")
            print("3. Sinh viên (5 sách, 21 ngày)")

            type_choice = input("Chọn loại (1-3, mặc định 1): ").strip() or "1"
            membership_types = {"1": "Thường", "2": "VIP", "3": "Sinh viên"}
            membership_type = membership_types.get(type_choice, "Thường")

            result = library.add_member(member_id, name, email, phone, membership_type)
            print(f"✅ {result}")

        elif choice == "2":
            # Xóa thành viên
            print("\n🗑️  XÓA THÀNH VIÊN")
            member_id = input("ID thành viên cần xóa: ").strip()
            result = library.remove_member(member_id)
            print(f"✅ {result}")

        elif choice == "3":
            # Danh sách thành viên
            print("\n📋 DANH SÁCH TẤT CẢ THÀNH VIÊN")
            if not library.members:
                print("Chưa có thành viên nào")
            else:
                for member in library.members.values():
                    print(f"  {member}")

        elif choice == "4":
            # Thông tin chi tiết thành viên
            print("\n🔍 THÔNG TIN CHI TIẾT THÀNH VIÊN")
            member_id = input("ID thành viên: ").strip()
            if member_id in library.members:
                member_info = library.members[member_id].get_info()
                for key, value in member_info.items():
                    print(f"  {key}: {value}")

                # Hiển thị sách đang mượn
                member = library.members[member_id]
                if member.borrowed_books:
                    print("\n  📚 Sách đang mượn:")
                    for book_info in member.borrowed_books:
                        book = library.books[book_info['book_id']]
                        due_date = book_info['due_date'].strftime('%d/%m/%Y')
                        print(f"    - {book.title} (Hạn trả: {due_date})")
            else:
                print("❌ Không tìm thấy thành viên")

        elif choice == "0":
            break
        else:
            print("❌ Lựa chọn không hợp lệ")


def borrow_book(library):
    """Mượn sách"""
    print("\n📖 MƯỢN SÁCH")
    member_id = input("ID thành viên: ").strip()
    book_id = input("ID sách: ").strip()

    result = library.borrow_book(member_id, book_id)
    if "Đã mượn sách" in result:
        print(f"✅ {result}")
    else:
        print(f"❌ {result}")


def return_book(library):
    """Trả sách"""
    print("\n📬 TRẢ SÁCH")
    member_id = input("ID thành viên: ").strip()
    book_id = input("ID sách: ").strip()

    result = library.return_book(member_id, book_id)
    if "Đã trả sách" in result:
        print(f"✅ {result}")
    else:
        print(f"❌ {result}")


def search_books(library):
    """Tìm kiếm sách"""
    print("\n🔍 TÌM KIẾM SÁCH")
    print("1. Tìm theo tiêu đề")
    print("2. Tìm theo tác giả")
    print("3. Tìm theo ISBN")
    print("4. Tìm tất cả")

    search_type = input("Chọn kiểu tìm kiếm (1-4): ").strip()
    keyword = input("Nhập từ khóa: ").strip()

    search_types = {"1": "title", "2": "author", "3": "isbn", "4": "all"}
    search_by = search_types.get(search_type, "title")

    results = library.search_books(keyword, search_by)

    if results:
        print(f"\n🎯 Tìm thấy {len(results)} kết quả:")
        for book in results:
            print(f"  {book}")
    else:
        print("❌ Không tìm thấy sách nào")


def search_members(library):
    """Tìm kiếm thành viên"""
    print("\n👤 TÌM KIẾM THÀNH VIÊN")
    keyword = input("Nhập tên hoặc email: ").strip()

    results = library.search_members(keyword)

    if results:
        print(f"\n🎯 Tìm thấy {len(results)} kết quả:")
        for member in results:
            print(f"  {member}")
    else:
        print("❌ Không tìm thấy thành viên nào")


def show_overdue_books(library):
    """Hiển thị sách quá hạn"""
    print("\n⚠️  SÁCH QUÁ HẠN")
    overdue_list = library.get_overdue_books()

    if not overdue_list:
        print("✅ Không có sách nào quá hạn")
    else:
        print(f"❌ Có {len(overdue_list)} sách quá hạn:")
        for item in overdue_list:
            member = item['member']
            book = item['book']
            days_overdue = item['days_overdue']
            due_date = item['due_date'].strftime('%d/%m/%Y')

            print(f"  📚 {book.title}")
            print(f"     👤 {member.name} (ID: {member.member_id})")
            print(f"     📅 Hạn trả: {due_date}")
            print(f"     ⏰ Quá hạn: {days_overdue} ngày")
            print()


def show_statistics(library):
    """Hiển thị thống kê"""
    print("\n📊 THỐNG KÊ THƯ VIỆN")
    stats = library.get_statistics()

    print("=" * 40)
    for key, value in stats.items():
        print(f"{key:.<30} {value}")
    print("=" * 40)


def save_data(library):
    """Lưu dữ liệu"""
    print("\n💾 LƯU DỮ LIỆU")
    filename = input("Tên file (Enter để dùng mặc định): ").strip()
    if not filename:
        filename = "library_data.json"

    result = library.save_data(filename)
    print(f"✅ {result}")


def create_sample_data(library):
    """Tạo dữ liệu mẫu để test"""
    print("🔧 Đang tạo dữ liệu mẫu...")

    # Thêm sách mẫu
    sample_books = [
        ("B001", "Lập trình Python", "Nguyễn Văn A", "978-0134444321", 2020, 3),
        ("B002", "Khoa học dữ liệu", "Trần Thị B", "978-1449319793", 2019, 2),
        ("B003", "Trí tuệ nhân tạo", "Lê Văn C", "978-0262035613", 2021, 2),
        ("B004", "Cơ sở dữ liệu", "Phạm Thị D", "978-0321523068", 2018, 1),
        ("B005", "An toàn thông tin", "Hoàng Văn E", "978-0134093413", 2020, 2)
    ]

    for book_data in sample_books:
        library.add_book(*book_data)

    # Thêm thành viên mẫu
        sample_members = [
        ("M001", "Nguyễn Văn Nam", "nam@email.com", "0901234567", "VIP"),
        ("M002", "Trần Thị Lan", "lan@email.com", "0901234568", "Sinh viên"),
        ("M003", "Lê Văn Hùng", "hung@email.com", "0901234569", "Thường"),
        ("M004", "Phạm Thị Mai", "mai@email.com", "0901234570", "Thường")
    ]

    for member_data in sample_members:
        library.add_member(*member_data)

    # Thực hiện một số giao dịch mượn sách
    library.borrow_book("M001", "B001")
    library.borrow_book("M002", "B002")
    library.borrow_book("M003", "B003")

    print("✅ Đã tạo dữ liệu mẫu thành công!")


def main():
    """Hàm main"""
    # Tạo thư viện
    library = Library("Thư viện Trung tâm Hà Nội")

    print("🎉 Chào mừng đến với Hệ thống Quản lý Thư viện!")
    print(f"📍 {library.name}")

    # Hỏi người dùng có muốn tạo dữ liệu mẫu không
    create_sample = input("\nBạn có muốn tạo dữ liệu mẫu để test không? (y/n): ").strip().lower()
    if create_sample == 'y':
        create_sample_data(library)

    # Vòng lặp chính
    while True:
        print_menu()
        choice = input("Chọn chức năng (0-9): ").strip()

        if choice == "1":
            manage_books(library)
        elif choice == "2":
            manage_members(library)
        elif choice == "3":
            borrow_book(library)
        elif choice == "4":
            return_book(library)
        elif choice == "5":
            search_books(library)
        elif choice == "6":
            search_members(library)
        elif choice == "7":
            show_overdue_books(library)
        elif choice == "8":
            show_statistics(library)
        elif choice == "9":
            save_data(library)
        elif choice == "0":
            print("\n👋 Cảm ơn bạn đã sử dụng hệ thống!")
            print("🔒 Đang đóng chương trình...")
            break
        else:
            print("❌ Lựa chọn không hợp lệ. Vui lòng chọn từ 0-9.")

        # Tạm dừng để người dùng đọc kết quả
        input("\n📝 Nhấn Enter để tiếp tục...")


if __name__ == "__main__":
    main()