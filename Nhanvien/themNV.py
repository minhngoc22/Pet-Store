import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore
from Nhanvien.ui_themNV import Ui_themnhanvien  # Đảm bảo file tồn tại
from SQL_database.csdl_NV import EmployeeDatabase  # Đảm bảo file tồn tại

class EventHandler(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_themnhanvien()
        self.ui.setupUi(self)
        self.image_path = None  # Lưu đường dẫn ảnh
        self.db = EmployeeDatabase()  # Kết nối CSDL

       
        
        self.ui.btn_them.clicked.connect(self.add_nv)
       

    def add_nv(self):
        """Xử lý sự kiện thêm nhân viên"""
        name = self.ui.txt_tennv.toPlainText().strip()
        position = self.ui.txt_vitri.toPlainText().strip()
        salary = self.ui.txt_luong.toPlainText().strip()
        email = self.ui.txt_email.toPlainText().strip()
        address = self.ui.txt_diachi.toPlainText().strip()
        phone = self.ui.txt_sdt.toPlainText().strip()

        if not name or not salary or not position or not email or not address or not phone:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin nhân viên!")
            return

        try:
            salary = float(salary)  # Đảm bảo lương là số
            if not phone.isdigit():
                raise ValueError("Số điện thoại phải là số!")

         # Thêm nhân viên vào CSDL (ID sẽ tự động tăng)
            if self.db.add_employee(name, phone,  email,address, salary,  position ):
                QMessageBox.information(self, "Thành công", "Nhân viên đã được thêm vào!")
                self.clear_fields()
            else:
                QMessageBox.warning(self, "Lỗi", "Email hoặc số điện thoại đã tồn tại!")
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Lương phải là số hợp lệ và số điện thoại chỉ chứa số!")

    def clear_fields(self):
            """Xóa dữ liệu trong form sau khi thêm thành công"""
            self.ui.txt_tennv.clear()
            self.ui.txt_luong.clear()
            self.ui.txt_email.clear()
            self.ui.txt_diachi.clear()
            self.ui.txt_sdt.clear()
            self.ui.txt_vitri.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EventHandler()
    window.show()
    sys.exit(app.exec())
