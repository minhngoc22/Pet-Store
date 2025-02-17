import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from UIPython.ui_dangnhap import Ui_LoginWindow
from ketnoiSQL import Database

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        # 🔗 Kết nối trực tiếp với MySQL

        self.ui.btn_dangnhap.clicked.connect(self.check_login)

    def check_login(self):
        db = Database()
        db.connect()
        username = self.ui.txt_ten.text().strip()
        password = self.ui.txt_pass.text().strip()

        if db.check_login( username,password):
              print("✅ Đăng nhập thành công!")
        else:
            print("❌ Đăng nhập thất bại!")
 # Đóng kết nối
        db.close()
            
if __name__ == "__main__":
    print("🔵 [START] Khởi chạy ứng dụng...")
    app = QtWidgets.QApplication(sys.argv)
    window = Login()
    window.show()
    print("🟢 [RUNNING] Ứng dụng đang chạy...")
    sys.exit(app.exec())
