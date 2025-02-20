import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QMessageBox
from UIPython.ui_themSP import Ui_Form  # Đảm bảo file tồn tại
from ketnoiSQL import Database  # Đảm bảo file tồn tại

class EventHandler(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()  # Tạo UI ngay trong constructor
        self.ui.setupUi(self)
        self.image_path = None  # Biến lưu đường dẫn ảnh
        self.db = Database()  # Kết nối CSDL qua lớp Database

        # Kết nối sự kiện
        self.ui.btn_chon_anh.clicked.connect(self.choose_image)
        self.ui.cbo_danhmucNCC.currentIndexChanged.connect(self.display_selected_supplier)
        self.load_suppliers()
        self.ui.btn_them.clicked.connect(self.add_product)

    def choose_image(self):
        """Chọn ảnh từ máy tính và hiển thị lên QLabel"""
        from PyQt6.QtWidgets import QFileDialog
        from PyQt6.QtGui import QPixmap
        from PyQt6 import QtCore

        file_path, _ = QFileDialog.getOpenFileName(None, "Chọn ảnh sản phẩm", "", "Images (*.png *.jpg *.jpeg)")
        if file_path and file_path.strip():
            self.image_path = file_path
            pixmap = QPixmap(file_path).scaled(241, 171, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.ui.lbl_anh.setPixmap(pixmap)

    def load_suppliers(self):
        """Tải danh sách nhà cung cấp vào ComboBox"""
        self.ui.cbo_danhmucNCC.clear()
        suppliers = self.db.execute_query("SELECT supplier_name FROM Suppliers")
        for supplier in suppliers:
            self.ui.cbo_danhmucNCC.addItem(supplier[0])

    def display_selected_supplier(self):
        """Hiển thị tên nhà cung cấp đã chọn"""
        supplier_name = self.ui.cbo_danhmucNCC.currentText()
        print(f"Nhà cung cấp đã chọn: {supplier_name}")


    def add_product(self):
        """Xử lý sự kiện thêm sản phẩm"""
        id = self.ui.txt_maSP.toPlainText().strip()
        name = self.ui.txt_tenSP.toPlainText().strip()
        category = self.ui.cbo_danhmucSP.currentText()
        price = self.ui.txt_giaSP.toPlainText().strip()
        stock_quantity = self.ui.txt_soluongP.toPlainText().strip()
        supplier = self.ui.cbo_danhmucNCC.currentText()
        image_path = self.image_path if self.image_path else ""  # Đường dẫn ảnh

        if not name or not price or not category or not supplier:
            QMessageBox.warning(None, "Lỗi", "Vui lòng nhập đầy đủ thông tin sản phẩm!")
            return

        try:
            price = float(price)  # Đảm bảo giá sản phẩm là số
            self.db.add_product(id,name, category, price,stock_quantity, supplier, image_path)
            QMessageBox.information(None, "Thành công", "Sản phẩm đã được thêm vào!")
            self.clear_fields()
        except ValueError:
            QMessageBox.warning(None, "Lỗi", "Giá sản phẩm phải là số hợp lệ!")

    def clear_fields(self):
        """Xóa dữ liệu trong form sau khi thêm thành công"""
        self.ui.txt_tenSP.clear()
        self.ui.txt_giaSP.clear()
        self.ui.cbo_danhmucNCC.setCurrentIndex(0)
        self.ui.cbo_danhmucNCC.setCurrentIndex(0)
        self.ui.lbl_anh.clear()
        self.image_path = None

if __name__ == "__main__":
    print("🔵 [START] Chạy giao diện thêm sản phẩm...")
    
    app = QApplication(sys.argv)
    window = QWidget()
    ui = Ui_Form()
    ui.setupUi(window)

    handler = EventHandler(ui)  # Tạo đối tượng xử lý sự kiện

    window.show()
    print("🟢 [RUNNING] Giao diện đang chạy...")
    sys.exit(app.exec())
