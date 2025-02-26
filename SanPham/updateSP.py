from PyQt6.QtWidgets import QWidget, QMessageBox, QFileDialog
from PyQt6.QtGui import QPixmap
from SanPham.ui_updateSP import Ui_updateSanPham
from PyQt6.QtWidgets import QMainWindow

class EditProductWindow(QMainWindow, Ui_updateSanPham):
    def __init__(self, product_id, db, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.product_id = product_id
        self.db = db
        self.image_path = None  # Đường dẫn ảnh sản phẩm

        # Nạp dữ liệu
        self.load_categories_and_suppliers()
        self.load_product_data()

        # Kết nối sự kiện
        self.btn_luusp.clicked.connect(self.save_changes)
        self.btn_chon_anh.clicked.connect(self.select_image)

    def load_categories_and_suppliers(self):
        self.cbo_danhmucSP.clear()
        self.cbo_danhmucNCC.clear()

        categories = self.db.get_all_categories() or ["Chưa có danh mục"]
        suppliers = self.db.get_all_suppliers() or []

        self.cbo_danhmucSP.addItems(categories)
        self.cbo_danhmucNCC.addItems(suppliers)

    def load_product_data(self):
        product = self.db.get_product_by_id(self.product_id)
        if product:
            self.txt_maSP.setText(str(product["id"]))
            self.txt_tenSP.setText(product["product_name"])
            self.txt_giaSP.setText(str(product["price"]))
            self.txt_soluongP.setText(str(product["stock_quantity"]))
            self.txt_note.setText(product["note"])

            index_category = self.cbo_danhmucSP.findText(product["category"])
            if index_category != -1:
                self.cbo_danhmucSP.setCurrentIndex(index_category)

            index_supplier = self.cbo_danhmucNCC.findText(product["supplier"])
            if index_supplier != -1:
                self.cbo_danhmucNCC.setCurrentIndex(index_supplier)

            if product.get("image_path"):
                self.image_path = product["image_path"]
                pixmap = QPixmap(self.image_path)
                self.lbl_anh.setPixmap(pixmap.scaled(self.lbl_anh.size()))

    def save_changes(self):
        new_name = self.txt_tenSP.toPlainText().strip()
        new_category = self.cbo_danhmucSP.currentText().strip()
        new_price = self.txt_giaSP.toPlainText().strip()
        new_stock = self.txt_soluongP.toPlainText().strip()
        new_supplier = self.cbo_danhmucNCC.currentText().strip()
        new_note = self.txt_note.toPlainText().strip()

        if not new_name or not new_price or not new_stock:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        try:
            new_price = float(new_price)
            new_stock = int(new_stock)
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Giá bán phải là số thực và số lượng phải là số nguyên!")
            return

        success = self.db.update_product(
            self.product_id, new_name, new_category, new_price, new_stock, new_supplier, self.image_path, new_note
        )

        if success:
            QMessageBox.information(self, "Thành công", "Cập nhật sản phẩm thành công!")
            self.close()  # Đóng cửa sổ sau khi cập nhật
        else:
            QMessageBox.critical(self, "Lỗi", "Cập nhật sản phẩm thất bại!")

    def select_image(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "Chọn ảnh", "", "Images (*.png *.xpm *.jpg *.jpeg)")
        if image_path:
            self.image_path = image_path
            pixmap = QPixmap(self.image_path)
            self.lbl_anh.setPixmap(pixmap.scaled(self.lbl_anh.size()))
