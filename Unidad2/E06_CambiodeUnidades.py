import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "E06_CambiodeUnidades.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_masa.clicked.connect(self.convertir_masa)
        self.btn_longitud.clicked.connect(self.convertir_longitud)
        self.btn_temperatura.clicked.connect(self.convertir_temperatura)
        self.btn_limpiar.clicked.connect(self.limpiar)

        self.txt_gramos.setEnabled(False)
        self.txt_libras.setEnabled(False)

        self.txt_centimetros.setEnabled(False)
        self.txt_pies.setEnabled(False)

        self.txt_fahrenheit.setEnabled(False)
        self.txt_kelvin.setEnabled(False)

    # Área de los Slots
    def convertir_masa(self):
        valor_original = float(self.txt_masa.text())


        valor_gramos = valor_original * 1000
        valor_libras = valor_original * 2.204
        self.txt_gramos.setText(str(valor_gramos))
        self.txt_libras.setText(str(valor_libras))

    def convertir_longitud(self):
        valor_original = float(self.txt_longitud.text())

        valor_centimetros = valor_original * 100
        valor_pies = valor_original * 3.28084

        self.txt_centimetros.setText(str(valor_centimetros))
        self.txt_pies.setText(str(valor_pies))

    def convertir_temperatura(self):
        valor_original = float(self.txt_temperatura.text())

        valor_fahrenheit = (valor_original * 9 / 5) + 32
        valor_kelvin = valor_original + 273.15

        self.txt_fahrenheit.setText(str(valor_fahrenheit))
        self.txt_kelvin.setText(str(valor_kelvin))


    def limpiar(self):

        self.txt_gramos.setText("")
        self.txt_libras.setText("")
        self.txt_masa.setText("")

        self.txt_centimetros.setText("")
        self.txt_pies.setText("")
        self.txt_longitud.setText("")

        self.txt_fahrenheit.setText("")
        self.txt_kelvin.setText("")
        self.txt_temperatura.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())