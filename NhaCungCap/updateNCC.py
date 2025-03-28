import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMessageBox
from SQL_database.csdl_nhaCC import SupplierDatabase  # Đổi từ CustomerDatabase -> SupplierDatabase
from NhaCungCap.ui_updateNCC import Ui_MainWindow  # Đảm bảo file .ui tồn tại

class UpdateSupplier(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, supplier_code, db):
        super().__init__()
        self.setupUi(self)
        self.db = db  
        self.supplier_code = supplier_code

        # Tải dữ liệu nhà cung cấp lên form
        self.load_supplier_data()

        # Kết nối sự kiện
        self.btn_luu.clicked.connect(self.update_supplier)

    def load_supplier_data(self):
        """Tải thông tin nhà cung cấp lên form"""
        supplier = self.db.get_supplier_by_code(self.supplier_code)
        if not supplier:
            QMessageBox.critical(self, "Lỗi", "Không tìm thấy nhà cung cấp!")
            self.close()
            return

        # Gán dữ liệu vào các trường nhập liệu
        self.txt_maNCC.setPlainText(str(supplier["supplier_code"]))  # Mã nhà cung cấp
        self.txt_maNCC.setReadOnly(True)
        self.txt_tenNCC.setPlainText(str(supplier["name"]))  # Tên nhà cung cấp
        self.txt_sdt.setPlainText(str(supplier["phone"]))  # Số điện thoại
        self.txt_email.setPlainText(str(supplier["email"]))  # Email
        self.txt_diachi.setPlainText(str(supplier["address"]))  # Địa chỉ
        self.txt_note.setPlainText(str(supplier["note"]))  # Ghi chú

    def update_supplier(self):
        """Cập nhật thông tin nhà cung cấp"""
        new_name = self.txt_tenNCC.toPlainText().strip()
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
        success = self.db.update_supplier(
            self.supplier_code, new_name, new_phone, new_email, new_address, new_note
        )

        if success:
            QMessageBox.information(self, "Thành công", "Cập nhật nhà cung cấp thành công!")
            self.close()  # Đóng cửa sổ sau khi cập nhật
        else:
            QMessageBox.critical(self, "Lỗi", "Cập nhật nhà cung cấp thất bại!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = SupplierDatabase()  # Khởi tạo database
    window = UpdateSupplier(supplier_code="NCC001", db=db)  # Truyền mã NCC phù hợp
    window.show()
    sys.exit(app.exec())
