# Form implementation generated from reading ui file 'Donhang/updateDH.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(630, 462)
        Form.setStyleSheet("background-color:rgb(248, 236, 240);")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(90, 320, 101, 21))
        self.label_6.setStyleSheet("font: 10pt \"UTM Bell\";\n"
"color: rgb(241, 121, 184);\n"
"")
        self.label_6.setObjectName("label_6")
        self.txt_tongtien = QtWidgets.QTextEdit(parent=Form)
        self.txt_tongtien.setGeometry(QtCore.QRect(340, 190, 261, 41))
        self.txt_tongtien.setStyleSheet("border-radius: 10px;\n"
"        border: 3px solid #3498db;  /* Viền xanh dương */\n"
"        background-color: #ffffff")
        self.txt_tongtien.setObjectName("txt_tongtien")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(60, 150, 141, 31))
        self.label.setStyleSheet("font: 10pt \"UTM Bell\";\n"
"color: rgb(241, 121, 184);\n"
"")
        self.label.setObjectName("label")
        self.cbo_nvxl = QtWidgets.QComboBox(parent=Form)
        self.cbo_nvxl.setGeometry(QtCore.QRect(20, 190, 261, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cbo_nvxl.setFont(font)
        self.cbo_nvxl.setStyleSheet("QComboBox {\n"
"          background-color: white;\n"
"          border: 3px solid #3498db;  /* Viền xanh dương */\n"
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
        self.cbo_nvxl.setObjectName("cbo_nvxl")
        self.btn_luu = QtWidgets.QPushButton(parent=Form)
        self.btn_luu.setGeometry(QtCore.QRect(250, 410, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_luu.setFont(font)
        self.btn_luu.setObjectName("btn_luu")
        self.labelTitle = QtWidgets.QLabel(parent=Form)
        self.labelTitle.setGeometry(QtCore.QRect(100, 10, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet("color: rgb(149, 106, 214);\n"
"font: 87 22pt \"Segoe UI Black\";")
        self.labelTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(410, 240, 101, 31))
        self.label_4.setStyleSheet("font: 10pt \"UTM Bell\";\n"
"color: rgb(241, 121, 184);\n"
"")
        self.label_4.setObjectName("label_4")
        self.cbo_thanhtoan = QtWidgets.QComboBox(parent=Form)
        self.cbo_thanhtoan.setGeometry(QtCore.QRect(20, 270, 261, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cbo_thanhtoan.setFont(font)
        self.cbo_thanhtoan.setStyleSheet("QComboBox {\n"
"          background-color: white;\n"
"          border: 3px solid #3498db;  /* Viền xanh dương */\n"
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
        self.cbo_thanhtoan.setObjectName("cbo_thanhtoan")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(80, 240, 111, 21))
        self.label_3.setStyleSheet("font: 10pt \"UTM Bell\";\n"
"color: rgb(241, 121, 184);\n"
"")
        self.label_3.setObjectName("label_3")
        self.cbo_trangthai = QtWidgets.QComboBox(parent=Form)
        self.cbo_trangthai.setGeometry(QtCore.QRect(340, 270, 261, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cbo_trangthai.setFont(font)
        self.cbo_trangthai.setStyleSheet("QComboBox {\n"
"          background-color: white;\n"
"          border: 3px solid #3498db;  /* Viền xanh dương */\n"
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
        self.cbo_trangthai.setObjectName("cbo_trangthai")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(420, 150, 91, 31))
        self.label_2.setStyleSheet("font: 10pt \"UTM Bell\";\n"
"color: rgb(241, 121, 184);\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(400, 60, 141, 31))
        self.label_5.setStyleSheet("font: 10pt \"UTM Bell\";\n"
"color: rgb(241, 121, 184);\n"
"")
        self.label_5.setObjectName("label_5")
        self.txt_maKH = QtWidgets.QTextEdit(parent=Form)
        self.txt_maKH.setGeometry(QtCore.QRect(340, 100, 261, 41))
        self.txt_maKH.setStyleSheet("border-radius: 10px;\n"
"        border: 3px solid #3498db;  /* Viền xanh dương */\n"
"        background-color: #ffffff")
        self.txt_maKH.setObjectName("txt_maKH")
        self.txt_note = QtWidgets.QTextEdit(parent=Form)
        self.txt_note.setGeometry(QtCore.QRect(20, 360, 261, 41))
        self.txt_note.setStyleSheet("border-radius: 10px;\n"
"        border: 3px solid #3498db;  /* Viền xanh dương */\n"
"        background-color: #ffffff")
        self.txt_note.setObjectName("txt_note")
        self.txt_maDH = QtWidgets.QTextEdit(parent=Form)
        self.txt_maDH.setGeometry(QtCore.QRect(20, 100, 261, 41))
        self.txt_maDH.setStyleSheet("border-radius: 10px;\n"
"        border: 3px solid #3498db;  /* Viền xanh dương */\n"
"        background-color: #ffffff")
        self.txt_maDH.setObjectName("txt_maDH")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(70, 60, 141, 31))
        self.label_7.setStyleSheet("font: 10pt \"UTM Bell\";\n"
"color: rgb(241, 121, 184);\n"
"")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "GHI CHÚ"))
        self.label.setText(_translate("Form", "NHÂN VIÊN XỬ LÝ"))
        self.btn_luu.setStyleSheet(_translate("Form", "background-color: rgb(255, 255, 215); color: rgb(149, 106, 214); border-radius: 10px;"))
        self.btn_luu.setText(_translate("Form", "LƯU"))
        self.labelTitle.setText(_translate("Form", "CẬP NHẬT ĐƠN HÀNG"))
        self.label_4.setText(_translate("Form", "TRẠNG THÁI"))
        self.label_3.setText(_translate("Form", "THANH TOÁN"))
        self.label_2.setText(_translate("Form", "TỔNG TIỀN"))
        self.label_5.setText(_translate("Form", "MÃ KHÁCH HÀNG"))
        self.label_7.setText(_translate("Form", "MÃ ĐƠN HÀNG"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
