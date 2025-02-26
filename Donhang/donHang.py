import sys
import os
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt
from SQL_database.csdl_DH import OrderDatabase # File quản lý đơn hàng

class Donhang:
    def __init__(self, ui):
        self.ui = ui
        self.model = QStandardItemModel()
        self.ui.tb_donhang.setModel(self.model)
        
        # Kết nối CSDL
        self.db = OrderDatabase()
        if not self.db.connect():
            QMessageBox.critical(self.ui, "Lỗi", "Không thể kết nối CSDL đơn hàng!")
            return

        # Gán sự kiện cho các nút
        self.ui.btn_refreshdh.clicked.connect(self.refresh_data)
        self.ui.btn_themdh.clicked.connect(self.show_them_donhang)
        #self.ui.btn_timkiemdh.clicked.connect(self.search_order)
        self.ui.cbo_trangthai.currentIndexChanged.connect(self.filter_by_status)
        
        # Nạp danh sách trạng thái
        self.load_statuses()

    def load_and_update_table(self, orders=None):
        """Tải và cập nhật bảng đơn hàng"""
        if orders is None:
            _, orders = self.db.get_all_orders()

            print(f"⚡ Debug - Số đơn hàng sau khi tải lại: {len(orders)}")  # Debug

        self.model.clear()
    
        # ✅ Cập nhật danh sách cột để khớp với CSDL
        column_names = [ "Mã ĐH", "Mã Khách hàng","Tên KH", "Tổng Tiền", "Ngày Đặt", "Trạng Thái", "Thanh Toán","Ghi chú"]
        self.model.setColumnCount(len(column_names))  # ✅ Đặt số cột chính xác
        self.model.setHorizontalHeaderLabels(column_names)

        for row_idx, row_data in enumerate(orders):
            for col_idx, value in enumerate(row_data):
                item = QStandardItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.model.setItem(row_idx, col_idx, item)

        self.ui.tb_donhang.setModel(self.model)
        self.ui.tb_donhang.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    def load_statuses(self):
        """Tải danh sách trạng thái đơn hàng vào ComboBox"""
        statuses = self.db.get_statuses()
        self.ui.cbo_trangthai.clear()
        self.ui.cbo_trangthai.addItem("Tất cả")
        for status in statuses:
            self.ui.cbo_trangthai.addItem(status)
    
    def filter_by_status(self):
        """Lọc đơn hàng theo trạng thái"""
        selected_status = self.ui.cbo_trangthai.currentText()
        print(f"⚡ Debug - Trạng thái được chọn: {selected_status}")  # Debug
        orders = self.db.get_order_by_status(selected_status)
        print(f"⚡ Debug - Số đơn hàng tìm thấy: {len(orders)}")  # Debug
        self.load_and_update_table(orders)
    
   
    
    def refresh_data(self):
        """Làm mới bảng đơn hàng theo trạng thái đang chọn"""
        
        self.load_and_update_table()
        self.load_statuses()

    def show_them_donhang(self):
        """Hiển thị giao diện thêm đơn hàng"""
        from Donhang.themDH import ThemDonHang
        self.them_dh = ThemDonHang()
        self.them_dh.show()
       
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Donhang()
    window.ui.show()
    sys.exit(app.exec())
    

       