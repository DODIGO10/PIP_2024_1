import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "E4_Semaforo.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.rojo = QtGui.QColor(255, 0, 0)
        self.amarillo = QtGui.QColor(255, 255, 0)
        self.verde = QtGui.QColor(0, 255, 0)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.CambiarColores)

        self.current_state = "verde"
        self.Colores()

        self.btn_iniciar.clicked.connect(self.IniciarDetener)

    # Área de los Slots
    def IniciarDetener(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn_iniciar.setText("Iniciar")
        else:
            self.timer.start(5000)
            self.btn_iniciar.setText("Detener")
    def CambiarColores(self):
        if self.current_state == "verde":
            self.current_state = "amarillo"
            self.timer.start(2000)
        elif self.current_state == "amarillo":
            self.current_state = "rojo"
            self.timer.start(5000)
        else:
            self.current_state = "verde"
            self.timer.start(5000)

        self.Colores()

    def Colores(self):
        if self.current_state == "verde":
            self.lbl_rojo.setStyleSheet("background-color: black; border-radius: "
                                        "50; border: 1px solid ;")
            self.lbl_amarillo.setStyleSheet("background-color: black; "
                                            "border-radius: 50; border: 1px solid ;")
            self.lbl_verde.setStyleSheet("background-color: %s; black; border-radius: "
                                         "50; border: 1px solid ;" % self.verde.name())
        elif self.current_state == "amarillo":
            self.lbl_rojo.setStyleSheet("background-color: black; black; border-radius: "
                                        "50; border: 1px solid ;")
            self.lbl_amarillo.setStyleSheet("background-color: %s; black; border-radius: "
                                            "50; border: 1px solid ;"  % self.amarillo.name())
            self.lbl_verde.setStyleSheet("background-color: black; black; border-radius: "
                                         "50; border: 1px solid ;")
        else:
            self.lbl_rojo.setStyleSheet("background-color: %s; black; border-radius: "
                                        "50; border: 1px solid ;" % self.rojo.name())
            self.lbl_amarillo.setStyleSheet("background-color: black; black; border-radius: "
                                            "50; border: 1px solid ;")
            self.lbl_verde.setStyleSheet("background-color: black; black; border-radius: "
                                         "50; border: 1px solid ;")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())