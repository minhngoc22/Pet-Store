import sqlite3
import os
import hashlib


class Database:
    def __init__(self, db_name=r"E:\HK6\DoAN\DoAn\CSDL\PetStore1.db"):
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


    
    @staticmethod
    def hash_password(password):
        """Hàm mã hóa mật khẩu bằng SHA-256"""
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def check_login(self, username, password):
        """Kiểm tra đăng nhập và trả về vai trò nếu đúng, ngược lại trả về None"""
        conn = self.connect()
        if conn is None:
            return None

        try:
            hashed_input_password = self.hash_password(password)  # Mã hóa mật khẩu nhập vào

            cursor = conn.cursor()
            cursor.execute("SELECT password, role FROM Users WHERE username = ?", (username,))
            result = cursor.fetchone()

            if result:
                stored_hashed_password, role = result  # Lấy mật khẩu và vai trò
                if hashed_input_password == stored_hashed_password:
                    return role  # Trả về vai trò nếu mật khẩu đúng

            return None  # Sai mật khẩu hoặc không tồn tại
        except sqlite3.Error as e:
            print("❌ Lỗi kiểm tra đăng nhập:", e)
            return None
        finally:
            conn.close()
