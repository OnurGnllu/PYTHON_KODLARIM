# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Belgelerim/KodÇalışmalarım/PYTHON_KODLARIM/PYTHON_ARAYUZ_DENEMELERI/python_ilkarayuz/my_gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 299)
        MainWindow.setMinimumSize(QtCore.QSize(400, 299))
        MainWindow.setMaximumSize(QtCore.QSize(400, 299))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 110, 71, 21))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 80, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 110, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.cevrilen_dolar = QtWidgets.QLabel(self.centralwidget)
        self.cevrilen_dolar.setGeometry(QtCore.QRect(170, 110, 47, 13))
        self.cevrilen_dolar.setText("")
        self.cevrilen_dolar.setObjectName("cevrilen_dolar")
        self.cevir_buton = QtWidgets.QPushButton(self.centralwidget)
        self.cevir_buton.setGeometry(QtCore.QRect(160, 160, 80, 21))
        self.cevir_buton.setObjectName("cevir_buton")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(20, 20, 174, 16))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.doviz_guncel_label = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doviz_guncel_label.setFont(font)
        self.doviz_guncel_label.setObjectName("doviz_guncel_label")
        self.dolar_label = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dolar_label.setFont(font)
        self.dolar_label.setObjectName("dolar_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Dolar - TL Kur Dönüşümü"))
        self.label_2.setText(_translate("MainWindow", "="))
        self.cevir_buton.setText(_translate("MainWindow", "Çevir"))
        self.doviz_guncel_label.setText(_translate("MainWindow", "<html><head/><body><p>Güncel Dolar Fiyatı =</p></body></html>"))
        self.dolar_label.setText(_translate("MainWindow", "TextLabel"))

