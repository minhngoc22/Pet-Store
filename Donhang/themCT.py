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

       
        self.load_order_details()  # Load chi tiết đơn hàng vào bảng
        self.calculate_total_price()


       # 🔹 Bắt sự kiện khi nhập mã sản phẩm
        self.ui.txt_masp.textChanged.connect(self.load_product_info)

        self.ui.btn_them.clicked.connect(self.add_order_details)

   
    def load_product_info(self):
        """Khi nhập mã sản phẩm, tự động hiển thị tên sản phẩm và đơn giá"""
        product_id = self.ui.txt_masp.toPlainText().strip()
        if not product_id:
            self.ui.txt_tensp.clear()
            self.ui.txt_dongia.clear()
            return

        product_info = self.db.get_product_by_code(product_id)
        if product_info:
            self.ui.txt_tensp.setText(product_info["product_name"])  # Hiển thị tên sản phẩm
            self.ui.txt_dongia.setText(str(product_info["price"]))  # Hiển thị đơn giá
        else:
            self.ui.txt_tensp.clear()
            self.ui.txt_dongia.clear()

    def load_order_details(self):
        """Lấy chi tiết đơn hàng từ CSDL và hiển thị trên QTableView"""
        columns = ["Mã Đơn Hàng","Mã Sản Phẩm" "Tên Sản Phẩm", "Số Lượng", "Đơn Giá", "Tổng Tiền", "Ghi Chú"]
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

    # 🚫 Chặn thêm sản phẩm nếu đơn hàng đã "Đã hủy", "Đã giao" hoặc "Hoàn thành"
        if current_status in ["Đã hủy", "Đã giao", "Hoàn thành"]:
            QMessageBox.warning(self, "Lỗi", f"Không thể thêm sản phẩm! Đơn hàng đang ở trạng thái '{current_status}'")
            self.clear_input_fields()
            return

    # 🔹 Lấy dữ liệu từ giao diện
        product_id = self.ui.txt_masp.toPlainText().strip()
        quantity_text = self.ui.txt_soluong.toPlainText().strip()
        unit_price_text = self.ui.txt_dongia.toPlainText().strip()
        note = self.ui.txt_note.toPlainText().strip()

        # 🚨 Kiểm tra dữ liệu nhập
        if not product_id or not quantity_text or not unit_price_text:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        # 🔹 Kiểm tra số lượng và đơn giá
        try:
            quantity = int(quantity_text)
            unit_price = float(unit_price_text)
            if quantity <= 0 or unit_price <= 0:
                QMessageBox.warning(self, "Lỗi", "Số lượng và đơn giá phải lớn hơn 0!")
                return
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Số lượng và đơn giá phải là số hợp lệ!")
            return

    # 🔹 Kiểm tra xem sản phẩm có tồn tại không
        product_info = self.db.get_product_by_code(product_id)
        if not product_info:
            QMessageBox.warning(self, "Lỗi", "Mã sản phẩm không tồn tại!")
            return

    # 🔹 Tính tổng tiền
        total_price = quantity * unit_price

    # 🔹 Thêm dữ liệu vào CSDL
        success = self.db.add_order_detail(
            order_code=self.order_code,
            product_id=product_id,
            quantity=quantity,
            unit_price=unit_price,  # ✅ Thêm tổng tiền
            note=note
    )

        if success:
            QMessageBox.information(self, "Thành công", "Chi tiết đơn hàng đã được thêm!")
            self.load_order_details()  # 🔥 Load lại bảng sau khi thêm
            self.calculate_total_price()  # 💰 Cập nhật tổng tiền
            self.clear_input_fields()  # 🧹 Xóa dữ liệu nhập
        else:
            QMessageBox.warning(self, "Lỗi", "Không thể thêm chi tiết đơn hàng!")




    def clear_input_fields(self):
        """Xóa dữ liệu nhập sau khi thêm thành công"""
        self.ui.txt_masp.clear()
        self.ui.txt_tensp.clear()  # Xóa tên sản phẩm
        self.ui.txt_soluong.clear()  # Xóa số lượng
        self.ui.txt_dongia.clear()  # Xóa đơn giá
        self.ui.txt_note.clear()  # Xóa ghi chú

    

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

