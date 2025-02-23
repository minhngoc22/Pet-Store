import sys
import os
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt
from SQL_database.csdl_KH import CustomerDatabase  # File quản lý khách hàng


class KhachHang:
    def __init__(self, ui):
        self.ui = ui
        self.model = QStandardItemModel()
        self.ui.tb_khachhang.setModel(self.model)
        
        # Kết nối CSDL
        self.db = CustomerDatabase()
        if not self.db.connect():
            QMessageBox.critical(self.ui, "Lỗi", "Không thể kết nối CSDL khách hàng!")
            return

        # Gán sự kiện cho các nút
        self.ui.btn_refreshKH.clicked.connect(self.refresh_data)
        self.ui.btn_themkh.clicked.connect(self.show_themkh)
        self.ui.btn_xoakh.clicked.connect(self.delete_customer)
        self.ui.btn_timkiemkh.clicked.connect(self.search_customer)
        self.ui.btn_suakh.clicked.connect(self.show_update_customer)
        self.ui.cbo_kh.currentIndexChanged.connect(self.filter_by_address)
        
       
        # Nạp danh sách địa chỉ
        self.load_addresses()
    
    def load_and_update_table(self, customers=None):
        """Tải và cập nhật bảng khách hàng"""
        if customers is None:
            _, customers = self.db.get_all_customers()
            print(f"⚡ Debug - Số khách hàng sau khi tải lại: {len(customers)}")  # Debug

        self.model.clear()
    
        # ✅ Cập nhật danh sách cột để khớp với CSDL
        column_names = ["Mã KH", "Tên Khách Hàng", "SĐT", "Email", "Địa Chỉ"]
        self.model.setColumnCount(len(column_names))  # ✅ Đặt số cột chính xác
        self.model.setHorizontalHeaderLabels(column_names)

        for row_idx, row_data in enumerate(customers):
            for col_idx, value in enumerate(row_data):
                item = QStandardItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.model.setItem(row_idx, col_idx, item)

        self.ui.tb_khachhang.setModel(self.model)
        self.ui.tb_khachhang.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    
    def load_addresses(self):
        """Tải danh sách địa chỉ vào ComboBox"""
        addresses = self.db.get_addresses()
        self.ui.cbo_kh.clear()
        self.ui.cbo_kh.addItem("Tất cả")
        for addr in addresses:
            self.ui.cbo_kh.addItem(addr)
    
    def filter_by_address(self):
        """Lọc khách hàng theo địa chỉ"""
        selected_address = self.ui.cbo_kh.currentText()
        print(f"⚡ Debug - Địa chỉ được chọn: {selected_address}")  # Debug
        customers = self.db.get_customers_by_address(selected_address)
        print(f"⚡ Debug - Số khách hàng tìm thấy: {len(customers)}")  # Debug
        self.load_and_update_table(customers)
    
    def delete_customer(self):
        """Xóa khách hàng được chọn khỏi CSDL bằng Mã KH"""
        selected_indexes = self.ui.tb_khachhang.selectionModel().selectedRows()
        if not selected_indexes:
            QMessageBox.warning(None, "Chú ý", "Vui lòng chọn một khách hàng để xóa.")
            return

        selected_row = selected_indexes[0].row()
        customer_code = self.model.item(selected_row, 0).text().strip()  # Lấy Mã KH từ cột đầu tiên

        reply = QMessageBox.question(
            None, "Xác nhận", f"Bạn có chắc chắn muốn xóa khách hàng có Mã KH: {customer_code}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            if self.db.delete_customer(customer_code):  # Gọi hàm xóa trong CSDL
                QMessageBox.information(None, "Thành công", "Khách hàng đã được xóa.")
                self.load_and_update_table()
            else:
                QMessageBox.critical(None, "Lỗi", "Xóa khách hàng thất bại! Có thể Mã KH không tồn tại.")

    
    def search_customer(self):
        """Tìm kiếm khách hàng theo tên"""
        search_text = self.ui.txt_timkiemkh.toPlainText().strip()
        if not search_text:
            self.load_and_update_table()
            return
        
        customers = self.db.get_customer_by_phone_or_email(search_text)
        self.load_and_update_table(customers)
    
    def refresh_data(self):
        self.load_and_update_table()
        self.load_addresses()
    
    def show_themkh(self):
        """Mở cửa sổ thêm khách hàng"""
        from KhachHang.themKH import EventHandler
        self.themkh_window = EventHandler()
        self.themkh_window.show()

    def show_update_customer(self):
        """Mở cửa sổ cập nhật khách hàng"""
        selected_indexes = self.ui.tb_khachhang.selectionModel().selectedRows()
        if not selected_indexes:
            QMessageBox.warning(None, "Chú ý", "Vui lòng chọn một khách hàng để cập nhật.")
            return
        selected_row = selected_indexes[0].row()
        model = self.ui.tb_khachhang.model()
        customer_id = model.item(selected_row, 0).text()  # Cột 0 chứa ID khách hàng

        from KhachHang.updateKH import UpdateCustomer
        self.sua_kh_window = UpdateCustomer(customer_id, self.db)
        self.sua_kh_window.show()
        self.load_and_update_table()  # Cập nhật bảng sau khi đóng cửa sổ'''
