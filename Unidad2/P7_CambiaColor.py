import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P7_CambiarColor.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        #self.text_equipo.setText("hola \n mundo")

        self.lex = ""
        self.nat = ""
        self.vic = ""
        self.poio = ""

        self.ValorR.setMinimum(0)
        self.ValorR.setMaximum(255)
        self.ValorR.setSingleStep(1)
        self.ValorR.setValue(0)
        self.ValorR.valueChanged.connect(self.cambiaR)

        self.ValorG.setMinimum(0)
        self.ValorG.setMaximum(255)
        self.ValorG.setSingleStep(1)
        self.ValorG.setValue(0)
        self.ValorG.valueChanged.connect(self.cambiaG)

        self.ValorB.setMinimum(0)
        self.ValorB.setMaximum(255)
        self.ValorB.setSingleStep(1)
        self.ValorB.setValue(0)
        self.ValorB.valueChanged.connect(self.cambiaB)

        self.R = 0
        self.G = 0
        self.B = 0

    # Área de los Slots
    def cambiaR(self):
        self.R = self.ValorR.value()
        estilo = ("background-color: rgb(" + str(self.R) + "," + str(self.G) + "," + str(self.B) + ");")
        self.colorburguer.setStyleSheet(estilo)
        self.txt_R.setText(str(self.R))


    def cambiaG(self):
        self.G = self.ValorG.value()
        estilo = ("background-color: rgb(" + str(self.R) + "," + str(self.G) + "," + str(self.B) + ");")
        self.colorburguer.setStyleSheet(estilo)
        self.txt_G.setText(str(self.G))

    def cambiaB(self):
        self.B = self.ValorB.value()
        estilo = ("background-color: rgb("+str(self.R)+","+str(self.G)+","+str(self.B)+");")
        self.colorburguer.setStyleSheet(estilo)
        self.txt_B.setText(str(self.B))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())