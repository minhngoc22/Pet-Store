from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from SQL_database.csdl_DH import OrderDatabase
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from Donhang.ui_themCT import Ui_Form

class ThemChiTiet(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # 🛠 Gọi constructor của lớp cha trước
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = OrderDatabase()
        self.customer_id = None  # Lưu ID khách hàng sau khi tìm kiếm

        # Gán sự kiện
       # self.ui.btn_them.clicked.connect(self.create_order)

       


  


    



