from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from SQL_database.csdl_DH import OrderDatabase
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from Donhang.ui_themDH import Ui_Form

class ThemDonHang(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # 🛠 Gọi constructor của lớp cha trước
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = OrderDatabase()
        self.customer_id = None  # Lưu ID khách hàng sau khi tìm kiếm

        # Gán sự kiện
        self.ui.btn_them.clicked.connect(self.create_order)
        self.ui.btn_timKH.clicked.connect(self.find_customer)

        self.load_employee_list()
        self.load_status_payment_options()

    def load_employee_list(self):
        """Tải danh sách nhân viên từ CSDL vào cbo_nvxl"""
        employees = self.db.get_all_employees()
        if employees:
            self.ui.cbo_nvxl.addItems(employees)
        else:
            QMessageBox.warning(None, "Lỗi", "Không thể tải danh sách nhân viên!")

    def load_status_payment_options(self):
        """Tải danh sách trạng thái và phương thức thanh toán"""
        self.ui.cbo_trangthai.clear()  # Xóa dữ liệu cũ trước khi thêm mới
        self.ui.cbo_thanhtoan.clear()

    # Cập nhật đúng giá trị trạng thái theo database
        self.ui.cbo_trangthai.addItems(["Đang xử lý", "Hoàn thành", "Đang giao"])
        self.ui.cbo_thanhtoan.addItems(["Đã thanh toán", "Chưa thanh toán"])


    def find_customer(self):
        from Donhang.timKH import TimKhachHang
        self.tim_khach_hang = TimKhachHang(parent_form=self)
        self.tim_khach_hang.show()
    

    def create_order(self):
        customer_code = self.ui.txt_maKH.toPlainText().strip()  # Lấy mã khách hàng từ giao diện
        employee_name = self.ui.cbo_nvxl.currentText()  # Lấy tên nhân viên từ combobox
        total_amount = float(self.ui.txt_tongtien.toPlainText())  # Lấy tổng tiền
        status = self.ui.cbo_trangthai.currentText()  # Lấy trạng thái đơn hàng
        payment = self.ui.cbo_thanhtoan.currentText()  # Lấy trạng thái thanh toán
        note = self.ui.txt_note.toPlainText()  # Lấy ghi chú

        employee_id = employee_name  # Chuyển tên nhân viên thành ID

        if total_amount <= 0:
            QMessageBox.warning(None, "Lỗi", "Tổng tiền không hợp lệ!")
            return
        if not total_amount:
            QMessageBox.warning(None, "Lỗi", "Vui lòng nhập tổng tiền!")
            return

     #✅ Lấy customer_id từ mã customer_code nếu chưa có
        if self.customer_id is None:
            self.customer_id = customer_code

        if not self.customer_id:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy khách hàng!")
            return

        success = self.db.add_order(self.customer_id, employee_id, total_amount, status, payment, note)

        if success:
            QMessageBox.information(self, "Thành công", "Đơn hàng đã được thêm!")
            from  Donhang.themCT import ThemChiTiet
            self.them_chitiet = ThemChiTiet()
            self.them_chitiet.show()
            self.close()
        else:
            QMessageBox.warning(self, "Lỗi", "Không thể thêm đơn hàng!")


  


    



