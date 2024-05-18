from python_ui import P1_Ejemplo
import sys
from PyQt5 import uic, QtWidgets,QtGui
#qtCreatorFile = "P1_ejemplo.ui"  # Nombre del archivo aquí.
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


import Plantilla_Grafica as interfaz
import matplotlib as plt


class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.pushButton_2.clicked.connect(self.graficar)
        self.pushButton_3.clicked.connect(self.titulo)
        self.pushButton.clicked.connect(self.grilla)
        self.pushButton_4.clicked.connect(self.limpiar)

        self.comboBox.addItem("Estilo :", ":")
        self.comboBox.addItem("Estilo -", "-")
        self.comboBox.addItem("Estilo --", "--")
        self.comboBox.addItem("Estilo -.", "-.")
        self.comboBox.currentIndexChanged.connect(self.estiloLinea)

        self.comboBox_2.addItem("Negro :", "black")
        self.comboBox_2.addItem("Rojo :", "red")
        self.comboBox_2.addItem("Azul :", "blue")
        self.comboBox_2.addItem("Verde :", "green")
        self.comboBox_2.currentIndexChanged.connect(self.colorLinea)

        self.spinBox_7.setValue(1)
        self.spinBox_7.setMaximum(10)
        self.spinBox_7.setMinimum(1)
        self.spinBox_7.setSingleStep(1)
        self.spinBox_7.valueChanged.connect(self.anchoLinea)


    # Área de los Slots
    def graficar(self):
        pass

    def titulo(self):
        pass
    def grilla(self):
        pass

    def limpiar(self):
        pass

    def estiloLinea(self):
        pass

    def colorLinea(self):
        pass

    def anchoLinea(self):
        pass





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
