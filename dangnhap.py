import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import QSettings
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QPixmap
from Dangnhap.ui_dangnhap import Ui_LoginWindow
from SQL_database.ketnoiSQL import Database  # Đảm bảo file `ketnoiSQL.py` có class Database

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
        username = self.ui.txt_ten.text().strip()
        password = self.ui.txt_pass.text().strip()

        msg = QMessageBox()

        if not username or not password:
            msg.setWindowTitle("Thông báo")
            msg.setText("Vui lòng nhập đầy đủ thông tin!")
            pixmap = QPixmap("hinhanh/2.png")  # Ảnh cảnh báo
            if not pixmap.isNull():
                msg.setIconPixmap(pixmap)
            msg.exec()
            return

    # Kết nối CSDL và kiểm tra đăng nhập
        self.db.connect()
        role = self.db.check_login(username, password)  # Lấy vai trò của user
        

        if role:
            msg.setWindowTitle("Thông báo")
            msg.setText("Đăng nhập thành công!")
            pixmap = QPixmap("hinhanh/1.ico")  # Ảnh thành công
            if not pixmap.isNull():
                msg.setIconPixmap(pixmap)
            msg.exec()
            settings = QSettings("MyApp", "UserSettings")
            settings.setValue("username", username)  # ✅ Lưu username vào QSettings
           

        # Mở giao diện theo vai trò
            if role.lower() == "admin":
                self.open_main_window()  # Giao diện chính cho admin
            else:
                self.open_main_window2()  # Giao diện khác cho nhân viên

            self.close()  # Đóng cửa sổ đăng nhập
        else:
            msg.setWindowTitle("Thông báo")
            msg.setText("Sai thông tin đăng nhập. Vui lòng kiểm tra lại!")
            pixmap = QPixmap("hinhanh/2.ico")  # Ảnh báo lỗi
            if not pixmap.isNull():
                msg.setIconPixmap(pixmap)
            msg.exec()

        self.db.close()


    def open_main_window(self):
        """Mở cửa sổ chính sau khi đăng nhập thành công"""
        from main import MainApp
        self.main_window = MainApp()  # ✅ Lưu tham chiếu tránh bị đóng
        self.main_window.show()
        self.close()  # Đóng cửa sổ đăng nhập

    def open_main_window2(self):
        """Mở cửa sổ chính sau khi đăng nhập thành công"""
        from main2 import Main2App
        self.main_window = Main2App()  # ✅ Lưu tham chiếu tránh bị đóng
        self.main_window.show()
        self.close()  # Đóng cửa sổ đăng nhập


if __name__ == "__main__":
    print("🔵 [START] Khởi chạy ứng dụng...")
    app = QtWidgets.QApplication(sys.argv)
    window = Login()
    window.show()
    print("🟢 [RUNNING] Ứng dụng đang chạy...")
    sys.exit(app.exec())
