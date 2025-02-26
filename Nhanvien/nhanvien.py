import sys
import os
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt
from SQL_database.csdl_NV import EmployeeDatabase  # File quản lý nhân viên

class Nhanvien:
    def __init__(self, ui):
        self.ui = ui
        self.model = QStandardItemModel()
        self.ui.tb_nhanvien.setModel(self.model)
        
        # Kết nối CSDL
        self.db = EmployeeDatabase()
        if not self.db.connect():
            QMessageBox.critical(self.ui, "Lỗi", "Không thể kết nối CSDL nhân viên!")
            return

        # Gán sự kiện cho các nút
        self.ui.btn_refreshnv.clicked.connect(self.refresh_data)
        self.ui.btn_themnv.clicked.connect(self.show_themnv)
        self.ui.btn_xoanv.clicked.connect(self.delete_employee)
        self.ui.btn_timkiemnv.clicked.connect(self.search_employee)
        self.ui.btn_suanv.clicked.connect(self.show_update_employee)
        self.ui.cbo_nv.currentIndexChanged.connect(self.filter_by_position)
        
        # Nạp danh sách vị trí
        self.load_positions()
    
    def load_and_update_table(self, employees=None):
        """Tải và cập nhật bảng nhân viên"""
        if employees is None:
            _, employees = self.db.get_all_employees()

            print(f"⚡ Debug - Số nhân viên sau khi tải lại: {len(employees)}")  # Debug

        self.model.clear()
    
    # ✅ Cập nhật danh sách cột để khớp với CSDL
        column_names = [ "Mã NV", "Tên Nhân Viên", "SĐT", "Email", "Địa Chỉ", "Lương", "Vị trí","Ghi chú"]
        self.model.setColumnCount(len(column_names))  # ✅ Đặt số cột chính xác
        self.model.setHorizontalHeaderLabels(column_names)

        for row_idx, row_data in enumerate(employees):
            for col_idx, value in enumerate(row_data):
                item = QStandardItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.model.setItem(row_idx, col_idx, item)

        self.ui.tb_nhanvien.setModel(self.model)
        self.ui.tb_nhanvien.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    
    def load_positions(self):
        """Tải danh sách vị trí vào ComboBox"""
        positions = self.db.get_positions()
        self.ui.cbo_nv.clear()
        self.ui.cbo_nv.addItem("Tất cả")
        for pos in positions:
            self.ui.cbo_nv.addItem(pos)
    
    def filter_by_position(self):
        """Lọc nhân viên theo vị trí"""
        selected_position = self.ui.cbo_nv.currentText()
        print(f"⚡ Debug - Vị trí được chọn: {selected_position}")  # Debug
        employees = self.db.get_employees_by_position(selected_position)
        print(f"⚡ Debug - Số nhân viên tìm thấy: {len(employees)}")  # Debug
        self.load_and_update_table(employees)
    
    def delete_employee(self):
        """Xóa nhân viên được chọn khỏi CSDL bằng Mã NV"""
        selected_indexes = self.ui.tb_nhanvien.selectionModel().selectedRows()
        if not selected_indexes:
            QMessageBox.warning(None, "Chú ý", "Vui lòng chọn một nhân viên để xóa.")
            return

        selected_row = selected_indexes[0].row()
        employee_code = self.model.item(selected_row, 0).text().strip()  # Lấy Mã NV từ cột đầu tiên

        reply = QMessageBox.question(
            None, "Xác nhận", f"Bạn có chắc chắn muốn xóa nhân viên có Mã NV: {employee_code}?",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        QMessageBox.StandardButton.No
    )

        if reply == QMessageBox.StandardButton.Yes:
            if self.db.delete_employee(employee_code):  # Gọi hàm xóa trong CSDL
                QMessageBox.information(None, "Thành công", "Nhân viên đã được xóa.")
                self.load_and_update_table()
            else:
             QMessageBox.critical(None, "Lỗi", "Xóa nhân viên thất bại! Có thể Mã NV không tồn tại.")



    
    def search_employee(self):
        """Tìm kiếm nhân viên theo tên"""
        search_text = self.ui.txt_timkiemnv.toPlainText().strip()
        if not search_text:
            self.load_and_update_table()
            return
        
        employees = self.db.search_employee_by_name(search_text)
        self.load_and_update_table(employees)
    
    def refresh_data(self):
        self.load_and_update_table()
        self.load_positions()
    
    def show_themnv(self):
        """Mở cửa sổ thêm nhân viên"""
        from Nhanvien.themNV import EventHandler
        self.themnv_window = EventHandler()
        self.themnv_window.show()

    def show_update_employee(self):
       
        selected_indexes = self.ui.tb_nhanvien.selectionModel().selectedRows()
        if not selected_indexes:
            QMessageBox.warning(None, "Chú ý", "Vui lòng chọn một nhân viên để cập nhật.")
            return
        selected_row = selected_indexes[0].row()
        model = self.ui.tb_nhanvien.model()
        employee_id = model.item(selected_row, 0).text()  # Cột 0 chứa ID sản phẩm


        from Nhanvien.updateNV import UpdateEmployee
        self.sua_nv_window = UpdateEmployee(employee_id, self.db)
        self.sua_nv_window.show()
        self.load_and_update_table()  # Cập nhật bảng sau khi đóng cửa sổ
