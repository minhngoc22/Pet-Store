
import sys
import os
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QIcon, QPixmap
from PyQt6.QtCore import Qt
from Main.ui_mainwindow import Ui_UIMainWindow
from SQL_database.csdl_sp import ProductDatabase

class Sanpham:
    def __init__(self, ui):
        self.ui = ui
        self.model = QStandardItemModel()
        self.ui.tb_sanpham.setModel(self.model)
        
        self.db = ProductDatabase()
        if not self.db.connect():
            QMessageBox.critical(None, "Lỗi", "Không thể kết nối CSDL!")
            return
        
        self.load_and_update_table()
        
        self.ui.btn_refresh.clicked.connect(self.refresh_data)
        self.ui.btn_themsp.clicked.connect(self.show_themsp)
        self.ui.btn_xoasp.clicked.connect(self.delete_product)
        self.ui.btn_suasp.clicked.connect(self.edit_product)
        self.ui.btn_timkiemsp.clicked.connect(self.search)
        self.ui.cbo_sp.currentIndexChanged.connect(self.filter_products)
        
        self.load_categories()
    
    def load_and_update_table(self, products=None):
        """Tải và cập nhật bảng sản phẩm"""
        if products is None:
            success, products = self.db.get_all_products()
            if not success:
                QMessageBox.critical(None, "Lỗi", "Không thể tải dữ liệu sản phẩm!")
                return
        else:
            success = True  # Đảm bảo 'success' luôn có giá trị

        print(f"⚡ Debug - Số sản phẩm sau khi tải lại: {len(products)}")  # Debug số lượng

        self.model.clear()

        column_names = ["ID", "Tên Sản Phẩm", "Danh Mục", "Giá Bán", "Số Lượng", "Nhà Cung Cấp", "Ảnh","Ghi chú"]
        self.model.setColumnCount(len(column_names))  # ✅ Đặt số cột chính xác
        self.model.setHorizontalHeaderLabels(column_names)

        for row_idx, row_data in enumerate(products):
            for col_idx, value in enumerate(row_data):
                item = QStandardItem()
                if col_idx == 6 and value:  # Ảnh
                    if os.path.exists(value):
                        pixmap = QPixmap(value).scaled(60, 60, Qt.AspectRatioMode.KeepAspectRatio)
                        icon = QIcon(pixmap)
                        item.setIcon(icon)
                    else:
                        item.setText("Không có ảnh")
                else:
                    item.setText(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.model.setItem(row_idx, col_idx, item)

        self.ui.tb_sanpham.setModel(self.model)
        self.ui.tb_sanpham.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    
    
    def delete_product(self):
        selected_indexes = self.ui.tb_sanpham.selectionModel().selectedRows()
        if not selected_indexes:
            QMessageBox.warning(None, "Chú ý", "Vui lòng chọn một sản phẩm để xóa.")
            return
        
        selected_row = selected_indexes[0].row()
        product_id = self.model.item(selected_row, 0).text()
        
        reply = QMessageBox.question(None, "Xác nhận", f"Bạn có chắc chắn muốn xóa sản phẩm ID {product_id}?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            if self.db.delete_product(product_id):
                QMessageBox.information(None, "Thành công", "Sản phẩm đã được xóa.")
                self.refresh_data()
            else:
                QMessageBox.critical(None, "Lỗi", "Xóa sản phẩm thất bại!")




    def show_themsp(self):
        from SanPham.themSP import EventHandler
        self.themsp_window = EventHandler()
        self.themsp_window.show()

    def delete_product(self):
        """Xóa sản phẩm được chọn khỏi CSDL"""
        selected_indexes = self.ui.tb_sanpham.selectionModel().selectedRows()
        if not selected_indexes:
            QMessageBox.warning(None, "Chú ý", "Vui lòng chọn một sản phẩm để xóa.")
            return

        selected_row = selected_indexes[0].row()
        product_id = self.model.item(selected_row, 0).text().strip()  # Lấy ID sản phẩm

        reply = QMessageBox.question(
            None, "Xác nhận", f"Bạn có chắc chắn muốn xóa sản phẩm ID: {product_id}?",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        QMessageBox.StandardButton.No
    )

        if reply == QMessageBox.StandardButton.Yes:
            if self.db.delete_product(product_id):  # Gọi hàm xóa trong CSDL
                QMessageBox.information(None, "Thành công", "Sản phẩm đã được xóa.")
                self.refresh_data()  # Làm mới bảng sau khi xóa
            else:   
                QMessageBox.critical(None, "Lỗi", "Xóa sản phẩm thất bại! Có thể ID không tồn tại.")

        
    def load_categories(self):
        """Tải danh sách danh mục từ SQLite và hiển thị trên ComboBox."""
        conn = self.db.connect()
        if conn is None:  # Kiểm tra nếu kết nối thất bại
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối CSDL!")
            return

        cursor = conn.cursor()  
        cursor.execute("SELECT category_name FROM Categories")
        categories = cursor.fetchall()
    
        self.ui.cbo_sp.clear()
        self.ui.cbo_sp.addItem("Tất cả")
        for category in categories:
            self.ui.cbo_sp.addItem(category[0])

        conn.close()



    def filter_products(self):
        """Lọc sản phẩm theo danh mục được chọn"""
        selected_category = self.ui.cbo_sp.currentText()
        print(f"⚡ Debug - Lọc sản phẩm theo danh mục: {selected_category}")  # Debug

        products = self.db.get_products_by_category(selected_category)  # Giả sử có hàm này trong CSDL
        print(f"⚡ Debug - Số sản phẩm tìm thấy: {len(products)}")  # Debug

        self.load_and_update_table(products)


    

    # 🔹 Tự động điều chỉnh kích thước cột
        self.ui.tb_sanpham.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)


    def refresh_data(self):
        """Làm mới dữ liệu bảng sản phẩm"""
        self.load_and_update_table()
        self.load_categories()  # Làm mới ComboBox danh mục

    

    def edit_product(self):
        """Sửa thông tin sản phẩm được chọn"""
        selected_indexes = self.ui.tb_sanpham.selectionModel().selectedRows()

        if not selected_indexes:
            QMessageBox.warning(None, "Chú ý", "Vui lòng chọn một sản phẩm để sửa.")
            return

        # Lấy ID của sản phẩm từ dòng được chọn
        selected_row = selected_indexes[0].row()
        model = self.ui.tb_sanpham.model()
        product_id = model.item(selected_row, 0).text()  # Cột 0 chứa ID

        from SanPham.updateSP import EditProductWindow  # Import lớp giao diện sửa sản phẩm
        self.sua_sp_window = EditProductWindow(product_id, self.db)
        self.sua_sp_window.show()
        self.load_and_update_table()  # Cập nhật bảng sau khi đóng cửa sổ





    def search(self):
        search_text = self.ui.txt_timkimsp.toPlainText().strip()  # Lấy từ khóa tìm kiếm

        if not search_text:
            self.load_data()  # Nếu ô tìm kiếm trống, nạp lại toàn bộ dữ liệu
            return

        products = self.db.search_product_by_name(search_text)

        # Xóa dữ liệu cũ trước khi cập nhật kết quả mới
        self.model.clear()

    # Đặt lại tiêu đề cột
        headers = ["ID", "Tên Sản Phẩm", "Danh Mục", "Giá Bán", "Số Lượng", "Nhà Cung Cấp", "Ảnh"]
        self.model.setHorizontalHeaderLabels(headers)

        if products:
            for product in products:
                row_data = [
                QStandardItem(str(product["id"])),
                QStandardItem(product["product_name"]),
                QStandardItem(product["category_name"]),
                QStandardItem(str(product["price"])),
                QStandardItem(str(product["stock_quantity"])),
                QStandardItem(product["supplier"])
            ]

            # Hiển thị ảnh sản phẩm
                image_item = QStandardItem()
                image_path = product["image_path"]
                if image_path and os.path.exists(image_path):
                    pixmap = QPixmap(image_path).scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio)  
                    icon = QIcon(pixmap)
                    image_item.setIcon(icon)
                else:
                    image_item.setText("Không có ảnh")

                row_data.append(image_item)

                self.model.appendRow(row_data)
        else:
            QMessageBox.information(self, "Kết quả", "Không tìm thấy sản phẩm nào phù hợp!")

    # Gán lại model cho bảng
        self.ui.tb_sanpham.setModel(self.model)

    # Căn chỉnh cột tự động
        self.ui.tb_sanpham.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Sanpham()
    window.show()
    sys.exit(app.exec())

    


