from SQL_database.ketnoiSQL import Database  
import sqlite3

class ProductDatabase(Database):
    def get_all_products(self):
        """Truy vấn tất cả sản phẩm từ bảng Products"""
        conn = self.connect()
        if conn is None:
            return False, []

        try:
            cursor = conn.cursor()
            query = """
            SELECT p.id, p.product_name, c.category_name, p.price, p.stock_quantity, p.supplier, p.image_path,p.note
            FROM Products p
            JOIN Categories c ON p.category_id = c.id
        """
            cursor.execute(query)
            products = cursor.fetchall()
            print(f"⚡ Debug - Dữ liệu lấy về từ SQL: {products}")  # Debug

            return True, products
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy sản phẩm: {e}")
            return False, []
        finally:
            conn.close()


    def add_product(self, id, product_name, category_name, price, stock_quantity, supplier, image_path,note):
        """Thêm sản phẩm mới vào bảng Products."""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            
            # Lấy ID danh mục từ tên danh mục
            cursor.execute("SELECT id FROM Categories WHERE category_name = ?", (category_name,))
            category_row = cursor.fetchone()
            if category_row is None:
                print("❌ Lỗi: Không tìm thấy danh mục sản phẩm!")
                return False
            category_id = category_row[0]

            # Thực hiện INSERT
            cursor.execute("""
                INSERT INTO Products (id, product_name, category_id, price, stock_quantity, supplier, image_path,note) 
                VALUES (?, ?, ?, ?, ?, ?, ?,?)
            """, (id, product_name, category_id, price, stock_quantity, supplier, image_path,note))

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

    def update_product(self, product_id, name, category_name, price, stock, supplier, image_path, note):
        """Cập nhật thông tin sản phẩm trong CSDL, bao gồm ảnh."""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()

            # Lấy ID danh mục từ tên danh mục
            cursor.execute("SELECT id FROM Categories WHERE category_name = ?", (category_name,))
            category_row = cursor.fetchone()
            if category_row is None:
                print("❌ Lỗi: Không tìm thấy danh mục sản phẩm!")
                return False
            category_id = category_row[0]

            query = """
            UPDATE Products
            SET product_name = ?, category_id = ?, price = ?, stock_quantity = ?, supplier = ?, image_path = ?,note = ?
            WHERE id = ?
            """
            cursor.execute(query, (name, category_id, price, stock, supplier, image_path,note, product_id))
            conn.commit()
            print(f"✅ Cập nhật sản phẩm '{name}' thành công!")
            return True
        except Exception as e:
            print(f"❌ Lỗi cập nhật sản phẩm: {e}")
            return False
        finally:
            conn.close()

    def get_product_by_id(self, id):
        """Lấy thông tin sản phẩm dựa trên ID."""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            query = """
                SELECT P.id, P.product_name, C.category_name, P.price, P.stock_quantity, P.supplier, P.note
                FROM Products P
                JOIN Categories C ON P.category_id = C.id
                WHERE P.id = ?
            """
            cursor.execute(query, (id,))
            row = cursor.fetchone()

            if row:
                return {
                    "id": row[0],
                    "product_name": row[1],
                    "category": row[2],
                    "price": row[3],
                    "stock_quantity": row[4],
                    "supplier": row[5],
                    "note": row[6]
                }
            return None
        except Exception as e:
            print(f"❌ Lỗi khi lấy sản phẩm: {e}")
            return None
        finally:
            conn.close()

    def get_all_categories(self):
        """Lấy tất cả danh mục từ CSDL."""
        conn = self.connect()
        if conn is None:
            return []

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT category_name FROM Categories")
            return [row[0] for row in cursor.fetchall()]
        except Exception as e:
            print(f"❌ Lỗi lấy danh mục: {e}")
            return []
        finally:
            conn.close()

    def get_all_suppliers(self):
        """Lấy tất cả nhà cung cấp từ CSDL."""
        conn = self.connect()
        if conn is None:
            return []

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM Suppliers")
            return [row[0] for row in cursor.fetchall()]
        except Exception as e:
            print(f"❌ Lỗi lấy nhà cung cấp: {e}")
            return []
        finally:
            conn.close()

    def search_product_by_name(self, search_text):
        """Tìm sản phẩm theo tên"""
        conn = self.connect()
        if conn is None:
            return []

        cursor = conn.cursor()
        query = """
        SELECT p.id, p.product_name, c.category_name, p.price, p.stock_quantity, p.supplier, p.image_path,p.note
        FROM Products p
        JOIN Categories c ON p.category_id = c.id
        WHERE p.product_name LIKE ?
    """
        cursor.execute(query, (f"%{search_text}%",))  # Tìm kiếm gần đúng
        results = cursor.fetchall()
        conn.close()

    # Chuyển kết quả thành danh sách từ điển
        products = []
        for row in results:
            products.append({
            "id": row[0],
            "product_name": row[1],
            "category_name": row[2],
            "price": row[3],
            "stock_quantity": row[4],
            "supplier": row[5],
            "image_path": row[6],
            "note": row[7]
        })
        return products


    def get_category_id(self, category_name):
        """Lấy ID danh mục dựa trên tên danh mục."""
        conn = self.connect()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM Categories WHERE category_name = ?", (category_name,))
            row = cursor.fetchone()
            return row[0] if row else None
        except Exception as e:
            print(f"❌ Lỗi lấy ID danh mục: {e}")
            return None
        finally:
            conn.close()

    
    def get_products_by_category(self, selected_category):
        """Lấy danh sách sản phẩm theo danh mục"""
        conn = self.connect()
        if conn is None:
            return []

        try:
            cursor = conn.cursor()
            if selected_category == "Tất cả":
                query = """
            SELECT p.id, p.product_name, c.category_name, p.price, p.stock_quantity, p.supplier, p.image_path,p.note
            FROM Products p
            JOIN Categories c ON p.category_id = c.id
            """
                cursor.execute(query)
            else:
                query = """
            SELECT p.id, p.product_name, c.category_name, p.price, p.stock_quantity, p.supplier, p.image_path,p.note
            FROM Products p
            JOIN Categories c ON p.category_id = c.id
            WHERE c.category_name = ?
            """
                cursor.execute(query, (selected_category,))

            products = cursor.fetchall()
            print(f"⚡ Debug - Sản phẩm theo danh mục [{selected_category}]:", products)  # Debug
            return products
        except sqlite3.Error as e:
            print(f"❌ Lỗi khi lấy sản phẩm theo danh mục: {e}")
            return []
        finally:
            conn.close()

    def update_product_quantity(self, product_id, quantity_change):
        """Cập nhật số lượng sản phẩm theo đơn hàng"""
        conn = self.connect()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE Products SET stock_quantity = stock_quantity + ? WHERE id = ?", (quantity_change, product_id))
            conn.commit()
            return True
        except Exception as e:
            print(f"Lỗi cập nhật số lượng sản phẩm: {e}")
            return False
        finally:
            conn.close()

