from PyQt5.QtWidgets import*
from PyQt5.QtCore import pyqtSlot
from my_ui import Ui_MainWindow
from get_units import get_dolar, get_sterlin ,get_euro
from MYSQL_adapter import veri_gonder


class dersler_7(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



    def on_cevir_buton_clicked(self):
        a = float(self.ui.dolar_label.text())
        b = self.ui.textEdit.toPlainText()
        c = round(float(a)*float(b),3)
        self.ui.cevrilen_dolar.setText(str(c) +" TL")



    def on_comboBox_currentTextChanged(self):
        if (self.ui.comboBox.currentText() == "Dolar"):
            guncel_parabirimi = get_dolar()
            veri_gonder(1,get_dolar(),'2012-05-05')
            self.ui.dolar_label.setText(str(guncel_parabirimi))

        elif (self.ui.comboBox.currentText() == "Euro"):
            guncel_parabirimi = get_euro()
            veri_gonder(1, get_euro(), '2012-05-05')
            self.ui.dolar_label.setText(str(guncel_parabirimi))

        elif (self.ui.comboBox.currentText() == "Sterlin"):
            guncel_parabirimi = get_sterlin()
            veri_gonder(1, get_sterlin(), '2012-05-05')
            self.ui.dolar_label.setText(str(guncel_parabirimi))

        else:
            guncel_parabirimi = 0
            self.ui.dolar_label.setText(str(guncel_parabirimi))





uygulama = QApplication([])
pencere = dersler_7()
pencere.show()
uygulama.exec_()