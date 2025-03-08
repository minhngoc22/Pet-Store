from datetime import datetime
from PyQt6.QtWidgets import QWidget
from SQL_database.ketnoiSQL import Database

class Home(QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.db = Database()  # 🔥 Khởi tạo database

        # Cập nhật dữ liệu khi mở giao diện
        self.update_dashboard()
        self.ui.btn_refreshHome.clicked.connect(self.update_dashboard)  # ✅ Sửa lỗi chính tả

    def update_dashboard(self):
        """Lấy dữ liệu từ CSDL và hiển thị lên giao diện"""
        today_date = datetime.now().strftime("%Y-%m-%d")

        conn = self.db.connect()  # ✅ Mở kết nối
        cursor = conn.cursor()

        try:
            # 1️⃣ **Tính số hóa đơn trong ngày**
            cursor.execute("SELECT COUNT(*) FROM Orders WHERE DATE(order_date) = ?", (today_date,))
            order_count = cursor.fetchone()[0] or 0

            # 2️⃣ **Tính tổng doanh thu trong ngày**
            cursor.execute("SELECT SUM(total_amount) FROM Orders WHERE DATE(order_date) = ? AND status = 'Hoàn thành'", 
                        (today_date,))
            revenue = cursor.fetchone()[0] or 0  

            # 3️⃣ **Tính số sản phẩm bán trong ngày**
            cursor.execute("""
                SELECT SUM(od.quantity) FROM OrdersDetails od
                JOIN Orders o ON od.order_id = o.id
                WHERE DATE(o.order_date) = ? AND o.status = 'Hoàn thành'
            """, (today_date,))
            product_count = cursor.fetchone()[0] or 0
        finally:
            conn.close()  # ✅ Đảm bảo đóng kết nối

        # Cập nhật dữ liệu lên QLabel với định dạng số rõ ràng hơn
        self.ui.lbl_dh.setText(f"{order_count:,} HD")
        self.ui.lbl_dt.setText(f"{revenue:,.0f} VNĐ")
        self.ui.lbl_sp.setText(f"{product_count:,} SP")
