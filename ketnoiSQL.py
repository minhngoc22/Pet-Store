import mysql.connector

class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        """Kết nối MySQL"""
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="petshop"
            )
            self.cursor = self.conn.cursor()
            print("✅ [DB] Kết nối MySQL thành công!")
        except mysql.connector.Error as e:
            print(f"❌ [DB] Lỗi kết nối MySQL: {e}")
            self.conn = None
            self.cursor = None

    def check_login(self, username, password):
        """Kiểm tra đăng nhập"""
        if not self.conn:
            print("❌ [DB] Chưa kết nối tới cơ sở dữ liệu.")
            return False

        try:
            query = "SELECT * FROM users WHERE username = %s AND passH = %s"
            self.cursor.execute(query, (username, password))
            result = self.cursor.fetchone()
            if result:
                print(f"✅ Đăng nhập thành công: {username}")
                return True
            else:
                print("❌ Sai tài khoản hoặc mật khẩu.")
                return False
        except mysql.connector.Error as e:
            print(f"❌ [DB] Lỗi truy vấn: {e}")
            return False

    def close(self):
        """Đóng kết nối"""
        if self.conn:
            self.cursor.close()
            self.conn.close()
            print("🔴 [DB] Đã đóng kết nối MySQL!")
