import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P13_SeleccionEquipo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.rb_lex.clicked.connect(self.clic_lex)
        self.rb_lex.toggled.connect(self.toggle_lex)

        self.rb_nat.clicked.connect(self.clic_nat)
        self.rb_nat.toggled.connect(self.toggle_nat)

        self.rb_vic.clicked.connect(self.clic_vic)
        self.rb_vic.toggled.connect(self.toggle_vic)

        self.rb_poio.clicked.connect(self.clic_yo)
        self.rb_poio.toggled.connect(self.toggle_yo)

    # Área de los Slots
    def clic_lex(self):
        print("hiciste clic a lesis")

    def toggle_lex(self):
        estado = self.rb_lex.isChecked()
        print(f"Lex cambio de estado (toggle). Nuevo Estado: {estado}")
        self.txt_integrante.setText("Lexiss")

    def clic_nat(self):
        print("hiciste clic a Natalia")

    def toggle_nat(self):
        estado = self.rb_nat.isChecked()
        print(f"Natalia cambio de estado (toggle). Nuevo Estado: {estado}")
        self.txt_integrante.setText("Natalia")

    def clic_vic(self):
        print("hiciste clic a Victor")

    def toggle_vic(self):
        estado = self.rb_vic.isChecked()
        print(f"Victor cambio de estado (toggle). Nuevo Estado: {estado}")
        self.txt_integrante.setText("Victor")

    def clic_yo(self):
        print("hiciste clic a Rodrigo")

    def toggle_yo(self):
        estado = self.rb_poio.isChecked()
        print(f"Rodrigo cambio de estado (toggle). Nuevo Estado: {estado}")
        self.txt_integrante.setText("Rodrigo")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

