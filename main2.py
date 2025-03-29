import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from Main.ui_main2window import Ui_MainWindow
from SanPham.sanPham import Sanpham  # Import class xử lý sự kiện sản phẩm
from Donhang.donHang import Donhang  # Import class xử lý sự kiện đơn hàng
from KhachHang.khachHang import KhachHang  # Import class xử lý sự kiện khách hàng
from NhaCungCap.nhaCungCap import NhaCungCap  # Import class xử lý sự kiện nhà cung cấp
from Trangchu.hom2 import Home2
class Main2App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Tạo đối tượng lớp xử lý sự kiện sản phẩm
        self.sanpham_handler = Sanpham(self.ui)  
        self.donhang_handler = Donhang(self.ui)
        self.khachhang_handler = KhachHang(self.ui)
        self.nhacc_handler = NhaCungCap(self.ui)
        self.home_handler = Home2(self.ui)

        # Chọn trang mặc định
        self.ui.Menu.setCurrentIndex(0)

        # Kết nối sự kiện chuyển trang
        self.ui.btn_home.clicked.connect(self.trangchu)
        self.ui.btn_spham.clicked.connect(self.sanpham)
        self.ui.btn_donhang.clicked.connect(self.donhang)
        self.ui.btn_khachhang.clicked.connect(self.khachhang)
        self.ui.btn_nhacc.clicked.connect(self.nhacc)
        # Kết nối sự kiện đăng xuất
        self.ui.btn_logout.clicked.connect(self.logout)

    def trangchu(self):
        """Chuyển về trang chủ"""
        self.ui.Menu.setCurrentIndex(0)

    def sanpham(self):
        """Chuyển về trang sản phẩm"""
        self.ui.Menu.setCurrentIndex(1)



    def donhang(self):
        """Chuyển về trang đơn hàng"""
        self.ui.Menu.setCurrentIndex(3)

    def khachhang(self):
        """Chuyển về trang khách hàng"""
        self.ui.Menu.setCurrentIndex(4)
    
    def nhacc(self):
        """Chuyển về trang nhà cung cấp"""
        self.ui.Menu.setCurrentIndex(5)
  
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
            from dangnhap import Login  # Import class đăng nhập
            self.login_window = Login()
            self.login_window.show()
           

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main2App()
    window.show()
    sys.exit(app.exec())
