from SQL_database.ketnoiSQL import Database  
import sqlite3
import hashlib  # Đảm bảo import thư viện hashlib

class UserDatabase(Database):
    def get_all_users(self):
        """Lấy danh sách tất cả người dùng"""
        conn = self.connect()
        if conn is None:
            return False, []

        try:
            cursor = conn.cursor()
            query = "SELECT  user_code, username, password,full_name, email, role,  note FROM Users"
            cursor.execute(query)
            users = cursor.fetchall()
            print(f"⚡ Debug - Dữ liệu người dùng: {users}")
            return True, users
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy danh sách người dùng: {e}")
            return False, []
        finally:
            conn.close()

    def add_user(self, username, password, full_name, email, role, note):
        """Thêm người dùng mới với mật khẩu đã được mã hóa"""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
        
        # Mã hóa mật khẩu bằng SHA-256
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            cursor.execute("""
            INSERT INTO Users (username, password, full_name, email, role, note) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (username, hashed_password, full_name, email, role, note))

            conn.commit()
            print(f"✅ Thêm người dùng '{username}' thành công!")
            return True
        except sqlite3.Error as e:
            print("❌ Lỗi khi thêm người dùng:", e)
            return False
        finally:
            conn.close()

    def delete_user(self, user_code):
        """Xóa người dùng theo ID"""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Users WHERE user_code = ?", (user_code,))
            conn.commit()
            print(f"🗑️ Xóa người dùng có ID {user_code} thành công!")
            return True
        except sqlite3.Error as e:
            print("❌ Lỗi khi xóa người dùng:", e)
            return False
        finally:
            conn.close()

    def update_user(self, user_code, username, full_name, role, password=None, note=""):
        """Cập nhật thông tin người dùng"""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()

        # Lấy vai trò hiện tại
            cursor.execute("SELECT role FROM Users WHERE user_code = ?", (user_code,))
            current_role = cursor.fetchone()

            if not current_role:
                print(f"❌ Không tìm thấy người dùng với ID {user_code}")
                return False

            current_role = current_role[0]

        # Nếu người dùng là "Khách hàng", không cho phép đổi role
            if current_role.lower() == "khách hàng":
                role = current_role  

        # Cập nhật thông tin
            if password:  # Nếu có mật khẩu mới
                query = """
            UPDATE Users
            SET username = ?, full_name = ?, role = ?, password = ?, note = ?
            WHERE user_code = ?
            """
                cursor.execute(query, (username, full_name, role, password, note, user_code))
            else:  # Nếu không có mật khẩu mới
                query = """
            UPDATE Users
            SET username = ?, full_name = ?, role = ?, note = ?
            WHERE user_code = ?
            """
                cursor.execute(query, (username, full_name, role, note, user_code))

            conn.commit()
            print(f"✅ Cập nhật người dùng ID {user_code} thành công!")
            return True

        except sqlite3.Error as e:
            print(f"❌ Lỗi cập nhật người dùng: {e}")
            return False

        finally:
            conn.close()

    def get_user_by_name(self, search_text):
        """Tìm kiếm người dùng theo tên đăng nhập, hỗ trợ tìm gần đúng bằng LIKE"""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            query = """
            SELECT user_code, username,password, full_name, email, role, note 
            FROM Users 
            WHERE full_name LIKE ?
        """
            cursor.execute(query, (f"%{search_text}%",))  # Tìm kiếm gần đúng bằng LIKE
            results = cursor.fetchall()
            return results
        except sqlite3.Error as e:
            print(f"❌ Lỗi tìm kiếm nhân viên: {e}")
            return []
        finally:
            conn.close()

    def get_user_by_code(self, user_code):
        """Lấy thông tin người dùng theo ID"""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            query = "SELECT  user_code, username, full_name,  role, note FROM Users WHERE user_code = ?"
            cursor.execute(query, (user_code,))
            user = cursor.fetchone()

            if user:
                return {
                    
                    "user_code": user[0],
                    "username": user[1],
                    "full_name": user[2],
                    "role": user[3],
                    "note": user[4]
                }
            return None
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy thông tin người dùng: {e}")
            return None
        finally:
            conn.close()

    def get_all_roles(self):
        """Lấy danh sách tất cả các vai trò từ bảng Users"""
        conn = self.connect()
        if conn is None:
            return []

        try:
            cursor = conn.cursor()
            query = "SELECT DISTINCT role FROM Users"
            cursor.execute(query)
            roles = [row[0] for row in cursor.fetchall()]
            print(f"✅ Danh sách vai trò: {roles}")
            return roles
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy danh sách vai trò: {e}")
            return []
        finally:
            conn.close()

    def get_users_by_role(self, role):
        """Lấy danh sách người dùng theo vai trò"""
        conn = self.connect()
        if conn is None:
            return False, []

        try:
            cursor = conn.cursor()
            if role == "Tất cả":
                query = "SELECT user_code, username,password, full_name, email, role, note FROM Users"
                cursor.execute(query)
            else:
                query = "SELECT user_code, username, full_name, email, role, note FROM Users WHERE role = ?"
                cursor.execute(query, (role,))
        
            users = cursor.fetchall()
            return True, users  # Trả về (bool, list)
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy danh sách người dùng theo vai trò: {e}")
            return False, []
        finally:
            conn.close()

