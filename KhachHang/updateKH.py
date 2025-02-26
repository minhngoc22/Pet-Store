import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMessageBox
from SQL_database.csdl_KH import CustomerDatabase
from KhachHang.ui_updateKH import Ui_MainWindow # Đảm bảo file .ui tồn tại

class UpdateCustomer(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, customer_code, db):
        super().__init__()
        self.setupUi(self)
        self.db = db  # Nhận database từ bên ngoài
        self.customer_code = customer_code

        # Tải dữ liệu khách hàng lên form
        self.load_customer_data()

        # Kết nối sự kiện
        self.btn_luu.clicked.connect(self.update_customer)

    def load_customer_data(self):
        """Tải thông tin khách hàng lên form"""
        customer = self.db.get_customer_by_code(self.customer_code)
        if not customer:
            QMessageBox.critical(self, "Lỗi", "Không tìm thấy khách hàng!")
            self.close()
            return

        # Gán dữ liệu vào các trường nhập liệu
        self.txt_maKH.setPlainText(str(customer["customer_code"]))  # Mã khách hàng
        self.txt_tenKH.setPlainText(str(customer["full_name"]))  # Tên khách hàng
        self.txt_sdt.setPlainText(str(customer["phone"]))  # Số điện thoại
        self.txt_email.setPlainText(str(customer["email"]))  # Email
        self.txt_diachi.setPlainText(str(customer["address"]))  # Địa chỉ
        self.txt_note.setPlainText(str(customer["note"]))  # Ghi chú

    def update_customer(self):
        """Xử lý cập nhật thông tin khách hàng"""
        new_name = self.txt_tenKH.toPlainText().strip()
        new_phone = self.txt_sdt.toPlainText().strip()
        new_email = self.txt_email.toPlainText().strip()
        new_address = self.txt_diachi.toPlainText().strip()
        new_note = self.txt_note.toPlainText().strip()

        # Kiểm tra dữ liệu nhập vào
        if not new_name or not new_phone or not new_email or not new_address:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        if not new_phone.isdigit():
            QMessageBox.warning(self, "Lỗi", "Số điện thoại phải là số!")
            return

        # Cập nhật vào CSDL
        success = self.db.update_customer(
            self.customer_code, new_name, new_phone, new_email, new_address, new_note
        )

        if success:
            QMessageBox.information(self, "Thành công", "Cập nhật khách hàng thành công!")
            self.close()  # Đóng cửa sổ sau khi cập nhật
        else:
            QMessageBox.critical(self, "Lỗi", "Cập nhật khách hàng thất bại!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = CustomerDatabase()  # Khởi tạo database
    window = UpdateCustomer(customer_code=1, db=db)  # Đổi `employee_code` thành `customer_code`
    window.show()
    sys.exit(app.exec())
