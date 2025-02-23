from SQL_database.ketnoiSQL import Database  
import sqlite3

class OrderDatabase(Database):
    def get_all_orders(self):
        """Lấy toàn bộ danh sách đơn hàng"""
        conn = self.connect()
        if conn is None:
            return [], []

        try:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT order_code, Customers.customer_code,Customers.full_name, total_amount, order_date, status, payment
            FROM Orders
            JOIN Customers ON Orders.customer_id = Customers.id
            """)
            data = cursor.fetchall()
            columns = ["Mã ĐH", "Mã Khách hàng","Tên KH", "Tổng Tiền", "Ngày Đặt", "Trạng Thái", "Thanh Toán"]
            return columns, data
        except sqlite3.Error as e:
            print("❌ Lỗi lấy danh sách đơn hàng:", e)
            return [], []
        finally:
            conn.close()

    def add_order(self, customer_id, employee_id, total_amount, status, payment):
        """Thêm đơn hàng mới"""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Orders (customer_id, employee_id, total_amount, status, payment)
                VALUES (?, ?, ?, ?, ?)
            """, (customer_id, employee_id, total_amount, status, payment))
            
            conn.commit()
            print("✅ Thêm đơn hàng thành công!")
            return True
        except sqlite3.Error as e:
            print("❌ Lỗi khi thêm đơn hàng:", e)
            return False
        finally:
            conn.close()

    def update_order(self, order_id, customer_id, employee_id, total_amount, status, payment):
        """Cập nhật thông tin đơn hàng"""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            query = """
            UPDATE Orders
            SET customer_id = ?, employee_id = ?, total_amount = ?, status = ?, payment = ?
            WHERE id = ?
            """
            cursor.execute(query, (customer_id, employee_id, total_amount, status, payment, order_id))
            conn.commit()
            print(f"✅ Cập nhật đơn hàng có ID {order_id} thành công!")
            return True
        except sqlite3.Error as e:
            print(f"❌ Lỗi cập nhật đơn hàng: {e}")
            return False
        finally:
            conn.close()

    def search_order_by_id(self, order_id):
        """Tìm kiếm đơn hàng theo mã đơn hàng"""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            query = """
            SELECT order_code, Customers.full_name, Customers.phone, Customers.email, Customers.address, total_amount, order_date, status, payment
            FROM Orders
            JOIN Customers ON Orders.customer_id = Customers.id
            WHERE Orders.id = ?
            """
            cursor.execute(query, (order_id,))
            row = cursor.fetchone()
            
            if row:
                return {
                    "order_code": row[0],
                    "customer_name": row[1],
                    "phone": row[2],
                    "email": row[3],
                    "address": row[4],
                    "total_amount": row[5],
                    "order_date": row[6],
                    "status": row[7],
                    "payment": row[8]
                }
            return None
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi tìm đơn hàng: {e}")
            return None
        finally:
            conn.close()

    def get_statuses(self):
        """Lấy danh sách vị trí từ CSDL"""
        conn = self.connect()
        if conn is None:
            return []

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT DISTINCT status FROM Orders")
            positions = [row[0] for row in cursor.fetchall()]
            print("Danh sách vị trí lấy từ CSDL:", positions)  # Debug
            return positions
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy danh sách vị trí: {e}")
            return []
        finally:
            conn.close()

    def get_order_by_status(self, status):
        """Lấy danh sách đơn hàng theo trạng thái"""
        conn = self.connect()
        if conn is None:
            return []

        try:
            cursor = conn.cursor()
            if status == "Tất cả":
                cursor.execute("""
                    SELECT order_code, Customers.customer_code, Customers.full_name, 
                           total_amount, order_date, status, payment
                    FROM Orders
                    JOIN Customers ON Orders.customer_id = Customers.id
                """)
            else:
                cursor.execute("""
                    SELECT order_code, Customers.customer_code, Customers.full_name, 
                           total_amount, order_date, status, payment
                    FROM Orders
                    JOIN Customers ON Orders.customer_id = Customers.id
                    WHERE status = ?
                """, (status,))

            orders = cursor.fetchall()
            print(f"⚡ Debug - Đơn hàng theo trạng thái [{status}]:", orders)  # Debug
            return orders
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy đơn hàng theo trạng thái: {e}")
            return []
        finally:
            conn.close()