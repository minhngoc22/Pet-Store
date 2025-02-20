from .ketnoiSQL import Database  
import sqlite3
import os

class ProductDatabase(Database):
    def get_all_products(self):
        """Lấy toàn bộ dữ liệu từ bảng Products."""
        conn = self.connect()
        if conn is None:
            return [], []

        try:
            cursor = conn.cursor()
            cursor.execute("PRAGMA table_info(Products);")
            columns = [col[1] for col in cursor.fetchall()]

            cursor.execute("SELECT * FROM Products")
            data = cursor.fetchall()

            return columns, data
        except sqlite3.Error as e:
            print("❌ Lỗi lấy dữ liệu từ bảng Products:", e)
            return [], []
        finally:
            conn.close()

    def add_product(self, id, product_name, category, price, stock_quantity, supplier, image_path):
        """Thêm sản phẩm mới vào bảng Products."""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Products (id, product_name, category, price, stock_quantity, supplier, image_path) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (id, product_name, category, price, stock_quantity, supplier, image_path))
        
            conn.commit()
            print(f"✅ Thêm sản phẩm '{product_name}' thành công!")
            return True
        except sqlite3.Error as e:
            print("❌ Lỗi khi thêm sản phẩm:", e)
            return False
        finally:
            conn.close()

    def delete_product(self, product_id):
        """Xóa sản phẩm theo ID."""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Products WHERE id = ?", (product_id,))
            conn.commit()
            print(f"🗑️ Xóa sản phẩm có ID {product_id} thành công!")
            return True
        except sqlite3.Error as e:
            print("❌ Lỗi khi xóa sản phẩm:", e)
            return False
        finally:
            conn.close()

    def update_product(self, product_id, product_name, category, price, stock_quantity, supplier):
        """Cập nhật thông tin sản phẩm."""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Products 
                SET product_name = ?, category = ?, price = ?, stock_quantity = ?, supplier = ?
                WHERE id = ?
            """, (product_name, category, price, stock_quantity, supplier, product_id))
            
            conn.commit()
            print(f"🔄 Cập nhật sản phẩm có ID {product_id} thành công!")
            return True
        except sqlite3.Error as e:
            print("❌ Lỗi khi cập nhật sản phẩm:", e)
            return False
        finally:
            conn.close()

    def get_product_by_id(self, product_id):
        """Lấy thông tin sản phẩm theo ID."""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Products WHERE id = ?", (product_id,))
            product = cursor.fetchone()
            return product  
        except sqlite3.Error as e:
            print("❌ Lỗi lấy sản phẩm theo ID:", e)
            return None
        finally:
            conn.close()
