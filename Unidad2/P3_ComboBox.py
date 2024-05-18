import sys
from PyQt5 import uic, QtWidgets,QtGui
qtCreatorFile = "P3_ComboBox.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_personas = {
            1: ["lex", "lol", 13, "o+", ":/Logos/Imagenes/WhatsApp Image 2024-02-15 at 8.14.59 PM.jpeg"],
            2: ["nat", "nier", 69, "b+", ":/Logos/Imagenes/WhatsApp Image 2024-02-15 at 8.48.55 PM.jpeg"],
            3: ["vic", "ver f1", 12, "a+", ":/Logos/Imagenes/WhatsApp Image 2024-02-15 at 8.48.55 PM (1).jpeg"],
            4: ["poio", "jugar valo", 1, "p+", ":/Logos/Imagenes/WhatsApp Image 2024-02-15 at 8.48.55 PM (2).jpeg"]
        }

        self.combo_personas.addItem("lex", 1)
        self.combo_personas.addItem("nat", 2)
        self.combo_personas.addItem("vic", 3)
        self.combo_personas.addItem("poio", 4)

        self.combo_personas.currentIndexChanged.connect(self.cambia)

    # Área de los Slots
    def cambia(self):
        print("text" + self.combo_personas.currentText())
        print("index:" + str(self.combo_personas.currentIndex()))
        print("data:" + str(self.combo_personas.currentData()))

        dataClave = self.combo_personas.currentData()
        imagen = self.datos_personas[dataClave][-1]
        self.img_persona_4.setPixmap(QtGui.QPixmap(imagen))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())