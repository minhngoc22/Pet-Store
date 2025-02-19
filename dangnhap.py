import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QPixmap
from UIPython.ui_dangnhap import Ui_LoginWindow
from main import MainWindowMain
from ketnoiSQL import Database
import hinhanh

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.db = Database()
        self.ui.setupUi(self)

        # 🔗 Kết nối trực tiếp với MySQL

        self.ui.btn_dangnhap.clicked.connect(self.login)

    def login(self):
        username = self.ui.txt_ten.text()
        password = self.ui.txt_pass.text()

        msg = QMessageBox()

        if username =="" or password =="":
            msg.setWindowTitle("Thông báo")
            msg.setText("Vui lòng nhập đầy đủ thông tin")
            # Chỉnh đường dẫn tới file ảnh của bạn (đảm bảo file ảnh tồn tại)
            pixmap = QPixmap("hinhanh/2.png")  
            # Nếu ảnh không tải được, bạn có thể kiểm tra lại đường dẫn
            if not pixmap.isNull():
                msg.setIconPixmap(pixmap)
            msg.exec()

        if self.db.check_login(username, password):
            msg.setWindowTitle("Thông báo")
            msg.setText("Đăng nhập thành công")
            # Chỉnh đường dẫn tới file ảnh của bạn (đảm bảo file ảnh tồn tại)
            pixmap = QPixmap("hinhanh/1.png")  
            # Nếu ảnh không tải được, bạn có thể kiểm tra lại đường dẫn
            if not pixmap.isNull():
                msg.setIconPixmap(pixmap)
            msg.exec()
            self.close()
            self.open_main_window()

        else:
            
            # Tạo MessageBox với ảnh lỗi
            
            msg.setWindowTitle("Thông báo")
            msg.setText("Sai thông tin đăng nhập. Vui lòng kiểm tra lại!")
            pixmap = QPixmap(".png")
            if not pixmap.isNull():
                msg.setIconPixmap(pixmap)
            else:
                print("Không tải được ảnh image_error.png")
            msg.exec()


    def open_main_window(self):
        from main import MainWindowMain
        
        self.main_window = MainWindowMain()  # ✅ Lưu lại tham chiếu
        self.main_window.show()
        self.close()  # Đóng cửa sổ đăng nhập


            
if __name__ == "__main__":
    print("🔵 [START] Khởi chạy ứng dụng...")
    app = QtWidgets.QApplication(sys.argv)
    window = Login()
    window.show()
    print("🟢 [RUNNING] Ứng dụng đang chạy...")
    sys.exit(app.exec())
