from PyQt6.QtWidgets import QMessageBox, QHeaderView
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6 import QtWidgets
from Donhang.ui_themCT import Ui_Form
from SQL_database.csdl_DH import OrderDatabase

class ThemChiTiet(QtWidgets.QMainWindow):
    def __init__(self, order_code):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = OrderDatabase()
        self.order_code = order_code  # Lưu ID đơn hàng

        self.ui.txt_maDH.setText(str(order_code))
        self.model = QStandardItemModel()  # Model cho QTableView
        self.ui.tb_CTDH.setModel(self.model)

        self.load_products()
        self.load_order_details()  # Load chi tiết đơn hàng vào bảng
        self.load_payment_methods()
        self.load_statuses()
        self.calculate_total_price()


    

        self.ui.btn_them.clicked.connect(self.add_order_details)

    def load_products(self):
        """Tải danh sách sản phẩm từ CSDL vào ComboBox"""
        products = self.db.get_product_list()
        self.ui.cbo_tenSP.clear()
        for product_id, product_name in products:
            self.ui.cbo_tenSP.addItem(product_name, product_id)

    def load_statuses(self):
        """Tải danh sách trạng thái đơn hàng vào ComboBox"""
        statuses = self.db.get_statuses()
        self.ui.cbo_trangthai.clear()
        for status in statuses:
            self.ui.cbo_trangthai.addItem(status)
      

    def load_payment_methods(self):
        """Tải danh sách phương thức thanh toán vào ComboBox"""
        payment_methods = self.db.get_payment_methods()
        self.ui.cbo_thanhtoan.clear()
        for method in payment_methods:
            self.ui.cbo_thanhtoan.addItem(method)


    def load_order_details(self):
        """Lấy chi tiết đơn hàng từ CSDL và hiển thị trên QTableView"""
        columns = ["Mã Đơn Hàng", "Sản Phẩm", "Số Lượng", "Đơn Giá", "Tổng Tiền", "Trạng Thái", "Thanh Toán"]
        self.model.setColumnCount(len(columns))
        self.model.setHorizontalHeaderLabels(columns)

        details = self.db.get_order_details(self.order_code)  # Lấy danh sách chi tiết đơn hàng

        if details:  # Nếu có dữ liệu
            self.model.setRowCount(len(details))  # Đặt số hàng
            for row_idx, detail in enumerate(details):
                # Thêm mã đơn hàng vào cột đầu tiên
                item_order_id = QStandardItem(str(self.order_code))
                item_order_id.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.model.setItem(row_idx, 0, item_order_id)

                # Điền dữ liệu còn lại vào các cột
                for col_idx, value in enumerate(detail):
                    item = QStandardItem(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.model.setItem(row_idx, col_idx + 1, item)  # +1 vì cột đầu tiên là mã đơn hàng
        

        # Tự động co giãn cột
        self.ui.tb_CTDH.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def add_order_details(self):
        """Thêm chi tiết đơn hàng và cập nhật bảng"""
        # 🔹 Lấy trạng thái đơn hàng từ CSDL
        current_status = self.db.get_order_status(self.order_code)
    
    # 🚫 Chặn thêm sản phẩm nếu đơn hàng đã "Đã hủy" hoặc "Đã giao"
        if current_status in ["Đã hủy", "Đã giao"]:
            QMessageBox.warning(self, "Lỗi", f"Không thể thêm sản phẩm! Đơn hàng đang ở trạng thái '{current_status}'")
            self.clear_input_fields()  # 🧹 Xóa dữ liệu nhập sau khi thêm
            return

        product_id = self.ui.cbo_tenSP.currentData()
        quantity = self.ui.txt_soluong.toPlainText().strip()
        unit_price = self.ui.txt_dongia.toPlainText().strip()
        note = self.ui.txt_note.toPlainText().strip()

    # 🔹 Lấy trạng thái & thanh toán từ ComboBox
        status = self.ui.cbo_trangthai.currentText()
        payment = self.ui.cbo_thanhtoan.currentText()

        if not product_id or not quantity or not unit_price:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        try:
            quantity = int(quantity)
            unit_price = float(unit_price)
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Số lượng và đơn giá phải là số!")
            return

    # 🔹 Gửi tất cả dữ liệu vào CSDL (gồm trạng thái & thanh toán)
        success = self.db.add_order_detail(self.order_code, product_id, quantity, unit_price, status, payment, note)

        if success:
            QMessageBox.information(self, "Thành công", "Chi tiết đơn hàng đã được thêm!")
            self.load_order_details()  # 🔥 Load lại bảng sau khi thêm
            self.calculate_total_price()  # 💰 TÍNH LẠI TỔNG TIỀN
            self.clear_input_fields()  # 🧹 Xóa dữ liệu nhập sau khi thêm

        else:
            QMessageBox.warning(self, "Lỗi", "Không thể thêm chi tiết đơn hàng!")



    def clear_input_fields(self):
        """Xóa dữ liệu nhập sau khi thêm thành công"""
        self.ui.txt_soluong.clear()  # Xóa số lượng
        self.ui.txt_dongia.clear()  # Xóa đơn giá
        self.ui.txt_note.clear()  # Xóa ghi chú

        self.ui.cbo_tenSP.setCurrentIndex(0)  # Chọn lại sản phẩm đầu tiên
        self.ui.cbo_trangthai.setCurrentIndex(0)  # Chọn lại trạng thái đầu tiên
        self.ui.cbo_thanhtoan.setCurrentIndex(0)  # Chọn lại thanh toán đầu tiên

    def calculate_total_price(self):
        """Tính tổng tiền của tất cả các chi tiết đơn hàng"""
        total = 0
        for row in range(self.model.rowCount()):
            try:
                total_price = float(self.model.item(row, 4).text().replace(',', ''))
                total += total_price
            except ValueError:
                continue  # Nếu có lỗi, bỏ qua hàng này

        self.ui.txt_tongtien.setText(f"{total:,.2f}")

