from SQL_database.ketnoiSQL import Database  
import sqlite3

class CTDHDatabase(Database):
    def get_order_by_code(self, order_code):
        """Lấy dữ liệu đơn hàng theo mã đơn hàng"""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            query = """
        SELECT o.order_code, c.customer_code, c.full_name,p.product_name, od.quantity, 
               o.total_amount, o.status, o.payment, o.note
       FROM Orders o
            JOIN Customers c ON o.customer_id = c.id
            JOIN OrdersDetails od ON o.id = od.order_id
            JOIN Products p ON od.product_id = p.id
            WHERE o.order_code = ?
        """
            cursor.execute(query, (order_code,))
            rows = cursor.fetchall()

            if rows:
                return [  # Trả về danh sách các sản phẩm
                    {
                        "Mã ĐH": row[0],
                        "Mã KH": row[1],
                        "Tên KH": row[2],
                        "Sản Phẩm": row[3],
                        "Số Lượng": row[4],
                        "Tổng Tiền": row[5],
                        "Trạng Thái": row[6],
                        "Thanh Toán": row[7],
                        "Ghi chú": row[8]
                    }
                    for row in rows
                ]
            return None  # Không có dữ liệu

        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy đơn hàng: {e}")
            return None

        finally:
            conn.close()

