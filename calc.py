# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Ui_Form(object):
    def addition(self):
        z = int(self.lineEdit.text()) + int(self.lineEdit_2.text())
        msg = QMessageBox()
        msg.setText(str(z))
        msg.setWindowTitle("Answer")
        msg.exec()
    def subtraction(self):
        z = int(self.lineEdit.text()) - int(self.lineEdit_2.text())
        msg = QMessageBox()
        msg.setText(str(z))
        msg.setWindowTitle("Answer")
        msg.exec()
    def multiplication(self):
        z = int(self.lineEdit.text()) * int(self.lineEdit_2.text())
        msg = QMessageBox()
        msg.setText(str(z))
        msg.setWindowTitle("Answer")
        msg.exec()
    def division(self):
        z = int(self.lineEdit.text()) // int(self.lineEdit_2.text())
        msg = QMessageBox()
        msg.setText(str(z))
        msg.setWindowTitle("Answer")
        msg.exec()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(515, 314)
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setGeometry(QtCore.QRect(30, 140, 113, 32))
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(self.addition)
        self.subButton = QtWidgets.QPushButton(Form)
        self.subButton.setGeometry(QtCore.QRect(140, 140, 113, 32))
        self.subButton.setObjectName("subButton")
        self.subButton.clicked.connect(self.subtraction)
        self.mulButton = QtWidgets.QPushButton(Form)
        self.mulButton.setGeometry(QtCore.QRect(250, 140, 113, 32))
        self.mulButton.setObjectName("mulButton")
        self.mulButton.clicked.connect(self.multiplication)
        self.divButton = QtWidgets.QPushButton(Form)
        self.divButton.setGeometry(QtCore.QRect(370, 140, 113, 32))
        self.divButton.setObjectName("divButton")
        self.divButton.clicked.connect(self.division)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 70, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 70, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addButton.setText(_translate("Form", "Add"))
        self.subButton.setText(_translate("Form", "Subtract"))
        self.mulButton.setText(_translate("Form", "Multiply"))
        self.divButton.setText(_translate("Form", "Divide"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

