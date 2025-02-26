import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMessageBox
from SQL_database.csdl_nhaCC import  SupplierDatabase # Đảm bảo file tồn tại
from NhaCungCap.ui_themNCC import Ui_themNhaCC # Đảm bảo file tồn tại

class EventHandler(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_themNhaCC()
        self.ui.setupUi(self)
        self.db = SupplierDatabase()  # Kết nối CSDL
        
        self.ui.btn_them.clicked.connect(self.add_supplier)  # Đổi tên hàm cho phù hợp

    def add_supplier(self):
        """Xử lý sự kiện thêm khách hàng"""
        name = self.ui.txt_tenncc.toPlainText().strip()
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
        if self.db.add_supplier(name, phone, email, address, note):
            QMessageBox.information(self, "Thành công", "Khách hàng đã được thêm vào!")
            self.clear_fields()
        else:
            QMessageBox.warning(self, "Lỗi", "Email hoặc số điện thoại đã tồn tại!")

    def clear_fields(self):
        """Xóa dữ liệu trong form sau khi thêm thành công"""
        self.ui.txt_tenncc.clear()
        self.ui.txt_email.clear()
        self.ui.txt_diachi.clear()
        self.ui.txt_sdt.clear()
        self.ui.txt_note.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EventHandler()
    window.show()
    sys.exit(app.exec())
