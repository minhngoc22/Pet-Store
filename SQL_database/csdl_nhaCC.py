from SQL_database.ketnoiSQL import Database  
import sqlite3

class SupplierDatabase(Database):
    def get_all_suppliers(self):
        """Lấy toàn bộ danh sách nhà cung cấp"""
        conn = self.connect()
        if conn is None:
            return [], []

        try:
            cursor = conn.cursor()

            # Kiểm tra xem bảng Suppliers có tồn tại không
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Suppliers';")
            if cursor.fetchone() is None:
                print("❌ Bảng 'Suppliers' không tồn tại.")
                return [], []

            # Truy vấn danh sách nhà cung cấp
            cursor.execute("""
            SELECT supplier_code, name, phone, email, address, note
            FROM Suppliers
            """)
            data = cursor.fetchall()
            columns = ["Mã NCC", "Tên Nhà Cung Cấp", "Số Điện Thoại", "Email", "Địa Chỉ", "Ghi chú"]
            return columns, data

        except sqlite3.OperationalError as e:
            print("❌ Lỗi cơ sở dữ liệu (OperationalError):", e)
        except sqlite3.DatabaseError as e:
            print("❌ Lỗi truy vấn cơ sở dữ liệu:", e)
        finally:
            conn.close()

        return [], []

    def get_addresses(self):
        """Lấy danh sách địa chỉ nhà cung cấp (không trùng lặp)"""
        conn = self.connect()
        if conn is None:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT DISTINCT address FROM Suppliers WHERE address IS NOT NULL AND address != ''")
            addresses = [row[0] for row in cursor.fetchall()]
            return addresses
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy danh sách địa chỉ: {e}")
        finally:
            conn.close()

        return []

    def get_suppliers_by_address(self, address):
        """Lọc nhà cung cấp theo địa chỉ"""
        conn = self.connect()
        if conn is None:
            return []
        
        try:
            cursor = conn.cursor()
            if address == "Tất cả":
                cursor.execute("SELECT supplier_code, name, phone, email, address, note FROM Suppliers")
            else:
                cursor.execute("""
                    SELECT supplier_code, name, phone, email, address, note
                    FROM Suppliers WHERE address = ?
                """, (address,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lọc nhà cung cấp theo địa chỉ: {e}")
        finally:
            conn.close()

        return []

    def search_supplier_by_name(self, name):
        """Tìm kiếm nhà cung cấp theo tên"""
        conn = self.connect()
        if conn is None:
            return []
        
        try:
            cursor = conn.cursor()
            query = """
                SELECT supplier_code, name, phone, email, address, note
                FROM Suppliers
                WHERE name LIKE ?
            """
            cursor.execute(query, (f"%{name}%",))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi tìm kiếm nhà cung cấp: {e}")
        finally:
            conn.close()

        return []

    def delete_supplier(self, supplier_code):
        """Xóa nhà cung cấp theo Mã NCC"""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Suppliers WHERE supplier_code = ?", (supplier_code,))
            if cursor.rowcount > 0:
                conn.commit()
                return True
            else:
                print("⚠ Không tìm thấy nhà cung cấp để xóa.")
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi xóa nhà cung cấp: {e}")
        finally:
            conn.close()

        return False

    def add_supplier(self, name, phone, email, address, note=""):
        """Thêm nhà cung cấp mới"""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Suppliers (name, phone, email, address, note)
                VALUES (?, ?, ?, ?, ?)
            """, (name, phone, email, address, note))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("❌ Lỗi: Mã NCC đã tồn tại!")
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi thêm nhà cung cấp: {e}")
        finally:
            conn.close()

        return False

    def update_supplier(self, supplier_code, name, phone, email, address, note):
        """Cập nhật thông tin nhà cung cấp"""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Suppliers
                SET name = ?, phone = ?, email = ?, address = ?, note = ?
                WHERE supplier_code = ?
            """, (name, phone, email, address, note, supplier_code))
            if cursor.rowcount > 0:
                conn.commit()
                return True
            else:
                print("⚠ Không tìm thấy nhà cung cấp để cập nhật.")
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi cập nhật nhà cung cấp: {e}")
        finally:
            conn.close()

        return False

    def get_supplier_by_code(self, supplier_code):
        """Lấy thông tin nhà cung cấp theo mã NCC"""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            query = """
            SELECT supplier_code, name, phone, email, address, note
            FROM Suppliers
            WHERE supplier_code = ?
        """
            cursor.execute(query, (supplier_code,))
            row = cursor.fetchone()

            if row:
                return {
                "supplier_code": row[0],
                "name": row[1],
                "phone": row[2],
                "email": row[3],
                "address": row[4],
                "note": row[5]
            }
            return None
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy thông tin nhà cung cấp: {e}")
        finally:
            conn.close()

        return None
