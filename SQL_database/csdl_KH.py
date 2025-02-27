from SQL_database.ketnoiSQL import Database  
import sqlite3

class CustomerDatabase(Database):
    def get_all_customers(self):
        """Lấy toàn bộ danh sách khách hàng"""
        conn = self.connect()
        if conn is None:
            return [], []

        try:
            cursor = conn.cursor()
            
            # Kiểm tra bảng Customers tồn tại không
            cursor.execute("""
                SELECT name FROM sqlite_master WHERE type='table' AND name='Customers';
            """)
            if cursor.fetchone() is None:
                print("❌ Bảng 'Customers' không tồn tại.")
                return [], []

            # Truy vấn danh sách khách hàng
            cursor.execute("""
            SELECT customer_code, full_name, phone, email, address, note
            FROM Customers
            """)
            data = cursor.fetchall()
            columns = ["Mã KH", "Tên Khách Hàng", "Số Điện Thoại", "Email", "Địa Chỉ", "Ghi chú"]
            return columns, data
        
        except sqlite3.OperationalError as e:
            print("❌ Lỗi cơ sở dữ liệu (OperationalError):", e)
        except sqlite3.DatabaseError as e:
            print("❌ Lỗi truy vấn cơ sở dữ liệu:", e)
        finally:
            conn.close()

        return [], []

    def get_addresses(self):
        """Lấy danh sách địa chỉ khách hàng (không trùng lặp)"""
        conn = self.connect()
        if conn is None:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT DISTINCT address FROM Customers WHERE address IS NOT NULL AND address != ''")
            addresses = [row[0] for row in cursor.fetchall()]
            return addresses
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy danh sách địa chỉ: {e}")
        finally:
            conn.close()

        return []

    def get_customers_by_address(self, address):
        """Lọc khách hàng theo địa chỉ"""
        conn = self.connect()
        if conn is None:
            return []
        
        try:
            cursor = conn.cursor()
            if address == "Tất cả":
                cursor.execute("SELECT customer_code, full_name, phone, email, address,note FROM Customers")
            else:
                cursor.execute("""
                    SELECT customer_code, full_name, phone, email, address,note
                    FROM Customers WHERE address = ?
                """, (address,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lọc khách hàng theo địa chỉ: {e}")
        finally:
            conn.close()

        return []

    def get_customer_by_phone_or_email(self, phone_or_email):
        """Tìm khách hàng theo số điện thoại hoặc email"""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            query = """
                SELECT customer_code, full_name, phone, email, address, note
                FROM Customers WHERE phone = ? OR email = ?
            """
            cursor.execute(query, (phone_or_email, phone_or_email))
            

            results = cursor.fetchall()
            return results
        except sqlite3.Error as e:
            print(f"❌ Lỗi tìm kiếm nhân viên: {e}")
            return []
        finally:
            conn.close()
       
        


    def delete_customer(self, customer_code):
        """Xóa khách hàng theo Mã KH"""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Customers WHERE customer_code = ?", (customer_code,))
            if cursor.rowcount > 0:
                conn.commit()
                return True
            else:
                print("⚠ Không tìm thấy khách hàng để xóa.")
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi xóa khách hàng: {e}")
        finally:
            conn.close()

        return False

    def add_customer(self,  full_name, phone, email, address,note):
        """Thêm khách hàng mới"""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Customers ( full_name, phone, email, address,note)
                VALUES (?, ?, ?, ?,?)
            """, ( full_name, phone, email, address,note))
            conn.commit()
            return True
        
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi thêm khách hàng: {e}")
        finally:
            conn.close()

        return False

    def update_customer(self, customer_code, full_name, phone, email, address, note):
        """Cập nhật thông tin khách hàng"""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Customers
                SET full_name = ?, phone = ?, email = ?, address = ?,note = ?
                WHERE customer_code = ?
            """, (full_name, phone, email, address,note, customer_code))
            if cursor.rowcount > 0:
                conn.commit()
                return True
            else:
                print("⚠ Không tìm thấy khách hàng để cập nhật.")
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi cập nhật khách hàng: {e}")
        finally:
            conn.close()

        return False

    def get_customer_by_code(self, customer_code):
        """Lấy thông tin khách hàng dựa trên customer_code."""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            query = """
            SELECT customer_code, full_name, phone, email, address,note
            FROM Customers
            WHERE customer_code = ?
        """
            cursor.execute(query, (customer_code,))
            row = cursor.fetchone()

            if row:
                return {
                "customer_code": row[0],
                "full_name": row[1],
                "phone": row[2],
                "email": row[3],
                "address": row[4],
                "note": row[5]
            }
            return None
        except Exception as e:
            print(f"❌ Lỗi khi lấy thông tin khách hàng: {e}")
            return None
        finally:
            conn.close()

    def get_last_inserted_customer_id(self):
        """Lấy mã khách hàng vừa thêm cuối cùng"""
        conn = self.connect()  # Kết nối CSDL
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT customer_code FROM Customers ORDER BY customer_code DESC LIMIT 1")
            result = cursor.fetchone()
            return result[0] if result else None
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy mã khách hàng mới nhất: {e}")
            return None
        finally:
            conn.close()
