import mysql.connector

class Database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  # Thay bằng mật khẩu MySQL của bạn
                database="PetShop"
            )
            self.cursor = self.conn.cursor(dictionary=True)
            print("✅ Kết nối MySQL thành công!")
        except mysql.connector.Error as err:
            print(f"❌ Lỗi kết nối MySQL: {err}")

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
        print("🔌 Đã đóng kết nối MySQL")
