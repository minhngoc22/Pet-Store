# Form implementation generated from reading ui file 'dangnhap.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(899, 458)
        LoginWindow.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        LoginWindow.setStyleSheet("background-color:rgb(248, 236, 240)")
        self.centralwidget = QtWidgets.QWidget(parent=LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, -20, 371, 121))
        font = QtGui.QFont()
        font.setFamily("UTM Akashi")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(198, 136, 235);")
        self.label.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 120, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(108, 126, 225)")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 220, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(108, 126, 225)")
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 50, 311, 291))
        self.widget.setStyleSheet("background-image: url(\"E:/HK6/DoAN/DoAn/hinhanh/logo.png\");\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-size: cover;  /* Ảnh sẽ tự động căn chỉnh để phủ toàn bộ */\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.btn_dangnhap = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_dangnhap.setGeometry(QtCore.QRect(570, 320, 211, 51))
        font = QtGui.QFont()
        font.setFamily("UTM Akashi")
        font.setPointSize(20)
        self.btn_dangnhap.setFont(font)
        self.btn_dangnhap.setStyleSheet("QPushButton {\n"
"    background-color: rgb(112, 194, 180); /* Màu nền xanh dương */\n"
"    color: white; /* Màu chữ trắng */\n"
"    border-radius: 10px; /* Bo góc */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(41, 128, 185); /* Màu nền khi rê chuột */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(31, 97, 141); /* Màu nền khi nhấn */\n"
"}\n"
"")
        self.btn_dangnhap.setObjectName("btn_dangnhap")
        self.txt_ten = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_ten.setGeometry(QtCore.QRect(530, 130, 291, 41))
        self.txt_ten.setStyleSheet("border-radius: 10px;\n"
"        border: 2px solid #3498db;  /* Viền xanh dương */\n"
"        background-color: #ffffff")
        self.txt_ten.setText("")
        self.txt_ten.setObjectName("txt_ten")
        self.txt_pass = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_pass.setGeometry(QtCore.QRect(530, 230, 291, 41))
        self.txt_pass.setStyleSheet("border-radius: 10px;\n"
"        border: 2px solid #3498db;  /* Viền xanh dương */\n"
"        background-color: #ffffff")
        self.txt_pass.setText("")
        self.txt_pass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.txt_pass.setObjectName("txt_pass")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 899, 26))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "LoginWindow"))
        self.label.setText(_translate("LoginWindow", "User Login"))
        self.label_2.setText(_translate("LoginWindow", "User Name"))
        self.label_3.setText(_translate("LoginWindow", "PassWord"))
        self.btn_dangnhap.setText(_translate("LoginWindow", "Login"))
        self.txt_ten.setPlaceholderText(_translate("LoginWindow", "Enter usename"))
        self.txt_pass.setPlaceholderText(_translate("LoginWindow", "Enter password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec())
