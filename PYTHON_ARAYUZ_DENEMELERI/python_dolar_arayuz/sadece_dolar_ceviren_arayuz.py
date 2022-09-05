from PyQt5.QtWidgets import*
from PyQt5.QtCore import pyqtSlot
from my_guim import Ui_MainWindow
from dolarverisi import float_dolar


class dersler_7(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.dolar_label.setText(str(float_dolar)+ " $" )



    def on_cevir_buton_clicked(self):
        a = float(self.ui.textEdit.toPlainText())*float_dolar
        b= str(a)
        self.ui.cevrilen_dolar.setText(b +" TL")



















uygulama = QApplication([])
pencere = dersler_7()
pencere.show()
uygulama.exec_()