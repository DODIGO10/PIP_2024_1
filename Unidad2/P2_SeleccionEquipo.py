import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P2_SeleccionEquipo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        #self.text_equipo.setText("hola \n mundo")
        self.cb_lex.toggled.connect(self.sel_lex)
        self.cb_nat.toggled.connect(self.sel_nat)
        self.cb_vic.toggled.connect(self.sel_vic)
        self.cb_poio.toggled.connect(self.sel_poio)

        self.lex = ""
        self.nat = ""
        self.vic = ""
        self.poio = ""

    # Área de los Slots
    def sel_lex(self):
        if self.cb_lex.isChecked():
            print("lex true")
            self.lex = "lex"
        else:
            print("lex false")
            self.lex = ""
        self.text_equipo.setPlainText(self.lex + self.nat + self.vic + self.poio)

    def sel_nat(self):
        if self.cb_nat.isChecked():
            print("nat true")
            self.nat = "\nnat"
        else:
            print("nat false")
            self.nat = ""
        self.text_equipo.setPlainText(self.lex + self.nat + self.vic + self.poio)

    def sel_vic(self):
        if self.cb_vic.isChecked():
            print("vic true")
            self.vic = "\nvic"
        else:
            print("vic false")
            self.vic = ""
        self.text_equipo.setPlainText(self.lex + self.nat + self.vic + self.poio)

    def sel_poio(self):
        if self.cb_poio.isChecked():
            print("poio true")
            self.poio = "\npoio"
        else:
            print("poio false")
            self.poio = ""
        self.text_equipo.setPlainText(self.lex + self.nat + self.vic + self.poio)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

