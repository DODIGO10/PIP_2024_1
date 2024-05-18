import sys
from PyQt5 import uic, QtWidgets,QtGui
qtCreatorFile = "P1_DescripcionImagenes.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_personas = {
            1:["lex","lol",21,"o+",":/Logos/Imagenes/WhatsApp Image 2024-02-15 at 8.14.59 PM.jpeg"],
            2: ["nat", "nier", 20, "b+",":/Logos/Imagenes/WhatsApp Image 2024-02-15 at 8.48.55 PM.jpeg"],
            3: ["vic", "ver f1", 20, "a+",":/Logos/Imagenes/WhatsApp Image 2024-02-15 at 8.48.55 PM (1).jpeg"],
            4: ["poio", "jugar valo", 21, "p+",":/Logos/Imagenes/WhatsApp Image 2024-02-15 at 8.48.55 PM (2).jpeg"]
        }
        self.btn_atras.clicked.connect(self.atras)
        self.btn_adelante.clicked.connect(self.adelante)
        self.index_control = 0

        self.btn_atras.setEnabled(False)

    # Área de los Slots
    def atras(self):
        if self.index_control > 1:
            self.index_control -= 1
            datos = self.datos_personas[self.index_control]
            print(datos)
            self.btn_adelante.setEnabled(True)
            self.img_persona.setPixmap(QtGui.QPixmap(datos[-1]))
            self.txt_nombre.setText(datos[0])
            self.txt_pasatiempo.setText(datos[1])
            self.txt_edad.setText(str(datos[2]))
            self.txt_tipodesangre.setText(datos[3])

        if  self.index_control == 1:
            self.btn_atras.setEnabled(False)

    def adelante(self):
        if self.index_control < 4:
            self.btn_atras.setEnabled(True)
            self.index_control += 1
            datos = self.datos_personas[self.index_control]
            print(datos)
            self.img_persona.setPixmap(QtGui.QPixmap(datos[-1]))
            self.txt_nombre.setText(datos[0])
            self.txt_pasatiempo.setText(datos[1])
            self.txt_edad.setText(str(datos[2]))
            self.txt_tipodesangre.setText(datos[3])

        if self.index_control == 4:
            self.btn_adelante.setEnabled(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

