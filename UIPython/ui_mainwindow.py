# Form implementation generated from reading ui file 'e:/HK6/DoAN/DoAn/UI/main.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_UIMainWindow(object):
    def setupUi(self, UIMainWindow):
        UIMainWindow.setObjectName("UIMainWindow")
        UIMainWindow.resize(1203, 695)
        UIMainWindow.setStyleSheet("background-color: rgb(255, 255, 215);")
        self.centralwidget = QtWidgets.QWidget(parent=UIMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 600, 61, 51))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("e:/HK6/DoAN/DoAn/UI\\hinhanh/user.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 241, 61))
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
        self.btn_logout = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_logout.setGeometry(QtCore.QRect(20, 540, 191, 51))
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
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 160, 241, 371))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_home = QtWidgets.QPushButton(parent=self.widget)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("e:/HK6/DoAN/DoAn/UI\\../hinhanh/home.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setObjectName("btn_home")
        self.verticalLayout.addWidget(self.btn_home)
        self.btn_spham = QtWidgets.QPushButton(parent=self.widget)
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
        self.verticalLayout.addWidget(self.btn_spham)
        self.btn_dichvu = QtWidgets.QPushButton(parent=self.widget)
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("e:/HK6/DoAN/DoAn/UI\\../hinhanh/4.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_dichvu.setIcon(icon1)
        self.btn_dichvu.setObjectName("btn_dichvu")
        self.verticalLayout.addWidget(self.btn_dichvu)
        self.btn_donhang = QtWidgets.QPushButton(parent=self.widget)
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
        self.verticalLayout.addWidget(self.btn_donhang)
        self.btn_khachhang = QtWidgets.QPushButton(parent=self.widget)
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
        self.verticalLayout.addWidget(self.btn_khachhang)
        self.btn_nhacc = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_nhacc.setFont(font)
        self.btn_nhacc.setStyleSheet("QPushButton {\n"
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
        self.btn_nhacc.setObjectName("btn_nhacc")
        self.verticalLayout.addWidget(self.btn_nhacc)
        self.Menu = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.Menu.setGeometry(QtCore.QRect(270, 30, 881, 621))
        self.Menu.setStyleSheet("background-color:rgb(248, 236, 240);\n"
"\n"
"border-radius: 20px; /* Bo góc */;")
        self.Menu.setObjectName("Menu")
        self.trangchu = QtWidgets.QWidget()
        self.trangchu.setObjectName("trangchu")
        self.label_3 = QtWidgets.QLabel(parent=self.trangchu)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(149, 106, 214);")
        self.label_3.setObjectName("label_3")
        self.widget_2 = QtWidgets.QWidget(parent=self.trangchu)
        self.widget_2.setGeometry(QtCore.QRect(20, 60, 841, 151))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bill_4 = QtWidgets.QWidget(parent=self.widget_2)
        self.bill_4.setStyleSheet("background-color: rgb(255, 253, 188);\n"
"color: rgb(255, 239, 178);\n"
"   border-radius: 20px; /* Bo góc */;")
        self.bill_4.setObjectName("bill_4")
        self.label_25 = QtWidgets.QLabel(parent=self.bill_4)
        self.label_25.setGeometry(QtCore.QRect(10, 0, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(241, 121, 184);\n"
"font: 87 12pt \"Arial\";\n"
"")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(parent=self.bill_4)
        self.label_26.setGeometry(QtCore.QRect(200, 50, 41, 41))
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap("e:/HK6/DoAN/DoAn/UI\\../hinhanh/bill1.png"))
        self.label_26.setScaledContents(True)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_2.addWidget(self.bill_4)
        self.dthu_4 = QtWidgets.QWidget(parent=self.widget_2)
        self.dthu_4.setStyleSheet("background-color: rgb(195, 255, 188);\n"
" border-radius: 20px; /* Bo góc */;")
        self.dthu_4.setObjectName("dthu_4")
        self.label_27 = QtWidgets.QLabel(parent=self.dthu_4)
        self.label_27.setGeometry(QtCore.QRect(10, 10, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(241, 121, 184);\n"
"font: 87 12pt \"Arial\";\n"
"\n"
"")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(parent=self.dthu_4)
        self.label_28.setGeometry(QtCore.QRect(130, 50, 41, 41))
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap("e:/HK6/DoAN/DoAn/UI\\../hinhanh/dthu1.png"))
        self.label_28.setScaledContents(True)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_2.addWidget(self.dthu_4)
        self.spham_4 = QtWidgets.QWidget(parent=self.widget_2)
        self.spham_4.setStyleSheet("background-color: rgb(255, 253, 188);\n"
"color: rgb(255, 239, 178);\n"
"   border-radius: 20px; /* Bo góc */;")
        self.spham_4.setObjectName("spham_4")
        self.label_29 = QtWidgets.QLabel(parent=self.spham_4)
        self.label_29.setGeometry(QtCore.QRect(190, 60, 41, 41))
        self.label_29.setText("")
        self.label_29.setPixmap(QtGui.QPixmap("e:/HK6/DoAN/DoAn/UI\\../hinhanh/spham.png"))
        self.label_29.setScaledContents(True)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(parent=self.spham_4)
        self.label_30.setGeometry(QtCore.QRect(10, 0, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(241, 121, 184);\n"
"font: 87 12pt \"Arial\";\n"
"\n"
"")
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_2.addWidget(self.spham_4)
        self.Menu.addWidget(self.trangchu)
        self.dichvu = QtWidgets.QWidget()
        self.dichvu.setObjectName("dichvu")
        self.label_5 = QtWidgets.QLabel(parent=self.dichvu)
        self.label_5.setGeometry(QtCore.QRect(30, 0, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(149, 106, 214);")
        self.label_5.setObjectName("label_5")
        self.cbo_dv = QtWidgets.QComboBox(parent=self.dichvu)
        self.cbo_dv.setGeometry(QtCore.QRect(30, 60, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.cbo_dv.setFont(font)
        self.cbo_dv.setStyleSheet("QComboBox {\n"
"    \n"
"          background-color: white;\n"
"          border: 2px solid #ccc;\n"
"          border-radius: 10px;\n"
"          padding: 5px;\n"
"font: 81 12pt \"Rockwell Extra Bold\";\n"
"      }\n"
"      QComboBox::drop-down {\n"
"          border: none;\n"
"          background: transparent;\n"
"      }\n"
"      QComboBox::down-arrow {\n"
"          image: url(down-arrow.png); /* Thay bằng icon của bạn */\n"
"          width: 14px;\n"
"          height: 14px;\n"
"      }\n"
"")
        self.cbo_dv.setObjectName("cbo_dv")
        self.cbo_dv.addItem("")
        self.cbo_dv.addItem("")
        self.cbo_dv.addItem("")
        self.cbo_dv.addItem("")
        self.txt_timkiem1 = QtWidgets.QTextEdit(parent=self.dichvu)
        self.txt_timkiem1.setGeometry(QtCore.QRect(310, 60, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txt_timkiem1.setFont(font)
        self.txt_timkiem1.setStyleSheet("background-color: rgb(248, 236, 240);\n"
"border: 3px solid #ffffff;  /* Viền màu hồng */\n"
"        border-radius: 20px;\n"
"        padding: 5px 10px;")
        self.txt_timkiem1.setObjectName("txt_timkiem1")
        self.btn_them = QtWidgets.QPushButton(parent=self.dichvu)
        self.btn_them.setGeometry(QtCore.QRect(160, 570, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_them.setFont(font)
        self.btn_them.setStyleSheet("QPushButton {\n"
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
        self.btn_them.setObjectName("btn_them")
        self.btn_xoa = QtWidgets.QPushButton(parent=self.dichvu)
        self.btn_xoa.setGeometry(QtCore.QRect(360, 570, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_xoa.setFont(font)
        self.btn_xoa.setStyleSheet("QPushButton {\n"
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
        self.btn_xoa.setObjectName("btn_xoa")
        self.btn_sua = QtWidgets.QPushButton(parent=self.dichvu)
        self.btn_sua.setGeometry(QtCore.QRect(580, 570, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_sua.setFont(font)
        self.btn_sua.setStyleSheet("QPushButton {\n"
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
        self.btn_sua.setObjectName("btn_sua")
        self.Menu.addWidget(self.dichvu)
        self.khachhang = QtWidgets.QWidget()
        self.khachhang.setObjectName("khachhang")
        self.cbo_kh = QtWidgets.QComboBox(parent=self.khachhang)
        self.cbo_kh.setGeometry(QtCore.QRect(10, 60, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cbo_kh.setFont(font)
        self.cbo_kh.setStyleSheet("QComboBox {\n"
"          background-color: white;\n"
"          border: 2px solid #ccc;\n"
"          border-radius: 10px;\n"
"          padding: 5px;\n"
"      }\n"
"      QComboBox::drop-down {\n"
"          border: none;\n"
"          background: transparent;\n"
"      }\n"
"      QComboBox::down-arrow {\n"
"          image: url(down-arrow.png); /* Thay bằng icon của bạn */\n"
"          width: 14px;\n"
"          height: 14px;\n"
"      }")
        self.cbo_kh.setObjectName("cbo_kh")
        self.cbo_kh.addItem("")
        self.cbo_kh.addItem("")
        self.txt_timkiem2 = QtWidgets.QTextEdit(parent=self.khachhang)
        self.txt_timkiem2.setGeometry(QtCore.QRect(300, 60, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txt_timkiem2.setFont(font)
        self.txt_timkiem2.setStyleSheet("background-color: rgb(248, 236, 240);\n"
"border: 3px solid #ffffff;  /* Viền màu hồng */\n"
"        border-radius: 20px;\n"
"        padding: 5px 10px;")
        self.txt_timkiem2.setObjectName("txt_timkiem2")
        self.btn_sua2 = QtWidgets.QPushButton(parent=self.khachhang)
        self.btn_sua2.setGeometry(QtCore.QRect(560, 570, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_sua2.setFont(font)
        self.btn_sua2.setStyleSheet("QPushButton {\n"
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
        self.btn_sua2.setObjectName("btn_sua2")
        self.label_8 = QtWidgets.QLabel(parent=self.khachhang)
        self.label_8.setGeometry(QtCore.QRect(10, 0, 491, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(149, 106, 214);")
        self.label_8.setObjectName("label_8")
        self.btn_them2 = QtWidgets.QPushButton(parent=self.khachhang)
        self.btn_them2.setGeometry(QtCore.QRect(140, 570, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_them2.setFont(font)
        self.btn_them2.setStyleSheet("QPushButton {\n"
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
        self.btn_them2.setObjectName("btn_them2")
        self.btn_xoa2 = QtWidgets.QPushButton(parent=self.khachhang)
        self.btn_xoa2.setGeometry(QtCore.QRect(340, 570, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_xoa2.setFont(font)
        self.btn_xoa2.setStyleSheet("QPushButton {\n"
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
        self.btn_xoa2.setObjectName("btn_xoa2")
        self.Menu.addWidget(self.khachhang)
        UIMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=UIMainWindow)
        self.statusbar.setObjectName("statusbar")
        UIMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(UIMainWindow)
        self.Menu.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(UIMainWindow)

    def retranslateUi(self, UIMainWindow):
        _translate = QtCore.QCoreApplication.translate
        UIMainWindow.setWindowTitle(_translate("UIMainWindow", "MainWindow"))
        self.label_12.setText(_translate("UIMainWindow", "Mini Pet"))
        self.btn_logout.setText(_translate("UIMainWindow", "Đăng xuất"))
        self.btn_home.setText(_translate("UIMainWindow", "Trang chủ"))
        self.btn_spham.setText(_translate("UIMainWindow", "Sản phẩm"))
        self.btn_dichvu.setText(_translate("UIMainWindow", "Dịch vụ"))
        self.btn_donhang.setText(_translate("UIMainWindow", "Đơn hàng"))
        self.btn_khachhang.setText(_translate("UIMainWindow", "Khách hàng"))
        self.btn_nhacc.setText(_translate("UIMainWindow", "Nhà cung cấp"))
        self.label_3.setText(_translate("UIMainWindow", "TRANG CHỦ"))
        self.label_25.setText(_translate("UIMainWindow", "Số hóa đơn trong ngày"))
        self.label_27.setText(_translate("UIMainWindow", "Doanh thu trong ngày"))
        self.label_30.setText(_translate("UIMainWindow", "Sản phẩm bán trong ngày"))
        self.label_5.setText(_translate("UIMainWindow", "DỊCH VỤ"))
        self.cbo_dv.setItemText(0, _translate("UIMainWindow", "Chăm sóc thú cưng"))
        self.cbo_dv.setItemText(1, _translate("UIMainWindow", "Thú y"))
        self.cbo_dv.setItemText(2, _translate("UIMainWindow", "Trông giữ thú cưng"))
        self.cbo_dv.setItemText(3, _translate("UIMainWindow", "Huấn luyện thú cưng"))
        self.txt_timkiem1.setPlaceholderText(_translate("UIMainWindow", "Tìm kiếm"))
        self.btn_them.setText(_translate("UIMainWindow", "THÊM"))
        self.btn_xoa.setText(_translate("UIMainWindow", "XÓA"))
        self.btn_sua.setText(_translate("UIMainWindow", "SỬA"))
        self.cbo_kh.setItemText(0, _translate("UIMainWindow", "Khách hàng"))
        self.cbo_kh.setItemText(1, _translate("UIMainWindow", "Thú cưng"))
        self.txt_timkiem2.setPlaceholderText(_translate("UIMainWindow", "Tìm kiếm"))
        self.btn_sua2.setText(_translate("UIMainWindow", "SỬA"))
        self.label_8.setText(_translate("UIMainWindow", "KHÁCH HÀNG VÀ THÚ CƯNG"))
        self.btn_them2.setText(_translate("UIMainWindow", "THÊM"))
        self.btn_xoa2.setText(_translate("UIMainWindow", "XÓA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UIMainWindow = QtWidgets.QMainWindow()
    ui = Ui_UIMainWindow()
    ui.setupUi(UIMainWindow)
    UIMainWindow.show()
    sys.exit(app.exec())
