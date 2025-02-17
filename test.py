from ketnoiSQL import Database

def test_database_connection():
    # Tạo đối tượng Database để kết nối
    db = Database()
    db.connect()
    # Kiểm tra đăng nhập với thông tin người dùng
    username = input("Nhập tên đăng nhập: ")
    password = input("Nhập mật khẩu: ")

    # Kiểm tra đăng nhập
    if db.check_login(username, password):
        print("✅ Đăng nhập thành công!")
    else:
        print("❌ Đăng nhập thất bại!")

    # Đóng kết nối
    db.close()

if __name__ == "__main__":
    test_database_connection()
