from python_ui import P2_Ejemplo
import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore


#qtCreatorFile = "P1_ejemplo.ui"  # Nombre del archivo aquí.
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, P2_Ejemplo.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        P2_Ejemplo.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        #self.btn_saludar.clicked.connect(self.saludar)

        self.btn_nuevo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_nuevo.setGeometry(QtCore.QRect(330,70,191,61))
        self.btn_nuevo.setObjectName("btn_nuevo")

        self.btn_nuevo.setText("NUEVO SALUDO")

        self.btn_saludar.clicked.connect(self.saludar)


    # Área de los Slots
    def saludar(self):
        try:

            self.lineEdit.setText("hola")

            self.btn_nuevo.hide()

        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

