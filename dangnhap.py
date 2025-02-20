import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QPixmap
from UIPython.ui_dangnhap import Ui_LoginWindow
from SQL_database.ketnoiSQL import Database  # Đảm bảo file `ketnoiSQL.py` có class Database
import hinhanh

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.db = Database()  # Kết nối CSDL
        self.ui.setupUi(self)

        # Kết nối sự kiện khi bấm nút đăng nhập
        self.ui.btn_dangnhap.clicked.connect(self.login)

    def login(self):
        """Xử lý đăng nhập"""
        username = self.ui.txt_ten.text().strip()  # Loại bỏ khoảng trắng thừa
        password = self.ui.txt_pass.text().strip()

        msg = QMessageBox()

        # 🔹 Kiểm tra nếu chưa nhập đủ thông tin
        if not username or not password:
            msg.setWindowTitle("Thông báo")
            msg.setText("Vui lòng nhập đầy đủ thông tin!")
            pixmap = QPixmap("hinhanh/2.png")  # Ảnh cảnh báo
            if not pixmap.isNull():
                msg.setIconPixmap(pixmap)
            msg.exec()
            return  # 🔹 Thêm return để không tiếp tục xử lý

        # Kết nối CSDL trước khi kiểm tra đăng nhập
        self.db.connect()
        if self.db.check_login(username, password):
            msg.setWindowTitle("Thông báo")
            msg.setText("Đăng nhập thành công!")
            pixmap = QPixmap("hinhanh/1.png")  # Ảnh thành công
            if not pixmap.isNull():
                msg.setIconPixmap(pixmap)
            msg.exec()

            # Đóng cửa sổ đăng nhập và mở giao diện chính
            self.open_main_window()
        else:
            msg.setWindowTitle("Thông báo")
            msg.setText("Sai thông tin đăng nhập. Vui lòng kiểm tra lại!")
            pixmap = QPixmap("hinhanh/2.png")  # Ảnh báo lỗi
            if not pixmap.isNull():
                msg.setIconPixmap(pixmap)
            msg.exec()

        # Đóng kết nối sau khi kiểm tra xong
        self.db.close()

    def open_main_window(self):
        """Mở cửa sổ chính sau khi đăng nhập thành công"""
        from main import MainWindowMain
        self.main_window = MainWindowMain()  # ✅ Lưu tham chiếu tránh bị đóng
        self.main_window.show()
        self.close()  # Đóng cửa sổ đăng nhập

if __name__ == "__main__":
    print("🔵 [START] Khởi chạy ứng dụng...")
    app = QtWidgets.QApplication(sys.argv)
    window = Login()
    window.show()
    print("🟢 [RUNNING] Ứng dụng đang chạy...")
    sys.exit(app.exec())
