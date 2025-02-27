from SQL_database.ketnoiSQL import Database  
import sqlite3

class OrderDatabase(Database):
    def get_all(self):
        """Lấy toàn bộ danh sách đơn hàng"""
        conn = self.connect()
        if conn is None:
            return [], []

        try:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT order_code, Customers.customer_code, total_amount, order_date, status, payment, Orders.note
FROM Orders
JOIN Customers ON Orders.customer_id = Customers.id

        """)
            data = cursor.fetchall()

        
            print("⚡ Debug - Dữ liệu đơn hàng:", data)  # Kiểm tra dữ liệu
            return  data
        except sqlite3.Error as e:
            print("❌ Lỗi lấy danh sách đơn hàng:", e)
            return [], []
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
            SELECT order_code, Customers.full_name, Customers.phone, Customers.email, Customers.address, total_amount, order_date, status, payment,note
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
                    "payment": row[8],
                    "note": row[9]
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
                    SELECT Orders.order_code, Customers.customer_code,
                           Orders.total_amount, Orders.order_date, Orders.status, Orders.payment, Orders.note
                    FROM Orders
                    JOIN Customers ON Orders.customer_id = Customers.id
                """)
            else:
                cursor.execute("""
                    SELECT Orders.order_code, Customers.customer_code, 
                           Orders.total_amount, Orders.order_date, Orders.status, Orders.payment, Orders.note
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

    def get_all_employees(self):
        """Lấy tất cả danh mục từ CSDL."""
        conn = self.connect()
        if conn is None:
            return []

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT full_name FROM Employees")
            return [row[0] for row in cursor.fetchall()]
        except Exception as e:
            print(f"❌ Lỗi lấy danh mục: {e}")
            return []
        finally:
            conn.close()

    def get_customer_by_phone_or_email(self, phone_or_email):
        """Tìm khách hàng theo số điện thoại hoặc email"""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            query = """
            SELECT customer_code
            FROM Customers 
            WHERE phone = ? OR email = ?
        """
            cursor.execute(query, (phone_or_email, phone_or_email))

            result = cursor.fetchone()  # Lấy một hàng duy nhất

            if result:  # Nếu có dữ liệu, trả về chuỗi
                return str(result[0])  # Chắc chắn trả về kiểu chuỗi
            else:
                return None  # Trả về None nếu không tìm thấy khách hàng

        except sqlite3.Error as e:
            print(f"❌ Lỗi tìm khách hàng: {e}")
            return None  

        finally:
            conn.close()

    def get_customer_id_by_code(self, customer_code):
        """Lấy ID khách hàng từ mã khách hàng"""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            print(f"🔍 Debug - Tìm ID cho mã KH: {customer_code}")  
            query = "SELECT id FROM Customers WHERE customer_code = ?"
            cursor.execute(query, (customer_code,))
            result = cursor.fetchone()
            print(f"🛠 Debug - Kết quả ID khách hàng: {result}")  

            return result[0] if result else None  # ✅ Lấy giá trị thực tế, không trả về tuple
        except sqlite3.Error as e:
            print(f"❌ Lỗi lấy ID khách hàng: {e}")
            return None
        finally:
            conn.close()



    def get_employee_id_by_name(self, employee_name):
        """Lấy ID của nhân viên từ tên"""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM Employees WHERE full_name = ?", (employee_name,))
            result = cursor.fetchone()
        
            if result:
                return result[0]  # Trả về ID của nhân viên
            else:
                return None  # Không tìm thấy nhân viên
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy ID nhân viên: {e}")
            return None
        finally:
            conn.close()

    def add_order(self, customer_code, employee_name, total_amount, status, payment, note):
        """Thêm đơn hàng mới với customer_code và employee_name"""
        print(f"🔍 Debug - Mã khách hàng nhận được: {customer_code}")  

    # Lấy ID khách hàng
        customer_id = self.get_customer_id_by_code(customer_code)
        print(f"🛠 Debug - ID khách hàng: {customer_id}")  # Thêm dòng debug

        if customer_id is None:
            print("❌ Lỗi: Không tìm thấy khách hàng với mã này! Vui lòng kiểm tra lại.")
            return False

    # Lấy ID nhân viên từ tên
        employee_id = self.get_employee_id_by_name(employee_name)
        print(f"🛠 Debug - ID nhân viên: {employee_id}")  # Thêm dòng debug

        if employee_id is None:
            print("❌ Lỗi: Không tìm thấy nhân viên với tên này! Vui lòng kiểm tra lại.")
            return False

        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            cursor.execute("""
        INSERT INTO Orders (customer_id, employee_id, total_amount, status, payment, note)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (customer_id, employee_id, total_amount, status, payment, note))

            conn.commit()
            print("✅ Thêm đơn hàng thành công!")
            return True
        except sqlite3.Error as e:
            print("❌ Lỗi khi thêm đơn hàng:", e)
            return False
        finally:
            conn.close()

    def update_order_total(self, order_id):
        """Cập nhật tổng tiền đơn hàng dựa trên tổng giá từ OrdersDetails"""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()

        # 🔹 Lấy tổng tiền từ bảng OrdersDetails
            cursor.execute("""
                SELECT COALESCE(SUM(quantity * unit_price), 0) FROM OrdersDetails WHERE order_id = ?
        """, (order_id,))
            total_price = cursor.fetchone()[0]

        # 🔄 Cập nhật tổng tiền vào bảng Orders
            cursor.execute("""
            UPDATE Orders SET total_amount = ? WHERE id = ?
        """, (total_price, order_id))
        
            conn.commit()
            print(f"✅ Tổng tiền của đơn hàng {order_id} đã được cập nhật: {total_price}")
            return True

        except sqlite3.Error as e:
            print(f"❌ Lỗi khi cập nhật tổng tiền: {e}")
        finally:
            conn.close()

        return False

    def get_last_inserted_order_code(self):
        """Lấy mã đơn hàng vừa được thêm vào"""
        conn = self.connect()  # Mở kết nối đến CSDL
        if conn is None:
            return None  # Trả về None nếu không kết nối được

        try:
            cursor = conn.cursor()
            query = "SELECT order_code FROM Orders ORDER BY id DESC LIMIT 1"
            cursor.execute(query)
            result = cursor.fetchone()
            return result[0] if result else None  # Nếu có kết quả, trả về mã đơn hàng
        except sqlite3.Error as e:
            print(f"❌ Lỗi lấy mã đơn hàng: {e}")
            return None
        finally:
            conn.close()  # Đóng kết nối


    def get_order_id_by_code(self, order_code):
        """Lấy id của đơn hàng dựa trên order_code"""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            query = "SELECT id FROM Orders WHERE order_code = ?"
            cursor.execute(query, (order_code,))
            result = cursor.fetchone()
            return result[0] if result else None
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy id đơn hàng từ order_code: {e}")
            return None
        finally:
            conn.close()
    
    def get_product_id_by_name(self, product_name):
        """Lấy ID sản phẩm từ tên sản phẩm"""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            query = "SELECT id FROM Products WHERE product_name = ?"
            cursor.execute(query, (product_name,))
            result = cursor.fetchone()
            return result[0] if result else None  # Trả về ID nếu có, nếu không thì None
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy ID sản phẩm từ tên: {e}")
            return None
        finally:
            conn.close()

    def get_product_list(self):
        """Lấy danh sách sản phẩm từ CSDL"""
        conn = self.connect()
        if conn is None:
            return []

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, product_name FROM Products")
            products = cursor.fetchall()  # Lấy tất cả sản phẩm
            return products  # Danh sách tuple (product_code, product_name)
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy danh sách sản phẩm: {e}")
            return []
        finally:
            conn.close()


    def add_order_detail(self, order_code, product_name, quantity, unit_price, note):
        """Thêm chi tiết đơn hàng vào bảng OrdersDetails với order_code và tên sản phẩm từ giao diện"""
    
    # 🔄 Chuyển đổi order_code thành order_id
        order_id = self.get_order_id_by_code(order_code)
        if order_id is None:
            print(f"❌ Không tìm thấy ID đơn hàng cho order_code: {order_code}")
            return False
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()

        # 🛒 Thêm chi tiết đơn hàng vào bảng OrdersDetails
            cursor.execute("""
            INSERT INTO OrdersDetails (order_id, product_id, quantity, unit_price, note)
            VALUES (?, ?, ?, ?, ?)
        """, (order_id, product_name, quantity, unit_price, note))

        # 🔄 Cập nhật tổng tiền đơn hàng sau khi thêm sản phẩm
            self.update_order_total(order_id)

            conn.commit()
            print(f"✅ Thêm sản phẩm '{product_name}' vào đơn hàng {order_code} thành công!")
            return True
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi thêm chi tiết đơn hàng: {e}")
            return False
        finally:
            conn.close()



    def update_order(self, order_code, customer_code, employee_name, total_amount, status, payment, note):
        """Cập nhật đơn hàng trong CSDL"""
        customer_id = self.get_customer_id_by_code(customer_code)
        print(f"🛠 Debug - ID khách hàng: {customer_id}")  # Thêm dòng debug

        # Lấy ID nhân viên từ tên
        employee_id = self.get_employee_id_by_name(employee_name)
        print(f"🛠 Debug - ID nhân viên: {employee_id}")  # Thêm dòng debug

        if employee_id is None:
            print("❌ Lỗi: Không tìm thấy nhân viên với tên này! Vui lòng kiểm tra lại.")
            return False
        
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            
            # Cập nhật đơn hàng
            query = """
                UPDATE Orders 
                SET customer_id = ?, employee_id = ?, total_amount = ?, status = ?, payment = ?, note = ?
                WHERE order_code = ?
            """
            cursor.execute(query, (customer_id, employee_id, total_amount, status, payment, note, order_code))
            conn.commit()  # Lưu thay đổi
            
            return cursor.rowcount > 0  # Trả về True nếu có bản ghi được cập nhật
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi cập nhật đơn hàng: {e}")
            return False
        finally:
            conn.close()  # Đóng kết nối




    def get_order_by_code(self, order_code):
        """Lấy dữ liệu đơn hàng theo mã đơn hàng"""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            query = """
            SELECT c.customer_code, e.full_name, o.total_amount, 
                   o.status, o.payment, o.note
            FROM Orders o
            JOIN Customers c ON o.customer_id = c.id
            JOIN Employees e ON o.employee_id = e.id
            WHERE o.order_code = ?
        """
            cursor.execute(query, (order_code,))
            row = cursor.fetchone()

            if row:
                return {
                "customer_code": row[0],   # Mã khách hàng
                "employee_name": row[1],   # Nhân viên xử lý (Đổi key để thống nhất)
                "total_amount": row[2],    # Tổng tiền
                "status": row[3],          # Trạng thái
                "payment": row[4],         # Thanh toán
                "note": row[5]             # Ghi chú
            }
            return None  # Không tìm thấy đơn hàng

        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy đơn hàng: {e}")
            return None

        finally:
            conn.close()
