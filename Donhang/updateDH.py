from PyQt6.QtWidgets import QMessageBox, QMainWindow
from PyQt6 import QtWidgets
from Donhang.ui_updateDH import Ui_Form
from SQL_database.csdl_DH import OrderDatabase

class UpdateDonHang(QMainWindow):
    def __init__(self, order_code):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = OrderDatabase()
        self.order_code = order_code # Lưu ID đơn hàng để cập nhật

      
        
        self.load_employee_list()  # Tải danh sách nhân viên vào ComboBox
        self.load_status_payment_options()  # Tải trạng thái & thanh toán
        self.load_order_data()  # Tải dữ liệu khi mở form
        
        self.ui.btn_luu.clicked.connect(self.update_order)  # Xử lý sự kiện Lưu

    def load_employee_list(self):
        """Tải danh sách nhân viên từ CSDL vào cbo_nvxl"""
        employees = self.db.get_all_employees()  # Lấy danh sách nhân viên
        if employees:
            self.ui.cbo_nvxl.addItems(employees)
        else:
            QMessageBox.warning(self, "Lỗi", "Không thể tải danh sách nhân viên!")

    def load_status_payment_options(self):
        """Tải danh sách trạng thái và phương thức thanh toán"""
        self.ui.cbo_trangthai.clear()
        self.ui.cbo_thanhtoan.clear()
  
        statuses = self.db.get_statuses()
        for status in statuses:
            self.ui.cbo_trangthai.addItem(status)

        payment_methods = self.db.get_payment_methods()
        for method in payment_methods:
            self.ui.cbo_thanhtoan.addItem(method)


    def load_order_data(self):
        """Tải dữ liệu đơn hàng lên form"""
        order = self.db.get_order_by_code(self.order_code)  # Lấy dữ liệu đơn hàng

        if order:
            self.ui.txt_maDH.setText(str(order["order_code"]))  # Mã đơn hàng
            self.ui.txt_maDH.setReadOnly(True)  # Không cho chỉnh sửa mã đơn hàng
            self.ui.txt_maKH.setText(str(order["customer_code"]))  # Mã khách hàng
            self.ui.txt_maKH.setReadOnly(True)  # Không cho chỉnh sửa mã khách hàng
            self.ui.txt_tongtien.setText(str(order["total_amount"]))  # Tổng tiền
            self.ui.cbo_trangthai.setCurrentText(order["status"])  # Trạng thái
            self.ui.cbo_thanhtoan.setCurrentText(order["payment"])  # Thanh toán
            self.ui.txt_note.setPlainText(order["note"])  # Ghi chú

            # Thiết lập cbo_nvxl theo tên nhân viên
            employee_index = self.ui.cbo_nvxl.findText(order["employee_name"])
            if employee_index != -1:
                self.ui.cbo_nvxl.setCurrentIndex(employee_index)
        else:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy đơn hàng!")

    def update_order(self):
        """Cập nhật đơn hàng vào CSDL"""
        # Lấy trạng thái đơn hàng hiện tại
        old_status = self.db.get_order_status(self.order_code)

        # Kiểm tra nếu đơn hàng đã hoàn thành hoặc đã hủy
        if old_status in ["Đã hủy", "Hoàn thành"]:
            QMessageBox.warning(self, "Lỗi", "Không thể cập nhật đơn hàng đã hoàn thành hoặc bị hủy!")
            return

        customer_code = self.ui.txt_maKH.toPlainText().strip()
        employee_name = self.ui.cbo_nvxl.currentText()
        total_amount = self.ui.txt_tongtien.toPlainText().strip()
        status = self.ui.cbo_trangthai.currentText()
        payment = self.ui.cbo_thanhtoan.currentText()
        note = self.ui.txt_note.toPlainText().strip()

        if not customer_code or not total_amount:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        try:
            total_amount = float(total_amount)
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Tổng tiền phải là số!")
            return

        success = self.db.update_order(
            self.order_code, employee_name, total_amount, status, payment, note
    )

        if success:
            QMessageBox.information(self, "Thành công", "Cập nhật đơn hàng thành công!")

            # Nếu trạng thái thay đổi thành "Đã hủy" → Hoàn số lượng sản phẩm
            if status == "Đã hủy" and old_status != "Đã hủy":
                self.db.restore_order_products(self.order_code)

            self.close()
        else:
            QMessageBox.critical(self, "Lỗi", "Cập nhật đơn hàng thất bại!")


    def show_themCT(self):
        """Mở cửa sổ thêm chi tiết đơn hàng"""
        from Donhang.themCT import ThemChiTiet # Import giao diện thêm chi tiết đơn hàng

        self.themCT_window = ThemChiTiet(self.order_code)  # Truyền mã đơn hàng vào
        self.themCT_window.show()
