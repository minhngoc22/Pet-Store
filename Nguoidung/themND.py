import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMessageBox
from SQL_database.csdl_ND import UserDatabase  # Đảm bảo file tồn tại
from Nguoidung.ui_themND import Ui_MainWindow  # Đảm bảo file tồn tại
import re  # Thêm thư viện kiểm tra email

class UserEventHandler(QtWidgets.QMainWindow):
    def __init__(self, full_name="", email=""):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = UserDatabase()  # Kết nối CSDL

        # Điền sẵn dữ liệu nếu có
        self.ui.txt_tenND.setPlainText(full_name)
        self.ui.txt_email.setPlainText(email)

          # Load danh sách vai trò vào combobox
        self.load_roles()


        self.ui.btn_them.clicked.connect(self.add_user)  # Xử lý nút "Thêm"
        
    def load_roles(self):
        """Tải danh sách vai trò từ CSDL lên combobox"""
        roles = self.db.get_all_roles()  # Hàm này sẽ truy vấn danh sách role từ CSDL
        self.ui.cbo_role.clear()
        if roles:
            self.ui.cbo_role.addItems(roles)
        else:
            QMessageBox.warning(self, "Lỗi", "Không thể tải danh sách vai trò!")

    def add_user(self):
        """Xử lý sự kiện thêm người dùng"""
        username = self.ui.txt_tenDN.toPlainText().strip()
        full_name = self.ui.txt_tenND.toPlainText().strip()
        password = self.ui.txt_pass.toPlainText().strip()
        email = self.ui.txt_email.toPlainText().strip()
        role = self.ui.cbo_role.currentText().strip()  # Lấy vai trò từ combobox
        note = self.ui.txt_note.toPlainText().strip()

        # Kiểm tra các trường không được để trống
        if not username or not full_name or not email or not role or not password:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin người dùng!")
            return

        # Kiểm tra định dạng email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            QMessageBox.warning(self, "Lỗi", "Email không hợp lệ!")
            return

        # Thêm người dùng vào CSDL
        if self.db.add_user(username, password, full_name, email, role, note):
            QMessageBox.information(self, "Thành công", "Người dùng đã được thêm vào!")
            self.clear_fields()
            self.close()  # Đóng form sau khi thêm
        else:
            QMessageBox.warning(self, "Lỗi", "Tên đăng nhập hoặc Email đã tồn tại!")

    def clear_fields(self):
        """Xóa dữ liệu trong form sau khi thêm thành công"""
        self.ui.txt_tenND.clear()
        self.ui.txt_pass.clear()
        self.ui.txt_tenDN.clear()
        self.ui.txt_email.clear()
        self.ui.txt_note.clear()