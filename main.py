import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from UIPython.ui_mainwindow import Ui_UIMainWindow



class MainWindowMain(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_UIMainWindow()
        self.ui.setupUi(self)

        # Kết nối sự kiện
        self.ui.Menu.setCurrentIndex(0)  # Trang chủ sẽ là trang đầu tiên

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
            self.show_login()
            

    def show_login():
        from dangnhap import Login  # Import bên trong hàm để tránh vòng lặp
        login_window = Login()
        login_window.show()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowMain()
    
    window.show()
    sys.exit(app.exec())
    
