import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMessageBox
from SQL_database.csdl_KH import CustomerDatabase  # Đảm bảo file tồn tại
from KhachHang.ui_themKH import Ui_MainWindow# Đảm bảo file tồn tại

class EventHandler(QtWidgets.QMainWindow):
    def __init__(self, phone_number=""):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = CustomerDatabase()  # Kết nối CSDL

        self.ui.txt_sdt.setPlainText(phone_number)
        self.ui.btn_them.clicked.connect(self.add_customer)  # Đổi tên hàm cho phù hợp

    def add_customer(self):
        """Xử lý sự kiện thêm khách hàng"""
        name = self.ui.txt_tenKH.toPlainText().strip()
        email = self.ui.txt_email.toPlainText().strip()
        address = self.ui.txt_diachi.toPlainText().strip()
        phone = self.ui.txt_sdt.toPlainText().strip()
        note = self.ui.txt_note.toPlainText().strip()

        if not name or not email or not address or not phone:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin khách hàng!")
            return

        if not phone.isdigit():
            QMessageBox.warning(self, "Lỗi", "Số điện thoại phải là số!")
            return

        # Thêm khách hàng vào CSDL
        if self.db.add_customer(name, phone, email, address, note):
            QMessageBox.information(self, "Thành công", "Khách hàng đã được thêm vào!")

           

            
            self.clear_fields()
            self.close()
        else:
            QMessageBox.warning(self, "Lỗi", "Email hoặc số điện thoại đã tồn tại!")

    def clear_fields(self):
        """Xóa dữ liệu trong form sau khi thêm thành công"""
        self.ui.txt_tenKH.clear()
        self.ui.txt_email.clear()
        self.ui.txt_diachi.clear()
        self.ui.txt_sdt.clear()
        self.ui.txt_note.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EventHandler()
    window.show()
    sys.exit(app.exec())
