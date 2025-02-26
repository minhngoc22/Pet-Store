# Form implementation generated from reading ui file 'KhachHang/themKH.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_themKH(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(594, 508)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_email = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txt_email.setGeometry(QtCore.QRect(320, 180, 261, 41))
        self.txt_email.setStyleSheet("border-radius: 10px;\n"
"        border: 3px solid #3498db;  /* Viền xanh dương */\n"
"        background-color: #ffffff")
        self.txt_email.setObjectName("txt_email")
        self.labelTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(140, 10, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.btn_them = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_them.setGeometry(QtCore.QRect(200, 400, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_them.setFont(font)
        self.btn_them.setObjectName("btn_them")
        self.txt_tenKH = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txt_tenKH.setGeometry(QtCore.QRect(30, 90, 261, 41))
        self.txt_tenKH.setStyleSheet("border-radius: 10px;\n"
"        border: 3px solid #3498db;  /* Viền xanh dương */\n"
"        background-color: #ffffff")
        self.txt_tenKH.setObjectName("txt_tenKH")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 150, 81, 21))
        self.label_3.setStyleSheet("font: 10pt \"UTM Bell\";\n"
"color: rgb(241, 121, 184);\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 60, 161, 21))
        self.label_4.setStyleSheet("font: 10pt \"UTM Bell\";\n"
"color: rgb(241, 121, 184);\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 150, 101, 31))
        self.label_2.setStyleSheet("font: 10pt \"UTM Bell\";\n"
"color: rgb(241, 121, 184);\n"
"")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 50, 191, 31))
        self.label.setStyleSheet("font: 10pt \"UTM Bell\";\n"
"color: rgb(241, 121, 184);\n"
"")
        self.label.setObjectName("label")
        self.txt_diachi = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txt_diachi.setGeometry(QtCore.QRect(30, 180, 261, 41))
        self.txt_diachi.setStyleSheet("border-radius: 10px;\n"
"        border: 3px solid #3498db;  /* Viền xanh dương */\n"
"        background-color: #ffffff")
        self.txt_diachi.setObjectName("txt_diachi")
        self.txt_sdt = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txt_sdt.setGeometry(QtCore.QRect(320, 90, 261, 41))
        self.txt_sdt.setStyleSheet("border-radius: 10px;\n"
"        border: 3px solid #3498db;  /* Viền xanh dương */\n"
"        background-color: #ffffff")
        self.txt_sdt.setObjectName("txt_sdt")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 240, 101, 21))
        self.label_6.setStyleSheet("font: 10pt \"UTM Bell\";\n"
"color: rgb(241, 121, 184);\n"
"")
        self.label_6.setObjectName("label_6")
        self.txt_note = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txt_note.setGeometry(QtCore.QRect(120, 270, 361, 111))
        self.txt_note.setObjectName("txt_note")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitle.setStyleSheet(_translate("MainWindow", "color: rgb(149, 106, 214);"))
        self.labelTitle.setText(_translate("MainWindow", "KHÁCH HÀNG MỚI"))
        self.btn_them.setStyleSheet(_translate("MainWindow", "background-color: rgb(255, 255, 215); color: rgb(149, 106, 214); border-radius: 10px;"))
        self.btn_them.setText(_translate("MainWindow", "THÊM"))
        self.label_3.setText(_translate("MainWindow", "EMAIL"))
        self.label_4.setText(_translate("MainWindow", "SỐ ĐIỆN THOẠI"))
        self.label_2.setText(_translate("MainWindow", "ĐỊA CHỈ"))
        self.label.setText(_translate("MainWindow", "TÊN KHÁCH HÀNG"))
        self.label_6.setText(_translate("MainWindow", "GHI CHÚ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_themKH()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
