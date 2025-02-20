import sqlite3
import os

db_path = r"E:\HK6\DoAN\DoAn\csdl\PetShop.db"
print("📂 Đang kết nối đến file:", os.path.abspath(db_path))

if not os.path.exists(db_path):
    print("❌ Lỗi: File CSDL không tồn tại!")
    exit()

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    if not tables:
        print("⚠️ CSDL không có bảng nào!")
    else:
        print("📌 Danh sách bảng trong CSDL:")
        for table in tables:
            print("-", table[0])

except sqlite3.Error as e:
    print("❌ Lỗi SQLite:", e)

finally:
    conn.close()
