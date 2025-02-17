import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from UIPython.ui_main import Ui_UIMainWindow  # Giao diện chính
from dangnhap import Login  # Import lớp Login (chứa cửa sổ đăng nhập)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_UIMainWindow()
        self.ui.setupUi(self)

        # Kết nối sự kiện
        self.ui.btn_home.clicked.connect(self.trangchu)
        self.ui.btn_dichvu.clicked.connect(self.dichvu)
        self.ui.btn_logout.clicked.connect(self.logout)

    def trangchu(self):
        """Chuyển về trang chủ"""
        self.ui.Menu.setCurrentIndex(0)

    def dichvu(self):
        """Chuyển về trang dịch vụ"""
        self.ui.Menu.setCurrentIndex(1)

    def logout(self):
        """Xử lý đăng xuất"""
        reply = QMessageBox.question(
            self, "Xác nhận", "Bạn có chắc chắn muốn đăng xuất?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            print("🔴 [LOGOUT] Đăng xuất thành công!")
            self.close()  # Đóng cửa sổ chính

            # Mở lại cửa sổ đăng nhập
            self.login = Login()  # Dùng lớp Login thay vì Ui_LoginWindow
            self.login.show()
        else:
            print("✅ [LOGOUT] Hủy đăng xuất!")




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    
    window.show()
    sys.exit(app.exec())
    
