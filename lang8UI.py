# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lang8UI.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(468, 585)
        self.randomButton = QtWidgets.QPushButton(Dialog)
        self.randomButton.setGeometry(QtCore.QRect(190, 540, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.randomButton.setFont(font)
        self.randomButton.setObjectName("randomButton")
        self.previousButton = QtWidgets.QPushButton(Dialog)
        self.previousButton.setGeometry(QtCore.QRect(110, 540, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.previousButton.setFont(font)
        self.previousButton.setObjectName("previousButton")
        self.nextButton = QtWidgets.QPushButton(Dialog)
        self.nextButton.setGeometry(QtCore.QRect(300, 540, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nextButton.setFont(font)
        self.nextButton.setObjectName("nextButton")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 60, 431, 471))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.currentPageDisplay = QtWidgets.QLabel(Dialog)
        self.currentPageDisplay.setGeometry(QtCore.QRect(30, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.currentPageDisplay.setFont(font)
        self.currentPageDisplay.setObjectName("currentPageDisplay")
        self.pageSearchButton = QtWidgets.QPushButton(Dialog)
        self.pageSearchButton.setGeometry(QtCore.QRect(390, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pageSearchButton.setFont(font)
        self.pageSearchButton.setObjectName("pageSearchButton")
        self.pageSearchLine = QtWidgets.QLineEdit(Dialog)
        self.pageSearchLine.setGeometry(QtCore.QRect(260, 10, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pageSearchLine.setFont(font)
        self.pageSearchLine.setObjectName("pageSearchLine")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Lang8 Yamasv\'s entries"))
        self.randomButton.setText(_translate("Dialog", "Random"))
        self.previousButton.setText(_translate("Dialog", "<"))
        self.nextButton.setText(_translate("Dialog", ">"))
        self.currentPageDisplay.setText(_translate("Dialog", "88/1400"))
        self.pageSearchButton.setText(_translate("Dialog", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

