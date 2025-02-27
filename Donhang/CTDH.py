import sys
from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QApplication, QHeaderView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt
from SQL_database.csdl_CTDH import CTDHDatabase
from Donhang.ui_CTDH import Ui_Form

class ChiTietDonHang(QWidget):  # ✅ Sửa lại kế thừa từ QWidget
    def __init__(self, order_id):
        super().__init__()
        self.ui = Ui_Form()  
        self.ui.setupUi(self)
        self.db = CTDHDatabase()
        self.order_id = order_id

        # ✅ Khởi tạo model bảng
        self.model = QStandardItemModel()
        self.ui.tb_CTDH.setModel(self.model)

        # ✅ Load dữ liệu đơn hàng
        self.load_order_details()

    def load_order_details(self):
        """Lấy chi tiết đơn hàng từ CSDL và hiển thị trên bảng"""
        columns = ["Mã ĐH", "Mã KH", "Tên KH", "Sản Phẩm", "Số Lượng", "Tổng Tiền", "Trạng Thái", "Thanh Toán", "Ghi chú"]
        self.model.setColumnCount(len(columns))
        self.model.setHorizontalHeaderLabels(columns)

        order_details = self.db.get_order_by_code(self.order_id)  # Lấy danh sách sản phẩm

        if order_details:  # Nếu có dữ liệu
            self.model.setRowCount(len(order_details))  # Đặt số hàng = số sản phẩm
            for row_idx, order in enumerate(order_details):
                for col_idx, key in enumerate(columns):
                    item = QStandardItem(str(order[key]))  # Lấy giá trị từ dict
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.model.setItem(row_idx, col_idx, item)  # Gán vào bảng
        else:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy thông tin đơn hàng!")

        self.ui.tb_CTDH.setModel(self.model)
        self.ui.tb_CTDH.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChiTietDonHang(order_id="DH001")  # ✅ Truyền mã đơn hàng hợp lệ
    window.show()
    sys.exit(app.exec())
