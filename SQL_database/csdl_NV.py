from SQL_database.ketnoiSQL import Database  
import sqlite3

class EmployeeDatabase(Database):
    def get_all_employees(self):
        """Lấy toàn bộ danh sách nhân viên (Bao gồm ID)"""
        conn = self.connect()
        if conn is None:
            return [], []

        try:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT  employee_code, full_name, phone, email, address, salary, position, note 
            FROM Employees
            """)
            data = cursor.fetchall()
            columns = [ "Mã NV", "Tên Nhân Viên", "SĐT", "Email", "Địa Chỉ", "Lương", "Vị trí","Ghi chú"]
            return columns, data
        except sqlite3.Error as e:
            print("❌ Lỗi lấy danh sách nhân viên:", e)
            return [], []
        finally:
            conn.close()



    def add_employee(self, full_name, phone, email, address, salary, position,note):
        """Thêm nhân viên mới"""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Employees (full_name, phone, email, address, salary, position,note) 
                VALUES (?, ?, ?, ?, ?, ?,?)
            """, (full_name, phone, email, address, salary, position,note))

            conn.commit()
            print(f"✅ Thêm nhân viên '{full_name}' thành công!")
            return True
        except sqlite3.Error as e:
            print("❌ Lỗi khi thêm nhân viên:", e)
            return False
        finally:
            conn.close()

    def delete_employee(self,  employee_code):
        """Xóa nhân viên theo ID."""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM  Employees WHERE employee_code = ?", ( employee_code,))
            conn.commit()
            print(f"🗑️ Xóa sản phẩm có ID {id} thành công!")
            return True
        except sqlite3.Error as e:
            print("❌ Lỗi khi xóa sản phẩm:", e)
            return False
        finally:
            conn.close()

    def update_employee(self, employee_code, full_name, phone, email, address, salary, position,note):
        """Cập nhật thông tin nhân viên dựa vào ID"""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            query = """
        UPDATE Employees
        SET full_name = ?, phone = ?, email = ?, address = ?, salary = ?, position = ?, note = ?
        WHERE employee_code = ?
        """
            cursor.execute(query, (full_name, phone, email, address, salary, position,note, employee_code))
            conn.commit()
            print(f"✅ Cập nhật nhân viên có ID {employee_code} thành công!")
            return True
        except sqlite3.Error as e:
            print(f"❌ Lỗi cập nhật nhân viên: {e}")
            return False
        finally:
            conn.close()


    def search_employee_by_name(self, search_text):
        """Tìm kiếm nhân viên theo tên"""
        conn = self.connect()
        if conn is None:
            return []

        try:
            cursor = conn.cursor()
            query = """
            SELECT  employee_code, full_name, phone, email, address, salary, position,note
            FROM Employees
            WHERE full_name LIKE ?
            """
            cursor.execute(query, (f"%{search_text}%",))
            results = cursor.fetchall()
            return results
        except sqlite3.Error as e:
            print(f"❌ Lỗi tìm kiếm nhân viên: {e}")
            return []
        finally:
            conn.close()

    
    def get_positions(self):
        """Lấy danh sách vị trí từ CSDL"""
        conn = self.connect()
        if conn is None:
            return []

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT DISTINCT position FROM Employees")
            positions = [row[0] for row in cursor.fetchall()]
            print("Danh sách vị trí lấy từ CSDL:", positions)  # Debug
            return positions
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy danh sách vị trí: {e}")
            return []
        finally:
            conn.close()

    def get_employees_by_position(self, position):
        """Lấy danh sách nhân viên theo vị trí"""
        conn = self.connect()
        if conn is None:
            return []

        try:
            cursor = conn.cursor()
            if position == "Tất cả":
                cursor.execute("SELECT employee_code, full_name, phone, email, address, salary, position ,note FROM Employees")
            else:
                cursor.execute(
                "SELECT employee_code, full_name, phone, email, address, salary, position, note FROM Employees WHERE position = ?",
                    (position,))
        
            employees = cursor.fetchall()
            print(f"⚡ Debug - Nhân viên theo vị trí [{position}]:", employees)  # Debug
            return employees
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy nhân viên theo vị trí: {e}")
            return []
        finally:
            conn.close()

    def get_employee_by_code(self, employee_code):
        """Lấy thông tin nhân viên dựa trên employee_code."""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            query = """
                SELECT employee_code, full_name, phone, email, address, salary, position ,note
                FROM Employees
                WHERE employee_code = ?
        """
            cursor.execute(query, (employee_code,))
            row = cursor.fetchone()

            if row:
                return {
                "employee_code": row[0],
                "full_name": row[1],
                "phone": row[2],
                "email": row[3],
                "address": row[4],
                "salary": row[5],
                "position": row[6],
                "note" : row[7]
            }
            return None
        except Exception as e:
            print(f"❌ Lỗi khi lấy thông tin nhân viên: {e}")
            return None
        finally:
            conn.close()

