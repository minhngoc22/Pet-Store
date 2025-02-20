import sys
import os
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from UIPython.ui_mainwindow import Ui_UIMainWindow
from SQL_database.csdl_sp import ProductDatabase

class MainWindowMain(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_UIMainWindow()
        self.ui.setupUi(self)

        # 🔗 Kết nối SQLite
        self.db = ProductDatabase()
        if not self.db.connect():
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối CSDL!")
            return  # Dừng nếu không kết nối được

        # Nạp dữ liệu vào bảng sản phẩm
        self.load_data()

        # 🔗 Kết nối các nút bấm với trang tương ứng
        self.ui.Menu.setCurrentIndex(0)  # Trang chủ là trang đầu tiên
        self.ui.btn_home.clicked.connect(self.trangchu)
        self.ui.btn_spham.clicked.connect(self.sanpham)
        self.ui.btn_nhanvien.clicked.connect(self.nhanvien)
        self.ui.btn_donhang.clicked.connect(self.donhang)
        self.ui.btn_khachhang.clicked.connect(self.khachhang)
        self.ui.btn_logout.clicked.connect(self.logout)
        self.ui.btn_refresh.clicked.connect(self.refresh_data)
        self.ui.btn_themsp.clicked.connect(self.show_themsp)
        self.ui.btn_xoasp.clicked.connect(self.delete_product)
        self.ui.cbo_sp.currentIndexChanged.connect(self.filter_products)

        self.load_categories()

    def trangchu(self):
        """Chuyển về trang chủ"""
        self.ui.Menu.setCurrentIndex(0)

    def sanpham(self):
        """Chuyển về trang sản phẩm"""
        self.ui.Menu.setCurrentIndex(1)

    def nhanvien(self):
        """Chuyển về trang nhân viên"""
        self.ui.Menu.setCurrentIndex(2)

    def donhang(self):
        """Chuyển về trang đơn hàng"""
        self.ui.Menu.setCurrentIndex(3)

    def khachhang(self):
        """Chuyển về trang khách hàng"""
        self.ui.Menu.setCurrentIndex(4)

    def logout(self):
        """Xử lý đăng xuất"""
        reply = QMessageBox.question(
            self, "Xác nhận", "Bạn có chắc chắn muốn đăng xuất?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            print("🔴 [LOGOUT] Đăng xuất thành công!")
            self.close()  # Đóng cửa sổ chính
            self.show_login()

    def load_data(self):
        """Nạp toàn bộ dữ liệu từ bảng Products lên QTableView"""
        columns, products = self.db.get_all_products()

        if not products:
            return  # Không có dữ liệu, thoát sớm

        # 📌 Đổi tên cột hiển thị
        column_names = {
            "id": "ID",
            "product_name": "Tên Sản Phẩm",
            "category": "Danh Mục",
            "price": "Giá Bán",
            "stock_quantity": "Số Lượng",
            "supplier": "Nhà Cung Cấp",
            "image_path": "Ảnh"
        }
        displayed_headers = [column_names.get(col, col) for col in columns]

        # 📌 Sử dụng QStandardItemModel để hiển thị dữ liệu
        model = QStandardItemModel(len(products), len(columns))
        model.setHorizontalHeaderLabels(displayed_headers)  # Đặt tên cột

        # 📌 Thêm dữ liệu vào model
        for row_idx, row_data in enumerate(products):
            for col_idx, value in enumerate(row_data):
                item = QStandardItem()

                if columns[col_idx] == "image_path" and value:  # Nếu cột là ảnh
                    if os.path.exists(value):  # Kiểm tra file có tồn tại không
                        pixmap = QPixmap(value).scaled(60, 60, Qt.AspectRatioMode.KeepAspectRatio)
                        icon = QIcon(pixmap)
                        item.setIcon(icon)  # Đặt icon cho ô
                    else:
                        item.setText("Không có ảnh")
                else:
                    item.setText(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Căn giữa

                model.setItem(row_idx, col_idx, item)

        # Gán model cho QTableView
        self.ui.tb_sanpham.setModel(model)

        # 🔹 Tự động điều chỉnh kích thước cột
        self.ui.tb_sanpham.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    def show_login(self):
        """Hiển thị màn hình đăng nhập"""
        from dangnhap import Login  # Import bên trong hàm để tránh vòng lặp import
        self.login_window = Login()
        self.login_window.show()
        self.close()  # Đóng cửa sổ chính

    def show_themsp(self):
        from themSP import EventHandler
        self.themsp_window = EventHandler()
        self.themsp_window.show()

    def delete_product(self):
        """Xóa sản phẩm được chọn"""
        selected_indexes = self.ui.tb_sanpham.selectionModel().selectedRows()

        if not selected_indexes:
            QMessageBox.warning(self, "Chú ý", "Vui lòng chọn một sản phẩm để xóa.")
            return

        # Lấy ID của sản phẩm từ dòng được chọn
        selected_row = selected_indexes[0].row()  # Lấy chỉ số dòng đầu tiên được chọn
        model = self.ui.tb_sanpham.model()
        product_id = model.item(selected_row, 0).text()  # Cột 0 chứa ID

        # Xác nhận trước khi xóa
        reply = QMessageBox.question(
            self, "Xác nhận", f"Bạn có chắc chắn muốn xóa sản phẩm ID {product_id}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
    )

        if reply == QMessageBox.StandardButton.Yes:
            # Xóa sản phẩm khỏi CSDL
            if self.db.delete_product(product_id):
                QMessageBox.information(self, "Thành công", "Sản phẩm đã được xóa.")
                self.load_data()  # Cập nhật lại bảng
            else:
                QMessageBox.critical(self, "Lỗi", "Xóa sản phẩm thất bại!")
        
    def load_categories(self):
        """Tải danh sách danh mục từ SQLite và hiển thị trên ComboBox."""
        conn = self.db.connect()
        if conn is None:  # Kiểm tra nếu kết nối thất bại
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối CSDL!")
            return

        cursor = conn.cursor()  
        cursor.execute("SELECT DISTINCT category FROM Products")
        categories = cursor.fetchall()
    
        self.ui.cbo_sp.clear()
        self.ui.cbo_sp.addItem("Tất cả")
        for category in categories:
            self.ui.cbo_sp.addItem(category[0])

        conn.close()


    def filter_products(self):
        """Lọc sản phẩm theo danh mục được chọn và hiển thị hình ảnh."""
        selected_category = self.ui.cbo_sp.currentText()

        conn = self.db.connect()
        if conn is None:
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối CSDL!")
            return

        cursor = conn.cursor()

        query = """
            SELECT id, product_name, category, price, stock_quantity, supplier, image_path
            FROM Products
    """

        if selected_category != "Tất cả":
            query += " WHERE category = ?"
            cursor.execute(query, (selected_category,))
        else:
            cursor.execute(query)

        products = cursor.fetchall()
        conn.close()

        self.update_table(products)  # Cập nhật lại bảng

    def update_table(self, products):
        """Cập nhật dữ liệu trong bảng sản phẩm và đảm bảo hiển thị hình ảnh"""
        model = QStandardItemModel(len(products), 7)  # 7 là số cột
        headers = ["ID", "Tên Sản Phẩm", "Danh Mục", "Giá Bán", "Số Lượng", "Nhà Cung Cấp", "Ảnh"]
        model.setHorizontalHeaderLabels(headers)

        for row_idx, row_data in enumerate(products):
            for col_idx, value in enumerate(row_data):
                item = QStandardItem()

                if col_idx == 6 and value:  # Cột 6 là cột chứa đường dẫn ảnh
                    if os.path.exists(value):
                        pixmap = QPixmap(value).scaled(60, 60, Qt.AspectRatioMode.KeepAspectRatio)
                        icon = QIcon(pixmap)
                        item.setIcon(icon)  # Hiển thị ảnh trong bảng
                    else:
                        item.setText("Không có ảnh")
                else:
                    item.setText(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Căn giữa

                model.setItem(row_idx, col_idx, item)

        self.ui.tb_sanpham.setModel(model)

    # 🔹 Tự động điều chỉnh kích thước cột
        self.ui.tb_sanpham.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)


    def refresh_data(self):
        """Làm mới bảng sản phẩm nhưng giữ nguyên danh mục đang chọn"""
        selected_category = self.ui.cbo_sp.currentText()

        if selected_category == "Tất cả":
            self.load_data()  # Nếu chọn "Tất cả", tải lại toàn bộ dữ liệu
        else:
            self.filter_products()  # Nếu đang lọc theo danh mục, chỉ cập nhật danh mục đó

    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowMain()
    window.show()
    sys.exit(app.exec())
