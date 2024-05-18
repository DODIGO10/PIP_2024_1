#from python_ui import P2_Ejemplo
import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore


qtCreatorFile = "main_envioinfo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        #self.btn_saludar.clicked.connect(self.saludar)
        self.btn_suma.clicked.connect(self.sumar)


    # Área de los Slots
    def sumar(self):
        a = int(self.txt_a.text())
        b = int(self.txt_b.text())
        r = a + b
        self.dialogo = MyDialog()
        self.dialogo.setModal(True)
        self.dialogo.txt_resultado.setText(str(r))
        self.dialogo.show()
##########
qtCreatorFile3 = "second_envioinfo.ui"  # Nombre del archivo aquí.
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)


class MyDialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


