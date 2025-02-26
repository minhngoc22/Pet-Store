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
        self.ui.btn_themncc.clicked.connect(self.add_supplier)
        self.ui.btn_suancc.clicked.connect(self.show_update_supplier)
        self.ui.btn_xoancc.clicked.connect(self.delete_supplier)

        # Nạp dữ liệu ban đầu
        self.load_addresses()

    def load_and_update_table(self, suppliers=None):
        """Tải và cập nhật bảng nhà cung cấp"""
        if suppliers is None:
            _, suppliers = self.db.get_all_suppliers()
            print(f"⚡ Debug - Số nhà cung cấp sau khi tải lại: {len(suppliers)}")

        self.model.clear()

        # ✅ Cập nhật danh sách cột để khớp với CSDL
        column_names = ["Mã NCC", "Tên Nhà Cung Cấp", "SĐT", "Email", "Địa Chỉ", "Ghi chú"]
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

    def add_supplier(self):
        """Thêm nhà cung cấp mới"""
        # Hiển thị giao diện thêm nhà cung cấp""
        from NhaCungCap.themNCC import EventHandler
        self.themkh_window = EventHandler()
        self.themkh_window.show()
    
    def show_update_supplier(self):
        """Mở cửa sổ cập nhật nhà cung cấp"""
        selected_indexes = self.ui.tb_nhaccap.selectionModel().selectedRows()
        if not selected_indexes:
            QMessageBox.warning(None, "Chú ý", "Vui lòng chọn một nhà cung cấp để cập nhật.")
            return

        selected_row = selected_indexes[0].row()
        model = self.ui.tb_nhaccap.model()
        supplier_code = model.item(selected_row, 0).text()  # Cột 0 chứa mã nhà cung cấp

        from NhaCungCap.updateNCC import UpdateSupplier  # Import cửa sổ cập nhật nhà cung cấp
        self.sua_ncc_window = UpdateSupplier(supplier_code, self.db)
        self.sua_ncc_window.show()
        self.load_and_update_table()  # Cập nhật bảng sau khi đóng cửa sổ

    def delete_supplier(self):
        """Xóa nhà cung cấp được chọn khỏi CSDL bằng Mã NCC"""
        selected_indexes = self.ui.tb_nhaccap.selectionModel().selectedRows()
        if not selected_indexes:
            QMessageBox.warning(None, "Chú ý", "Vui lòng chọn một nhà cung cấp để xóa.")
            return

        selected_row = selected_indexes[0].row()
        supplier_code = self.model.item(selected_row, 0).text().strip()  # Lấy Mã NCC từ cột đầu tiên

        reply = QMessageBox.question(
        None, "Xác nhận", f"Bạn có chắc chắn muốn xóa nhà cung cấp có Mã NCC: {supplier_code}?",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        QMessageBox.StandardButton.No
    )

        if reply == QMessageBox.StandardButton.Yes:
            if self.db.delete_supplier(supplier_code):  # Gọi hàm xóa nhà cung cấp trong CSDL
                QMessageBox.information(None, "Thành công", "Nhà cung cấp đã được xóa.")
                self.load_and_update_table()  # Cập nhật bảng sau khi xóa
            else:
                QMessageBox.critical(None, "Lỗi", "Xóa nhà cung cấp thất bại! Có thể Mã NCC không tồn tại.")

