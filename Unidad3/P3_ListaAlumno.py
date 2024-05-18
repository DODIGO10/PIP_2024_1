import P2_LeerArchivo as moduloArchivo

import sys
from PyQt5 import uic, QtWidgets,QtGui
qtCreatorFile = "P3_ListaAlumnos.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        b = moduloArchivo.cargarArchivo()
        print("desde p3")
        print(b)

        for elemento in b:
            self.listWidget.addItem(elemento[0])


    # Área de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

