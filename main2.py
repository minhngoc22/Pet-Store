from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QListWidget, QFrame, QGridLayout, QTableWidget
from PyQt6.QtGui import QFont
import sys

class PetStoreUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pet Shop - Trang chủ")
        self.setGeometry(100, 100, 1200, 700)
        
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QHBoxLayout()
        
        # Sidebar menu
        sidebar = QVBoxLayout()
        sidebar.setSpacing(10)
        
        self.shop_name = QLabel("🐾 PET SHOP")
        self.shop_name.setScaledContents(True)
        self.shop_name.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        sidebar.addWidget(self.shop_name)
        
        self.menu_buttons = ["Trang chủ", "Đơn hàng", "Sản phẩm", "Khách hàng", "Nhập hàng", "Cài đặt", "Đăng xuất"]
        for name in self.menu_buttons:
            btn = QPushButton(name)
            btn.setFixedHeight(40)
            sidebar.addWidget(btn)
        
        sidebar_frame = QFrame()
        sidebar_frame.setLayout(sidebar)
        sidebar_frame.setFixedWidth(250)
        sidebar_frame.setStyleSheet("background-color: #2C2F33; color: white; border-radius: 10px; padding: 10px;")
        main_layout.addWidget(sidebar_frame)
        
        # Dashboard
        dashboard = QVBoxLayout()
        
        title = QLabel("📊 Trang Chủ")
        title.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        dashboard.addWidget(title)
        
        stats_layout = QHBoxLayout()
        stats = ["Số đơn bán ra trong ngày:", "Doanh thu ngày:", "Số sản phẩm bán trong ngày:"]
        colors = ["#6A5ACD", "#FFA500", "#6495ED"]
        
        for i, stat in enumerate(stats):
            stat_frame = QVBoxLayout()
            stat_label = QLabel(stat)
            stat_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
            stat_value = QLabel("0")
            stat_value.setFont(QFont("Arial", 20, QFont.Weight.Bold))
            stat_frame.addWidget(stat_label)
            stat_frame.addWidget(stat_value)
            
            stat_widget = QWidget()
            stat_widget.setLayout(stat_frame)
            stat_widget.setStyleSheet(f"background-color: {colors[i]}; color: white; padding: 15px; border-radius: 10px;")
            stats_layout.addWidget(stat_widget)
        
        dashboard.addLayout(stats_layout)
        
        # Biểu đồ (placeholder bằng bảng tạm thời)
        self.chart = QTableWidget(5, 2)
        self.chart.setHorizontalHeaderLabels(["Thời gian", "Số lượng bán"])
        dashboard.addWidget(self.chart)
        
        main_layout.addLayout(dashboard)
        
        central_widget.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PetStoreUI()
    window.show()
    sys.exit(app.exec())
