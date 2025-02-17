# database.py
import sqlite3
import csdl

class Database:
    def __init__(self, db_name=r'csdl\PetShop.db'):
        self.db_name = db_name

    def check_connection(self):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cursor.fetchall()
                print("Danh sách bảng trong cơ sở dữ liệu:", tables)
        except sqlite3.Error as e:
            print("Lỗi kết nối với cơ sở dữ liệu:", e)

    def check_login(self, username, password):
        """
        Kiểm tra thông tin đăng nhập của người dùng.
        Trả về True nếu tìm thấy user, ngược lại trả về False.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM users 
                    WHERE username = ? AND passH = ?
                """, (username, password))
                result = cursor.fetchone()
            return True if result else False
        except sqlite3.Error as e:
            print("Lỗi trong quá trình check_in:", e)
            return False
