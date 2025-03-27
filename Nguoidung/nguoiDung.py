import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt
from SQL_database.csdl_ND import UserDatabase  # Import lớp kết nối SQLite

class NguoiDung:
    def __init__(self, ui):
        self.ui = ui
        self.model = QStandardItemModel()
        self.ui.tb_user.setModel(self.model)
        
        # Kết nối CSDL
        self.db = UserDatabase()
        if not self.db.connect():
            QMessageBox.critical(self.ui, "Lỗi", "Không thể kết nối CSDL người dùng!")
            return

        # Gán sự kiện cho các nút
        self.ui.btn_refresh_2.clicked.connect(self.refresh_data)
        self.ui.btn_themND.clicked.connect(self.show_add_user)
        self.ui.btn_xoa.clicked.connect(self.delete_user)
        self.ui.btn_sua.clicked.connect(self.show_update_user)
        self.ui.btn_timkiem.clicked.connect(self.search_user)
        self.ui.cbo_role.currentIndexChanged.connect(self.filter_users)
        
        # Nạp danh sách vai trò
        self.load_roles()
        self.load_and_update_table()
    
    def load_and_update_table(self, users=None):
        """Tải và cập nhật bảng người dùng"""
        if users is None:
            _, users = self.db.get_all_users()

        self.model.clear()
        column_names = ["Mã Người Dùng", "Tên Đăng Nhập","Mật Khẩu" ,"Tên Người Dùng", "Email", "Vai Trò", "Ghi chú"]
        self.model.setColumnCount(len(column_names))
        self.model.setHorizontalHeaderLabels(column_names)

        for row_idx, row_data in enumerate(users):
            for col_idx, value in enumerate(row_data):
                item = QStandardItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.model.setItem(row_idx, col_idx, item)
        
        self.ui.tb_user.setModel(self.model)
        self.ui.tb_user.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
    
    def load_roles(self):
        """Tải danh sách vai trò vào ComboBox"""
        roles = self.db.get_all_roles()
        self.ui.cbo_role.clear()
        self.ui.cbo_role.addItem("Tất cả")
        for role in roles:
            self.ui.cbo_role.addItem(role.strip())  # Loại bỏ khoảng trắng thừa

    
    def filter_users(self): 
        """Lọc người dùng theo vai trò"""
        selected_role = self.ui.cbo_role.currentText()
    
        success, users = self.db.get_users_by_role(selected_role)  # Tách biến trạng thái và dữ liệu
    
        if success:
            self.load_and_update_table(users)
        else:
            QMessageBox.critical(None, "Lỗi", "Không thể lọc người dùng theo vai trò!")

    
    def delete_user(self):
        """Xóa người dùng được chọn khỏi CSDL bằng Mã Người Dùng"""
        selected_indexes = self.ui.tb_user.selectionModel().selectedRows()
        if not selected_indexes:
            QMessageBox.warning(None, "Chú ý", "Vui lòng chọn một người dùng để xóa.")
            return

        selected_row = selected_indexes[0].row()
        user_id = self.model.item(selected_row, 0).text().strip()

        reply = QMessageBox.question(
            None, "Xác nhận", f"Bạn có chắc chắn muốn xóa người dùng có Mã ID: {user_id}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            if self.db.delete_user(user_id):
                QMessageBox.information(None, "Thành công", "Người dùng đã được xóa.")
                self.load_and_update_table()
            else:
                QMessageBox.critical(None, "Lỗi", "Xóa người dùng thất bại!")
    
    def search_user(self):
        """Tìm kiếm người dùng theo tên hoặc email"""
        search_text = self.ui.txt_timkiem.toPlainText().strip()
        if not search_text:
            self.load_and_update_table()
            return
        
        users = self.db.get_user_by_name(search_text)
        self.load_and_update_table(users)
    
    def refresh_data(self):
        """Làm mới dữ liệu bảng người dùng"""
        self.load_and_update_table()
        self.load_roles()
        self.ui.cbo_role.setCurrentIndex(0)
        self.ui.txt_timkiem.clear()
    
    def show_add_user(self):
        """Mở form thêm người dùng"""
        
        from Nguoidung.themND import UserEventHandler
        self.themnv_window = UserEventHandler()
        self.themnv_window.show()

    def show_update_user(self):
        """Mở form cập nhật thông tin người dùng"""
        selected_indexes = self.ui.tb_user.selectionModel().selectedRows()
        if not selected_indexes:
            QMessageBox.warning(None, "Chú ý", "Vui lòng chọn một người dùng để sửa.")
            return

        selected_row = selected_indexes[0].row()
        user_code = self.model.item(selected_row, 0).text().strip()

        from Nguoidung.updateND import UpdateUser  # Import form cập nhật người dùng

    # Mở form cập nhật với user_id
        self.sua_user_window = UpdateUser(user_code, self.db)
        self.sua_user_window.show()

 

