import sqlite3
import os

class Database:
    def __init__(self, db_name=r"E:\HK6\DoAN\DoAn\CSDL\PetStore.db"):
        """Khởi tạo đối tượng Database với đường dẫn đến SQLite DB."""
        self.db_name = os.path.abspath(db_name)  
        self.conn = None  

    def connect(self):
        """Kết nối với CSDL SQLite."""
        try:
            if not os.path.exists(self.db_name):
                print(f"❌ Không tìm thấy file CSDL: {self.db_name}")
                return None  

            self.conn = sqlite3.connect(self.db_name)
            return self.conn  
        except sqlite3.Error as e:
            print("❌ Lỗi kết nối CSDL:", e)
            return None  

    def close(self):
        """Đóng kết nối với CSDL."""
        if self.conn:
            self.conn.close()
            self.conn = None

    def execute_query(self, query, params=None):
        """Thực hiện truy vấn SQL và trả về kết quả."""
        conn = self.connect()
        if conn is None:
            return []

        try:
            cursor = conn.cursor()
            cursor.execute(query, params or ())  
            results = cursor.fetchall()  
            return results
        except sqlite3.Error as e:
            print("❌ Lỗi thực thi truy vấn:", e)
            return []
        finally:
            conn.close()

    def check_login(self, username, password):
        """Kiểm tra đăng nhập với username và password."""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Users WHERE username = ? AND password = ?", (username, password))
            result = cursor.fetchone()
            return result is not None  
        except sqlite3.Error as e:
            print("❌ Lỗi kiểm tra đăng nhập:", e)
            return False
        finally:
            conn.close()
