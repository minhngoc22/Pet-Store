# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox

class Ui_UIMainWindow(QtWidgets.QMainWindow):
    def setupUi(self, UIMainWindow):
        UIMainWindow.setObjectName("UIMainWindow")
        UIMainWindow.resize(1179, 680)
        UIMainWindow.setStyleSheet("background-color: rgb(255, 255, 215);")
        self.centralwidget = QtWidgets.QWidget(parent=UIMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.home = QtWidgets.QWidget(parent=self.centralwidget)
        self.home.setGeometry(QtCore.QRect(270, 70, 731, 551))
        self.home.setStyleSheet("\n"
"background-color:rgb(248, 236, 240);\n"
" border-radius: 20px; /* Bo góc */")
        self.home.setObjectName("home")
        self.stats = QtWidgets.QWidget(parent=self.home)
        self.stats.setGeometry(QtCore.QRect(0, 0, 731, 161))
        self.stats.setObjectName("stats")
        self.bill = QtWidgets.QWidget(parent=self.stats)
        self.bill.setGeometry(QtCore.QRect(10, 10, 231, 101))
        self.bill.setStyleSheet("background-color: rgb(255, 253, 188);\n"
"color: rgb(255, 239, 178);\n"
"   border-radius: 20px; /* Bo góc */;")
        self.bill.setObjectName("bill")
        self.label_5 = QtWidgets.QLabel(parent=self.bill)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(241, 121, 184)")
        self.label_5.setObjectName("label_5")
        self.label_11 = QtWidgets.QLabel(parent=self.bill)
        self.label_11.setGeometry(QtCore.QRect(180, 50, 41, 41))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("hinhanh/bill1.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.dthu = QtWidgets.QWidget(parent=self.stats)
        self.dthu.setGeometry(QtCore.QRect(250, 10, 231, 101))
        self.dthu.setStyleSheet("background-color: rgb(195, 255, 188);\n"
" border-radius: 20px; /* Bo góc */;")
        self.dthu.setObjectName("dthu")
        self.label_7 = QtWidgets.QLabel(parent=self.dthu)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(241, 121, 184)")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.dthu)
        self.label_8.setGeometry(QtCore.QRect(180, 50, 41, 41))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("hinhanh/dthu1.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.spham = QtWidgets.QWidget(parent=self.stats)
        self.spham.setGeometry(QtCore.QRect(490, 10, 231, 101))
        self.spham.setStyleSheet("background-color: rgb(255, 253, 188);\n"
"color: rgb(255, 239, 178);\n"
"   border-radius: 20px; /* Bo góc */;")
        self.spham.setObjectName("spham")
        self.label_10 = QtWidgets.QLabel(parent=self.spham)
        self.label_10.setGeometry(QtCore.QRect(180, 50, 41, 41))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("hinhanh/spham.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(parent=self.spham)
        self.label_9.setGeometry(QtCore.QRect(10, 0, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(241, 121, 184)")
        self.label_9.setObjectName("label_9")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 0, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(149, 106, 214);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 10, 61, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("hinhanh/home.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1010, 0, 61, 51))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("hinhanh/user.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1010, 50, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(149, 106, 214);\n"
"font: 14pt \"Segoe Script\";")
        self.label_2.setObjectName("label_2")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 10, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(241, 121, 184);\n"
"font: 75 30pt \"Segoe Script\";\n"
"")
        self.label_12.setObjectName("label_12")
        self.btn_donhang = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_donhang.setGeometry(QtCore.QRect(20, 340, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_donhang.setFont(font)
        self.btn_donhang.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 255, 215); /* Màu nền xanh dương */\n"
"    /* Màu chữ trắng rgb(255, 255, 215)*/\n"
"    color: rgb(149, 106, 214);\n"
"    border-radius: 10px; /* Bo góc */\n"
"}\n"
"QPushButton:hover {\n"
" /* Màu nền khi rê chuột */\n"
"    background-color: rgb(108, 187, 174);\n"
"color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(31, 97, 141); /* Màu nền khi nhấn */\n"
"}")
        self.btn_donhang.setObjectName("btn_donhang")
        self.widget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(60, 80, 81, 81))
        self.widget_3.setStyleSheet("background-image: url(\"E:/HK6/DoAN/DoAn/hinhanh/logo2.png\");\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-size: cover;  /* Ảnh sẽ tự động căn chỉnh để phủ toàn bộ */\n"
"\n"
"\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.btn_dichvu = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_dichvu.setGeometry(QtCore.QRect(20, 280, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_dichvu.setFont(font)
        self.btn_dichvu.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 255, 215); /* Màu nền xanh dương */\n"
"    /* Màu chữ trắng rgb(255, 255, 215)*/\n"
"    color: rgb(149, 106, 214);\n"
"    border-radius: 10px; /* Bo góc */\n"
"}\n"
"QPushButton:hover {\n"
" /* Màu nền khi rê chuột */\n"
"    background-color: rgb(108, 187, 174);\n"
"color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(31, 97, 141); /* Màu nền khi nhấn */\n"
"}")
        self.btn_dichvu.setObjectName("btn_dichvu")
        self.btn_home = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_home.setGeometry(QtCore.QRect(20, 160, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_home.setFont(font)
        self.btn_home.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 255, 215); /* Màu nền xanh dương */\n"
"    /* Màu chữ trắng rgb(255, 255, 215)*/\n"
"    color: rgb(149, 106, 214);\n"
"    border-radius: 10px; /* Bo góc */\n"
"}\n"
"QPushButton:hover {\n"
" /* Màu nền khi rê chuột */\n"
"    background-color: rgb(108, 187, 174);\n"
"color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(31, 97, 141); /* Màu nền khi nhấn */\n"
"}")
        self.btn_home.setObjectName("btn_home")
        self.btn_khachhang = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_khachhang.setGeometry(QtCore.QRect(20, 400, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_khachhang.setFont(font)
        self.btn_khachhang.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 255, 215); /* Màu nền xanh dương */\n"
"    /* Màu chữ trắng rgb(255, 255, 215)*/\n"
"    color: rgb(149, 106, 214);\n"
"    border-radius: 10px; /* Bo góc */\n"
"}\n"
"QPushButton:hover {\n"
" /* Màu nền khi rê chuột */\n"
"    background-color: rgb(108, 187, 174);\n"
"color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(31, 97, 141); /* Màu nền khi nhấn */\n"
"}")
        self.btn_khachhang.setObjectName("btn_khachhang")
        self.btn_logout = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_logout.setGeometry(QtCore.QRect(30, 560, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_logout.setFont(font)
        self.btn_logout.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 255, 215); /* Màu nền xanh dương */\n"
"    /* Màu chữ trắng rgb(255, 255, 215)*/\n"
"    color: rgb(149, 106, 214);\n"
"    border-radius: 10px; /* Bo góc */\n"
"}\n"
"QPushButton:hover {\n"
" /* Màu nền khi rê chuột */\n"
"    background-color: rgb(108, 187, 174);\n"
"color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(31, 97, 141); /* Màu nền khi nhấn */\n"
"}")
        self.btn_logout.setObjectName("btn_logout")
        self.btn_spham = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_spham.setGeometry(QtCore.QRect(20, 220, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_spham.setFont(font)
        self.btn_spham.setStyleSheet("QPushButton {\n"
"    background-color:rgb(255, 255, 215); /* Màu nền xanh dương */\n"
"    /* Màu chữ trắng rgb(255, 255, 215)*/\n"
"    color: rgb(149, 106, 214);\n"
"    border-radius: 10px; /* Bo góc */\n"
"}\n"
"QPushButton:hover {\n"
" /* Màu nền khi rê chuột */\n"
"    background-color: rgb(108, 187, 174);\n"
"color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(31, 97, 141); /* Màu nền khi nhấn */\n"
"}")
        self.btn_spham.setObjectName("btn_spham")
        UIMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=UIMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1179, 26))
        self.menubar.setObjectName("menubar")
        UIMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=UIMainWindow)
        self.statusbar.setObjectName("statusbar")
        UIMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(UIMainWindow)
        QtCore.QMetaObject.connectSlotsByName(UIMainWindow)

        # Kết nối sự kiện click cho các button
        self.btn_logout.clicked.connect(self.logout)

    def retranslateUi(self, UIMainWindow):
        _translate = QtCore.QCoreApplication.translate
        UIMainWindow.setWindowTitle(_translate("UIMainWindow", "MainWindow"))
        self.label_5.setText(_translate("UIMainWindow", "Số hóa đơn trong ngày"))
        self.label_7.setText(_translate("UIMainWindow", "Doanh thu trong ngày"))
        self.label_9.setText(_translate("UIMainWindow", "Số sản phẩm bán trong ngày"))
        self.label_3.setText(_translate("UIMainWindow", "Trang chủ"))
        self.label_2.setText(_translate("UIMainWindow", "Xin chào"))
        self.label_12.setText(_translate("UIMainWindow", "Mini Pet"))
        self.btn_donhang.setText(_translate("UIMainWindow", "Đơn hàng"))
        self.btn_dichvu.setText(_translate("UIMainWindow", "Dịch vụ"))
        self.btn_home.setText(_translate("UIMainWindow", "Trang chủ"))
        self.btn_khachhang.setText(_translate("UIMainWindow", "Khách hàng"))
        self.btn_logout.setText(_translate("UIMainWindow", "Đăng xuất"))
        self.btn_spham.setText(_translate("UIMainWindow", "Sản phẩm"))


    def logout(self):
            msg = QMessageBox.question(
            self, "Xác nhận", "Bạn có chắc chắn muốn đăng xuất?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
            if msg == QMessageBox.StandardButton.Yes:
                self.open_login_window()  # Mở lại màn hình đăng nhập
                self.close()

    def open_login_window(self):
                from dangnhap import Ui_LoginWindow
                
                self.close()  # Đóng màn hình chính trước khi mở lại đăng nhập
                self.login_win = QtWidgets.QMainWindow()
                self.ui = Ui_LoginWindow()
                self.ui.setupUi(self.login_win)
                self.login_win.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UIMainWindow = QtWidgets.QMainWindow()
    ui = Ui_UIMainWindow()
    ui.setupUi(UIMainWindow)
    UIMainWindow.show()
    sys.exit(app.exec())
