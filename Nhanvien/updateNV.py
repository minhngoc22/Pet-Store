import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMessageBox
from SQL_database.csdl_NV import EmployeeDatabase
from Nhanvien.ui_updateNV import Ui_updateNV  # Đảm bảo file .ui tồn tại

class UpdateEmployee(QtWidgets.QMainWindow, Ui_updateNV):
    def __init__(self, employee_code, db):
        super().__init__()
        self.setupUi(self)
        self.db = db  # Nhận database từ bên ngoài
        self.employee_code= employee_code

        
        # Tải dữ liệu nhân viên lên form
        self.load_employee_data()

        # Kết nối sự kiện
        self.btn_luunv.clicked.connect(self.update_employee)

    def load_employee_data(self):
        """Tải thông tin nhân viên lên form"""
        employee = self.db.get_employee_by_code(self.employee_code)
        if not employee:
            QMessageBox.critical(self, "Lỗi", "Không tìm thấy nhân viên!")
            self.close()
            return

        # Gán dữ liệu vào các trường nhập liệu
        self.txt_manv.setPlainText(str(employee["employee_code"]))  # Mã nhân viên
        self.txt_tennv.setPlainText(str(employee["full_name"]))  # Tên nhân viên
        self.txt_sdt.setPlainText(str(employee["phone"]))    # Số điện thoại
        self.txt_email.setPlainText(str(employee["email"]))  # Email
        self.txt_diachi.setPlainText(str(employee["address"])) # Địa chỉ
        self.txt_luong.setPlainText(str(employee["salary"]))  # Lương
        self.txt_vitri.setPlainText(str(employee["position"]))  # Vị trí
        self.txt_note.setPlainText(str(employee["note"]))  # Ghi chú

    def update_employee(self):
        """Xử lý cập nhật thông tin nhân viên"""
        new_name = self.txt_tennv.toPlainText().strip()
        new_phone = self.txt_sdt.toPlainText().strip()
        new_email = self.txt_email.toPlainText().strip()
        new_address = self.txt_diachi.toPlainText().strip()
        new_salary = self.txt_luong.toPlainText().strip()
        new_position = self.txt_vitri.toPlainText().strip()
        new_note = self.txt_note.toPlainText().strip()

        # Kiểm tra dữ liệu nhập vào
        if not new_name or not new_phone or not new_email or not new_address or not new_salary or not new_position:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        try:
            new_salary = float(new_salary)  # Chuyển lương thành số thực
            if not new_phone.isdigit():
                raise ValueError("Số điện thoại phải là số!")

        except ValueError as e:
            QMessageBox.warning(self, "Lỗi", str(e))
            return

        # Cập nhật vào CSDL
        success = self.db.update_employee(
            self.employee_code ,new_name, new_phone, new_email, new_address, new_salary, new_position,new_note
        )

        if success:
            QMessageBox.information(self, "Thành công", "Cập nhật nhân viên thành công!")
            self.close()  # Đóng cửa sổ sau khi cập nhật
        else:
            QMessageBox.critical(self, "Lỗi", "Cập nhật nhân viên thất bại!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = EmployeeDatabase()  # Khởi tạo database
    window = UpdateEmployee(employee_id=1)  # Mặc định Mã NV là 1 để test
    window.show()
    sys.exit(app.exec())
