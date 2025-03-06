from PyQt6.QtWidgets import QMessageBox, QHeaderView
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6 import QtWidgets
from Donhang.ui_themCT import Ui_Form
from SQL_database.csdl_DH import OrderDatabase

class ThemChiTiet(QtWidgets.QMainWindow):
    def __init__(self, order_id):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = OrderDatabase()
        self.order_id = order_id  # Lưu ID đơn hàng

        self.ui.txt_maDH.setText(str(order_id))
        self.model = QStandardItemModel()  # Model cho QTableView
        self.ui.tb_CTDH.setModel(self.model)

        self.load_products()
        self.load_order_details()  # Load chi tiết đơn hàng vào bảng

        self.ui.btn_them.clicked.connect(self.add_order_details)

    def load_products(self):
        """Tải danh sách sản phẩm từ CSDL vào ComboBox"""
        products = self.db.get_product_list()
        self.ui.cbo_tenSP.clear()
        for product_id, product_name in products:
            self.ui.cbo_tenSP.addItem(product_name, product_id)

    def load_order_details(self):
        """Lấy chi tiết đơn hàng từ CSDL và hiển thị trên QTableView"""
        columns = ["Mã Đơn Hàng", "Sản Phẩm", "Số Lượng", "Đơn Giá", "Tổng Tiền", "Trạng Thái", "Thanh Toán"]
        self.model.setColumnCount(len(columns))
        self.model.setHorizontalHeaderLabels(columns)

        details = self.db.get_order_details(self.order_id)  # Lấy danh sách chi tiết đơn hàng

        if details:  # Nếu có dữ liệu
            self.model.setRowCount(len(details))  # Đặt số hàng
            for row_idx, detail in enumerate(details):
                # Thêm mã đơn hàng vào cột đầu tiên
                item_order_id = QStandardItem(str(self.order_id))
                item_order_id.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.model.setItem(row_idx, 0, item_order_id)

                # Điền dữ liệu còn lại vào các cột
                for col_idx, value in enumerate(detail):
                    item = QStandardItem(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.model.setItem(row_idx, col_idx + 1, item)  # +1 vì cột đầu tiên là mã đơn hàng
        else:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy thông tin đơn hàng!")

        # Tự động co giãn cột
        self.ui.tb_CTDH.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def add_order_details(self):
        """Thêm chi tiết đơn hàng và cập nhật bảng"""
        product_id = self.ui.cbo_tenSP.currentData()
        quantity = self.ui.txt_soluong.toPlainText().strip()  # Sử dụng text() nếu là QLineEdit
        unit_price = self.ui.txt_dongia.toPlainText().strip()
        note = self.ui.txt_note.toPlainText().strip()

        if not product_id or not quantity or not unit_price:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        try:
            quantity = int(quantity)
            unit_price = float(unit_price)
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Số lượng và đơn giá phải là số!")
            return

        success = self.db.add_order_detail(self.order_id, product_id, quantity, unit_price, note)

        if success:
            QMessageBox.information(self, "Thành công", "Chi tiết đơn hàng đã được thêm!")
            self.load_order_details()  # 🔥 Load lại bảng sau khi thêm
        else:
            QMessageBox.warning(self, "Lỗi", "Không thể thêm chi tiết đơn hàng!")
