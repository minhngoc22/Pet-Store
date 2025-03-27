import sys
import hashlib
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMessageBox
from SQL_database.csdl_ND import UserDatabase  # Import lớp xử lý CSDL người dùng
from Nguoidung.ui_updateND import Ui_MainWindow  # Đảm bảo file UI tồn tại

class UpdateUser(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, user_code, db):
        super().__init__()
        self.setupUi(self)
        self.db = db  # Kết nối database
        self.user_code = user_code  # Lưu ID người dùng cần sửa

        # Tải dữ liệu lên form
        self.load_user_data()

        # Khóa không cho sửa mã người dùng và tên đăng nhập
        self.txt_maND.setReadOnly(True)
        #self.txt_tenDN.setReadOnly(True)

        # Kết nối sự kiện
        self.btn_luu.clicked.connect(self.update_user)

    def load_user_data(self):
        """Tải thông tin người dùng lên form"""
        user = self.db.get_user_by_code(self.user_code)
        if not user:
            QMessageBox.critical(self, "Lỗi", "Không tìm thấy người dùng!")
            self.close()
            return

        # Gán dữ liệu vào các trường nhập liệu
        self.txt_maND.setPlainText(str(user["user_code"]))  # Mã người dùng (khóa)
        self.txt_tenND.setPlainText(str(user["full_name"]))  # Họ và Tên
        self.txt_tenDN.setPlainText(str(user["username"]))  # Tên đăng nhập (khóa)
        
        self.txt_note.setPlainText(str(user["note"]))  # Ghi chú

         # Load danh sách vai trò
        roles = self.db.get_all_roles()
        self.cbo_role.clear()  # Xóa dữ liệu cũ trong combobox
        self.cbo_role.addItems(roles)  # Thêm danh sách vai trò vào combobox

    # Đặt vai trò hiện tại của người dùng
        index = self.cbo_role.findText(user["role"])
        if index != -1:
            self.cbo_role.setCurrentIndex(index)

    def update_user(self):
        """Xử lý cập nhật thông tin người dùng"""
        username = self.txt_tenDN.toPlainText().strip()
        name = self.txt_tenND.toPlainText().strip()
        role = self.cbo_role.currentText()
        note = self.txt_note.toPlainText().strip()
        new_pass = self.txt_newpass.toPlainText().strip()

    # Kiểm tra nếu có mật khẩu mới
        hashed_password = None
        if new_pass:
            hashed_password = hashlib.sha256(new_pass.encode()).hexdigest()

    # Không cho phép cập nhật vai trò nếu người dùng là "Khách hàng"
        current_user = self.db.get_user_by_code(self.user_code)
        if current_user and current_user["role"] == "Khách hàng" and role != "Khách hàng":
            QMessageBox.warning(self, "Lỗi", "Không thể thay đổi vai trò của khách hàng!")
            return

    # Gọi update_user() với số tham số đúng
        if hashed_password:
            success = self.db.update_user(
                self.user_code, username, name, role, hashed_password, note
        )
        else:
            success = self.db.update_user(
                self.user_code, username, name, role, note
        )

        if success:
            QMessageBox.information(self, "Thành công", "Cập nhật người dùng thành công!")
            self.close()  # Đóng cửa sổ sau khi cập nhật
        else:
            QMessageBox.critical(self, "Lỗi", "Cập nhật người dùng thất bại!")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = UserDatabase()  # Khởi tạo database
    window = UpdateUser(user_id=1, db=db)  # Truyền user_id cần chỉnh sửa
    window.show()
    sys.exit(app.exec())
