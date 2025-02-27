import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMessageBox
from SQL_database.csdl_KH import CustomerDatabase  # Đảm bảo file tồn tại
from KhachHang.ui_themKH import Ui_themKH # Đảm bảo file tồn tại

class EventHandler(QtWidgets.QMainWindow):
    def __init__(self, tim_khach_hang_form=None):
        super().__init__()
        self.ui = Ui_themKH()
        self.ui.setupUi(self)
        self.db = CustomerDatabase()  # Kết nối CSDL
        self.tim_khach_hang_form = tim_khach_hang_form  # Lưu tham chiếu form cha
        
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

              # Lấy mã khách hàng vừa thêm
            customer_id = self.db.get_last_inserted_customer_id()

            # Cập nhật mã khách hàng trong TimKhachHang
            if self.tim_khach_hang_form:
                self.tim_khach_hang_form.cap_nhat_maKH(customer_id)
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
