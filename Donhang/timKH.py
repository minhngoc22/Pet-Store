import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from Donhang.ui_timKH import Ui_Form  # Import file giao diện UI
from SQL_database.csdl_DH import OrderDatabase  # Import class xử lý CSDL
from KhachHang.themKH import EventHandler  # Import form thêm khách hàng

class TimKhachHang(QtWidgets.QWidget):
    def __init__(self,parent_form=None):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.parent_form = parent_form  # Lưu tham chiếu đến form ThemDonHang
        self.them_khach_hang = None  # Biến lưu form thêm khách hàng

        # Kết nối database
        self.db = OrderDatabase()
        if not self.db.connect():
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối CSDL khách hàng!")
            return

        # Gán sự kiện cho nút tìm kiếm
        self.ui.btn_timKH.clicked.connect(self.tim_khach_hang)

    def tim_khach_hang(self):
        """Tìm khách hàng theo số điện thoại hoặc email"""
        search_value = self.ui.txt_tim.toPlainText().strip()

        if not search_value:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập số điện thoại hoặc email!")
            return

        customer_id = self.db.get_customer_by_phone_or_email(search_value)

        if customer_id and self.parent_form:
            self.ui.txt_maKH.setText(customer_id)  # Hiển thị mã khách hàng
            self.parent_form.ui.txt_maKH.setText(customer_id)
            QMessageBox.information(None, "Thông báo", "Tìm thấy khách hàng coi mã: " + customer_id)
            self.close()
           
        else:
        
            QMessageBox.information(None, "Thông báo", "Không tìm thấy khách hàng!")
            reply = QMessageBox.question(self, "Thông báo", "Bạn có muốn thêm khách hàng mới không?", 
                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.Yes:
    # Mở form thêm khách hàng và truyền `self`
                self.them_khach_hang = EventHandler(self)
                self.them_khach_hang.show()
                self.close()


    def cap_nhat_maKH(self, new_customer_id):
        """Cập nhật mã khách hàng sau khi thêm mới"""
        self.ui.txt_maKH.setText(new_customer_id)  # Hiển thị mã khách hàng mới
        if self.parent_form:
            self.parent_form.ui.txt_maKH.setText(new_customer_id)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TimKhachHang()
    window.show()
    sys.exit(app.exec())
