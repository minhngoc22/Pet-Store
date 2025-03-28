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
    def get_payment_methods(self):
        """Lấy danh sách phương thức thanh toán từ CSDL"""
        conn = self.connect()
        if conn is None:
            return []

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT DISTINCT payment FROM Orders")  # Truy vấn lấy phương thức thanh toán
            payments = [row[0] for row in cursor.fetchall()]
            print("Danh sách phương thức thanh toán từ CSDL:", payments)  # Debug
            return payments
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy danh sách phương thức thanh toán: {e}")
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



    def update_order(self, order_code, employee_name, total_amount, status, payment, note):
        """Cập nhật đơn hàng trong CSDL"""
       

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
                SET  employee_id = ?, total_amount = ?, status = ?, payment = ?, note = ?
                WHERE order_code = ?
            """
            cursor.execute(query, ( employee_id, total_amount, status, payment, note, order_code))
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
            SELECT o.order_code,c.customer_code, e.full_name, o.total_amount, 
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
                    "order_code": row[0],
                    "customer_code": row[1], # Mã khách hàng
                "employee_name": row[2],   # Nhân viên xử lý (Đổi key để thống nhất)
                "total_amount": row[3],    # Tổng tiền
                "status": row[4],          # Trạng thái
                "payment": row[5],         # Thanh toán
                "note": row[6]             # Ghi chú
            }
            return None  # Không tìm thấy đơn hàng

        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy đơn hàng: {e}")
            return None

        finally:
            conn.close()

    def get_customer_id_by_phone(self, phone_number):
        """Lấy ID khách hàng từ số điện thoại"""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            query = "SELECT id FROM Customers WHERE phone = ?"
            cursor.execute(query, (phone_number,))
            result = cursor.fetchone()
            return result[0] if result else None  # Trả về ID nếu tìm thấy, nếu không thì None
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy ID khách hàng từ số điện thoại: {e}")
            return None
        finally:
            conn.close()

    def add_order(self, customer_id, employee_name, note=""):
        """Thêm đơn hàng mới chỉ với mã khách hàng và nhân viên xử lý."""
        conn = self.connect()
        if conn is None:
            return None
        try:
            # Lấy employee_id từ tên nhân viên
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM Employees WHERE full_name = ?", (employee_name,))
            employee =cursor.fetchone()

            if not employee:
                return False  # Nếu nhân viên không tồn tại

            employee_id = employee[0]

            # Chèn đơn hàng vào bảng Orders
            cursor.execute(
                "INSERT INTO Orders (customer_id, employee_id, note) VALUES (?, ?, ?)",
                (customer_id, employee_id, note)
            )
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print("Lỗi khi thêm đơn hàng:", e)
            return False
        finally:
            conn.close()

    def add_order_detail(self, order_code, product_id, quantity, unit_price, note):
        """Thêm chi tiết đơn hàng, cập nhật tổng tiền và trừ đi số lượng sản phẩm"""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()

        # 🔹 Lấy ID đơn hàng từ mã đơn hàng
            order_id = self.get_order_id_by_code(order_code)
            if not order_id:
                print(f"❌ Lỗi: Không tìm thấy đơn hàng với mã {order_code}")
                return False

        # 🔹 Kiểm tra số lượng sản phẩm còn trong kho
            cursor.execute("SELECT stock_quantity FROM Products WHERE id = ?", (product_id,))
            stock_quantity = cursor.fetchone()

            if stock_quantity is None:
                print(f"❌ Lỗi: Không tìm thấy sản phẩm với ID {product_id}")
                return False

            stock_quantity = stock_quantity[0]  # Lấy số lượng tồn kho
            if stock_quantity < quantity:
                print(f"❌ Lỗi: Không đủ hàng trong kho. Số lượng tồn kho: {stock_quantity}, cần: {quantity}")
                return False

        # 🔹 Thêm sản phẩm vào đơn hàng (OrdersDetails)
            cursor.execute("""
            INSERT INTO OrdersDetails (order_id, product_id, quantity, unit_price, note)
            VALUES (?, ?, ?, ?, ?)
        """, (order_id, product_id, quantity, unit_price, note))

        # 🔄 Trừ số lượng sản phẩm trong kho
            cursor.execute("""
            UPDATE Products
            SET stock_quantity = stock_quantity - ?
            WHERE id = ?
        """, (quantity, product_id))

        # 🔄 Cập nhật tổng tiền đơn hàng (KHÔNG cập nhật trạng thái & thanh toán)
            cursor.execute("""
            SELECT COALESCE(SUM(quantity * unit_price), 0)
            FROM OrdersDetails
            WHERE order_id = ?
        """, (order_id,))
            total_price = cursor.fetchone()[0]

            cursor.execute("""
            UPDATE Orders
            SET total_amount = ?
            WHERE id = ?
        """, (total_price, order_id))

            conn.commit()
            print(f"✅ Đã thêm sản phẩm vào đơn hàng {order_code} và cập nhật tổng tiền.")
            return True

        except sqlite3.Error as e:
            print(f"❌ Lỗi khi thêm sản phẩm vào đơn hàng: {e}")
            return False

        finally:
            conn.close()




    def get_order_details(self, order_code):
        """Lấy chi tiết đơn hàng theo order_code"""
        conn = self.connect()
        if conn is None:
            return []

        try:
            cursor = conn.cursor()

        # 🔹 Lấy order_id từ order_code
            order_id = self.get_order_id_by_code(order_code)
            if not order_id:
                print(f"❌ Lỗi: Không tìm thấy đơn hàng với mã {order_code}")
                return []

        # 🔹 Truy vấn chi tiết đơn hàng
            cursor.execute("""
        SELECT P.product_name, OD.quantity, OD.unit_price, 
               (OD.quantity * OD.unit_price) AS total_price,
               O.status, O.payment
        FROM OrdersDetails OD
        JOIN Products P ON OD.product_id = P.id
        JOIN Orders O ON OD.order_id = O.id
        WHERE O.id = ?  -- ✅ Truy vấn bằng order_id đã lấy được
        """, (order_id,))

            details = cursor.fetchall()

        # 🔹 Kiểm tra nếu không có dữ liệu
            if not details:
                print(f"⚠️ Không tìm thấy chi tiết đơn hàng cho mã {order_code}")

            return details
        except sqlite3.Error as e:
            print(f"❌ Lỗi lấy chi tiết đơn hàng: {e}")
            return []
        finally:
            conn.close()  # 🔹 Đảm bảo đóng kết nối
    def get_order_status(self, order_code):

        """Lấy trạng thái hiện tại của đơn hàng"""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT status FROM Orders WHERE order_code = ?", (order_code,))
            row = cursor.fetchone()
            return row[0] if row else None

        except sqlite3.Error as e:
            print(f"❌ Lỗi lấy trạng thái đơn hàng: {e}")
            return None

        finally:
            conn.close()

    def restore_order_products(self, order_code):   
        """Hoàn lại số lượng sản phẩm nếu đơn hàng bị hủy"""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()

        # 🔹 Lấy danh sách sản phẩm trong đơn hàng
            cursor.execute("""
            SELECT product_id, quantity FROM OrdersDetails 
            WHERE order_id = (SELECT id FROM Orders WHERE order_code = ?)
        """, (order_code,))
            products = cursor.fetchall()

        # 🔄 Cập nhật lại số lượng sản phẩm trong kho
            for product_id, quantity in products:
                cursor.execute("""
                UPDATE Products SET stock_quantity = stock_quantity + ?
                WHERE id = ?
            """, (quantity, product_id))

            conn.commit()
            print(f"✅ Hoàn lại sản phẩm cho đơn hàng {order_code}")
            return True

        except sqlite3.Error as e:
            print(f"❌ Lỗi khi hoàn lại sản phẩm: {e}")
            return False

        finally:
            conn.close()

    def get_product_by_code(self, product_code):
        """Lấy tên sản phẩm và đơn giá từ mã sản phẩm"""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            query = "SELECT product_name, price FROM Products WHERE id = ?"
            cursor.execute(query, (product_code,))
            result = cursor.fetchone()

            if result:
                return {"product_name": result[0], "price": result[1]}
            return None
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy thông tin sản phẩm: {e}")
            return None
        finally:
            conn.close()

    # ✅ Lấy thông tin nhân viên đang đăng nhập
    def get_logged_in_employee(self, username):  
        """Lấy thông tin nhân viên đang đăng nhập từ bảng Users"""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            query = """
                SELECT e.full_name, e.phone, e.position
                FROM Employees e
                JOIN Users u ON e.id = u.id
                WHERE u.username = ? LIMIT 1
            """
            cursor.execute(query, (username,))
            employee = cursor.fetchone()

            if employee:
                return {
                    "full_name": employee[0],
                    "phone": employee[1],
                    "position": employee[2]
                }
            return None
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy thông tin nhân viên đăng nhập: {e}")
            return None
        finally:
            conn.close()