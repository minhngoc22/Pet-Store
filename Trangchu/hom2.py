from datetime import datetime
from PyQt6.QtWidgets import QWidget
from SQL_database.ketnoiSQL import Database

class Home2(QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.db = Database()  # 🔥 Khởi tạo database

        # Cập nhật dữ liệu khi mở giao diện
        self.update_dashboard()
        self.ui.btn_refreshHome.clicked.connect(self.update_dashboard)  # ✅ Sửa lỗi chính tả

    def update_dashboard(self):
        """Lấy dữ liệu trong tháng từ CSDL và hiển thị lên giao diện"""
        today_date = datetime.now().strftime("%Y-%m-%d")
        first_day_of_month = datetime.now().strftime("%Y-%m-01")  # Ngày đầu tháng

        conn = self.db.connect()  # ✅ Mở kết nối
        cursor = conn.cursor()

        try:
            # 1️⃣ **Tính số hóa đơn trong tháng**
            cursor.execute("SELECT COUNT(*) FROM Orders WHERE order_date BETWEEN ? AND ?", 
                           (first_day_of_month, today_date))
            order_count = cursor.fetchone()[0] or 0

            

            # 3️⃣ **Tính số sản phẩm bán trong tháng**
            cursor.execute("""
                SELECT SUM(od.quantity) FROM OrdersDetails od
                JOIN Orders o ON od.order_id = o.id
                WHERE o.order_date BETWEEN ? AND ? AND o.status = 'Hoàn thành'
            """, (first_day_of_month, today_date))
            product_count = cursor.fetchone()[0] or 0
        finally:
            conn.close()  # ✅ Đảm bảo đóng kết nối

        # Cập nhật dữ liệu lên QLabel với định dạng số rõ ràng hơn
        self.ui.lbl_dh.setText(f"{order_count:,} HD")  # 🔄 Số hóa đơn trong tháng
       
        self.ui.lbl_sp.setText(f"{product_count:,} SP")  # 🔄 Số sản phẩm bán ra trong tháng
