from PyQt6.QtWidgets import QMessageBox, QInputDialog
from PyQt6 import QtWidgets
from PyQt6.QtCore import QSettings
from SQL_database.csdl_DH import OrderDatabase
from Donhang.ui_themDH import Ui_Form


class ThemDonHang(QtWidgets.QMainWindow):
    def __init__(self ):
        super().__init__()  
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = OrderDatabase()
        self.customer_id = None  
        settings = QSettings("MyApp", "UserSettings")
        self.current_username = settings.value("username")  # ✅ Lấy username từ QSettings

        # Gán sự kiện
        self.ui.btn_them.clicked.connect(self.create_order)

        self.load_employee_list()

    def load_employee_list(self):
        """Tải danh sách nhân viên từ CSDL vào cbo_nvxl và chọn nhân viên đăng nhập làm mặc định"""
        employees = self.db.get_all_employees()  # 🔹 Lấy danh sách tất cả nhân viên

        if employees:
            self.ui.cbo_nvxl.addItems(employees)  # Thêm vào combobox

        # ✅ Lấy nhân viên đang đăng nhập
            logged_in_employee = self.db.get_logged_in_employee(self.current_username)  

            if logged_in_employee:
                full_name = logged_in_employee["full_name"]
                index = self.ui.cbo_nvxl.findText(full_name)  # Tìm vị trí của nhân viên đăng nhập
                if index >= 0:
                    self.ui.cbo_nvxl.setCurrentIndex(index)  # Đặt làm mặc định

        else:
            QMessageBox.warning(self, "Lỗi", "Không thể tải danh sách nhân viên!")



    def create_order(self):
        phone_number = self.ui.txt_sdt.toPlainText().strip()
        employee_name = self.ui.cbo_nvxl.currentText()
        

        # 🔍 Kiểm tra khách hàng theo số điện thoại
        self.customer_id = self.db.get_customer_id_by_phone(phone_number)

    # Nếu khách hàng chưa tồn tại, mở form thêm khách hàng
        if self.customer_id is None:
            from KhachHang.themKH import EventHandler
            self.them_khachhang = EventHandler(phone_number)  # Truyền số điện thoại để tự điền
            self.them_khachhang.show()
            return  # Chờ thêm khách hàng xong mới tạo đơn hàng

    # ✅ Thêm đơn hàng
        success = self.db.add_order(self.customer_id, employee_name, "")

        if success:
            order_id = self.db.get_last_inserted_order_code()
            if order_id:
                QMessageBox.information(self, "Thành công", f"Đơn hàng đã được thêm với mã: {order_id}")

                # 👉 Mở form thêm chi tiết đơn hàng
                from Donhang.themCT import ThemChiTiet
                self.them_chitiet = ThemChiTiet(order_id)
                self.them_chitiet.show()
            else:
                QMessageBox.warning(self, "Lỗi", "Không thể lấy mã đơn hàng!")
        else:
            QMessageBox.warning(self, "Lỗi", "Không thể thêm đơn hàng!")

        self.close()