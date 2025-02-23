import sys
import os
from PyQt6.QtGui import QIcon, QPixmap, QStandardItemModel, QStandardItem
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt
from SQL_database.csdl_nhaCC import SupplierDatabase  # File quản lý nhà cung cấp

class NhaCungCap:
    def __init__(self, ui):
        self.ui = ui
        self.model = QStandardItemModel()
        self.ui.tb_nhaccap.setModel(self.model)

        # Kết nối CSDL
        self.db = SupplierDatabase()

        # Gán sự kiện cho các nút
        self.ui.btn_refreshncc.clicked.connect(self.refresh_data)
        self.ui.btn_timkiemncc.clicked.connect(self.search_supplier)
        self.ui.cbo_diachi.currentIndexChanged.connect(self.filter_by_address)

        # Nạp dữ liệu ban đầu
        self.load_addresses()

    def load_and_update_table(self, suppliers=None):
        """Tải và cập nhật bảng nhà cung cấp"""
        if suppliers is None:
            _, suppliers = self.db.get_all_suppliers()
            print(f"⚡ Debug - Số nhà cung cấp sau khi tải lại: {len(suppliers)}")

        self.model.clear()

        # ✅ Cập nhật danh sách cột để khớp với CSDL
        column_names = ["Mã NCC", "Tên Nhà Cung Cấp", "SĐT", "Email", "Địa Chỉ"]
        self.model.setColumnCount(len(column_names))
        self.model.setHorizontalHeaderLabels(column_names)

        for row_idx, row_data in enumerate(suppliers):
            for col_idx, value in enumerate(row_data):
                item = QStandardItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.model.setItem(row_idx, col_idx, item)

        # Cập nhật giao diện bảng
        self.ui.tb_nhaccap.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    def load_addresses(self):
        """Tải danh sách địa chỉ vào ComboBox"""
        addresses = self.db.get_addresses()
        self.ui.cbo_diachi.clear()
        self.ui.cbo_diachi.addItem("Tất cả")
        for addr in addresses:
            self.ui.cbo_diachi.addItem(addr)
        
        print(f"⚡ Debug - Danh sách địa chỉ tải về: {addresses}")

    def filter_by_address(self):
        """Lọc nhà cung cấp theo địa chỉ"""
        selected_address = self.ui.cbo_diachi.currentText()
        print(f"⚡ Debug - Địa chỉ được chọn: {selected_address}")

        suppliers = self.db.get_suppliers_by_address(selected_address)
        print(f"⚡ Debug - Số nhà cung cấp tìm thấy: {len(suppliers)}")

        self.load_and_update_table(suppliers)

    def search_supplier(self):
        """Tìm kiếm nhà cung cấp theo tên"""
        search_text = self.ui.txt_timkiemncc.toPlainText().strip()  # Đổi từ toPlainText() thành text()
        if not search_text:
            self.refresh_data()
            return

        suppliers = self.db.search_supplier_by_name(search_text)
        print(f"⚡ Debug - Số nhà cung cấp tìm thấy khi tìm kiếm: {len(suppliers)}")
        self.load_and_update_table(suppliers)

    def refresh_data(self):
        """Làm mới danh sách nhà cung cấp"""
        self.load_addresses()
        self.load_and_update_table()
