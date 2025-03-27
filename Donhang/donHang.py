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
        self.ui.btn_suadh.clicked.connect(self.edit_order)
        self.ui.cbo_trangthai.currentIndexChanged.connect(self.filter_by_status)
        self.ui.btn_xemCT.clicked.connect(self.xemCT)
        
        # Nạp danh sách trạng thái
        self.load_statuses()


    def load_and_update_table(self):
        """Tải và cập nhật bảng đơn hàng"""

        orders = self.db.get_all()
        print(f"Đơn hàng lấy từ CSDL: {orders}")  # Kiểm tra dữ liệu lấy từ cơ sở dữ liệu


        print(f"⚡ Debug - Số đơn hàng sau khi tải lại: {len(orders)}")  # Debug

        self.model.clear()

    # Cập nhật danh sách cột để khớp với CSDL
        column_names = ["Mã ĐH", "Mã Khách hàng", "Tổng Tiền", "Ngày Đặt", "Trạng Thái", "Thanh Toán", "Ghi chú"]
        self.model.setColumnCount(len(column_names))  # Đặt số cột chính xác
        self.model.setHorizontalHeaderLabels(column_names)

        for row_idx, row_data in enumerate(orders):
            for col_idx, value in enumerate(row_data):
                item = QStandardItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Căn giữa nội dung
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
    
        if selected_status == "Tất cả":
            orders = self.db.get_all()
        else:
            orders = self.db.get_order_by_status(selected_status)

        print(f"⚡ Debug - Số đơn hàng tìm thấy: {len(orders)}")  # Debug
        self.update_table(orders)  # Cập nhật bảng với dữ liệu đã lọc
    
   
    def update_table(self, orders):
        """Cập nhật bảng đơn hàng với dữ liệu truyền vào"""
        self.model.removeRows(0, self.model.rowCount())  # Chỉ xóa dữ liệu, giữ tiêu đề

        column_names = ["Mã ĐH", "Mã Khách hàng", "Tổng Tiền", "Ngày Đặt", "Trạng Thái", "Thanh Toán", "Ghi chú"]
        self.model.setColumnCount(len(column_names))  
        self.model.setHorizontalHeaderLabels(column_names)

        for row_idx, row_data in enumerate(orders):
            for col_idx, value in enumerate(row_data):
                item = QStandardItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  
                self.model.setItem(row_idx, col_idx, item)

        self.ui.tb_donhang.setModel(self.model)
        self.ui.tb_donhang.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    def refresh_data(self):
        """Làm mới bảng đơn hàng theo trạng thái đang chọn"""
        
        self.load_and_update_table()
        self.load_statuses()

    def show_them_donhang(self):
        """Hiển thị giao diện thêm đơn hàng"""
        from Donhang.themDH import ThemDonHang
        self.them_dh = ThemDonHang()
        self.them_dh.show()

    def edit_order(self):
        """Sửa thông tin đơn hàng được chọn"""
        selected_indexes = self.ui.tb_donhang.selectionModel().selectedRows()

        if not selected_indexes:
            QMessageBox.warning(None, "Chú ý", "Vui lòng chọn một đơn hàng để sửa.")
            return

    # Lấy ID của đơn hàng từ dòng được chọn
        selected_row = selected_indexes[0].row()
        model = self.ui.tb_donhang.model()
        order_id = model.item(selected_row, 0).text()  # Cột 0 chứa ID đơn hàng

    # 🔹 Kiểm tra trạng thái đơn hàng trước khi mở form cập nhật
        current_status = self.db.get_order_status(order_id)
        if current_status in ["Đã hủy"]:
            QMessageBox.warning(None, "Thông báo", "Không thể sửa đơn hàng đã bị hủy!")
            return  # Không mở form
        if current_status in ["Hoàn thành"]:
            QMessageBox.warning(None, "Thông báo", "Không thể sửa đơn hàng đã hoàn thành!")
            return


        from Donhang.updateDH import UpdateDonHang  # Import cửa sổ sửa đơn hàng
        self.sua_dh_window = UpdateDonHang(order_id)
        self.sua_dh_window.show()

    # Kết nối sự kiện khi cửa sổ đóng thì cập nhật lại bảng
        self.sua_dh_window.destroyed.connect(self.refresh_data)



    def xemCT(self):
        """Mở giao diện xem chi tiết đơn hàng"""
        selected_indexes = self.ui.tb_donhang.selectionModel().selectedRows()

        if not selected_indexes:
            QMessageBox.warning(None, "Chú ý", "Vui lòng chọn một đơn hàng để xem chi tiết.")
            return

    # Lấy ID đơn hàng từ dòng được chọn
        selected_row = selected_indexes[0].row()
        model = self.ui.tb_donhang.model()
        order_id = model.item(selected_row, 0).text()  # Cột 0 là Mã ĐH

        from Donhang.themCT import ThemChiTiet  # Import cửa sổ xem chi tiết đơn hàng
        self.chitiet_window = ThemChiTiet(order_id)  # Chỉ xem, không cho thêm
        self.chitiet_window.show()


        
   

        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Donhang()
    window.ui.show()
    sys.exit(app.exec())
    

       