from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from SQL_database.csdl_DH import OrderDatabase
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from Donhang.ui_themCT import Ui_Form

class ThemChiTiet(QtWidgets.QMainWindow):
    def __init__(self,order_id):
        super().__init__()  # 🛠 Gọi constructor của lớp cha trước
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = OrderDatabase()
        self.order_id = order_id # Lưu ID khách hàng sau khi tìm kiếm

        self.ui.txt_maDH.setText(str(order_id)) 
        # 🔥 Load danh sách sản phẩm vào combo box
        self.load_products()
          # Gán sự kiện cho nút thêm chi tiết đơn hàng
        self.ui.btn_them.clicked.connect(self.add_order_details)
        

    def load_products(self):
        """Tải danh sách sản phẩm từ CSDL vào ComboBox"""

        products = self.db.get_product_list()
        self.ui.cbo_tenSP.clear()  # Xóa dữ liệu cũ
        for product_id, product_name in products:
            self.ui.cbo_tenSP.addItem(product_name, product_id)  # Lưu product_code vào userData
            
    def add_order_details(self):
        """Thêm chi tiết đơn hàng"""
        
        product_id = self.ui.cbo_tenSP.currentData()
        quantity = self.ui.txt_soluong.toPlainText().strip()
        unit_price = self.ui.txt_dongia.toPlainText().strip()
        note = self.ui.txt_note.toPlainText().strip()

        
        if not product_id or not quantity or not unit_price:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin sản phẩm!")
            return

        try:
            quantity = int(quantity)
            unit_price = float(unit_price)
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Số lượng và đơn giá phải là số!")
            return

        # 👉 Thêm chi tiết đơn hàng vào CSDL
        success = self.db.add_order_detail(self.order_id, product_id, quantity, unit_price, note)

        if success:
            QMessageBox.information(self, "Thành công", "Chi tiết đơn hàng đã được thêm!")
        else:
            QMessageBox.warning(self, "Lỗi", "Không thể thêm chi tiết đơn hàng!")
        self.close()

    

       


  


    



