import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore
from SanPham.ui_themSP import Ui_themsanpham  # Đảm bảo file tồn tại
from SQL_database.csdl_sp import ProductDatabase  # Đảm bảo file tồn tại

class EventHandler(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_themsanpham()
        self.ui.setupUi(self)
        self.image_path = None  # Lưu đường dẫn ảnh
        self.db = ProductDatabase()  # Kết nối CSDL

        # Kết nối sự kiện
        self.ui.btn_chon_anh.clicked.connect(self.choose_image)
        self.ui.cbo_danhmucNCC.currentIndexChanged.connect(self.display_selected_supplier)
        self.ui.cbo_danhmucSP.currentIndexChanged.connect(self.display_selected_category)
        self.ui.btn_them.clicked.connect(self.add_product)

        self.load_suppliers()
        self.load_categories()

    def choose_image(self):
        """Chọn ảnh từ máy tính và hiển thị lên QLabel"""
        file_path, _ = QFileDialog.getOpenFileName(self, "Chọn ảnh sản phẩm", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.image_path = file_path
            pixmap = QPixmap(file_path).scaled(241, 171, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.ui.lbl_anh.setPixmap(pixmap)

    def load_suppliers(self):
        """Tải danh sách nhà cung cấp vào ComboBox"""
        self.ui.cbo_danhmucNCC.clear()
        suppliers = self.db.get_all_suppliers()  # Lấy từ CSDL
        self.ui.cbo_danhmucNCC.addItems(suppliers)

    def display_selected_supplier(self):
        """Hiển thị tên nhà cung cấp đã chọn"""
        supplier_name = self.ui.cbo_danhmucNCC.currentText()
        print(f"✅ Nhà cung cấp đã chọn: {supplier_name}")

    def load_categories(self):
        """Tải danh sách danh mục vào ComboBox"""
        self.ui.cbo_danhmucSP.clear()
        categories = self.db.get_all_categories()  # Lấy từ CSDL
        print("📌 Danh mục trong database:", categories)  # Kiểm tra danh mục
        self.ui.cbo_danhmucSP.addItems(categories)

    def display_selected_category(self):
        """Hiển thị danh mục đã chọn"""
        category_name = self.ui.cbo_danhmucSP.currentText()
        print(f"✅ Danh mục đã chọn: {category_name}")

    def add_product(self):
        """Xử lý sự kiện thêm sản phẩm"""
        id = self.ui.txt_maSP.toPlainText().strip()
        name = self.ui.txt_tenSP.toPlainText().strip()
        category_name = self.ui.cbo_danhmucSP.currentText().strip()
        supplier = self.ui.cbo_danhmucNCC.currentText().strip()
        price_text = self.ui.txt_giaSP.toPlainText().strip()
        stock_text = self.ui.txt_soluongP.toPlainText().strip()
        image_path = self.image_path if self.image_path else ""
        note = self.ui.txt_note.toPlainText().strip()

    # Kiểm tra dữ liệu nhập vào
        if not id or not name or not price_text or not stock_text or not category_name or not supplier:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin sản phẩm!")
            return

    # Kiểm tra giá và số lượng có hợp lệ không
        try:
            price = float(price_text)
            stock_quantity = int(stock_text)
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Giá và số lượng phải là số hợp lệ!")
            return

        # Lấy ID danh mục từ tên
        

        print(f"📌 Đang thêm sản phẩm: {name}, ID: {id}, Danh mục : {category_name}, NCC: {supplier}")

        # Thêm sản phẩm vào CSDL
        success = self.db.add_product(id, name, category_name, price, stock_quantity, supplier, image_path, note)
        if success:
            QMessageBox.information(self, "Thành công", "Sản phẩm đã được thêm vào!")
            self.clear_fields()
        else:
            QMessageBox.warning(self, "Lỗi", "Không thể thêm sản phẩm vào CSDL!")


    def clear_fields(self):
        """Xóa dữ liệu trong form sau khi thêm thành công"""
        self.ui.txt_maSP.clear()
        self.ui.txt_tenSP.clear()
        self.ui.txt_giaSP.clear()
        self.ui.txt_soluongP.clear()
        self.ui.cbo_danhmucSP.setCurrentIndex(0)
        self.ui.cbo_danhmucNCC.setCurrentIndex(0)
        self.ui.lbl_anh.clear()
        self.image_path = None
        self.ui.txt_note.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EventHandler()
    window.show()
    sys.exit(app.exec())
