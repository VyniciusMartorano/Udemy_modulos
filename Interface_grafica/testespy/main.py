import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from testespy.tela1 import *
from testespy.tela2 import *




class Janela2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Janela2()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        self.origem = Tela()
        self.origem.show()
        event.accept()



class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.jan1 = Ui_Janela1()    #self.jan1 sera usado para manipular oque tem dentro
        self.jan1.setupUi(self)

        self.jan2 = Janela2()


        self.jan1.button_tela.clicked.connect(self.mudajanela)

    def mudajanela(self):
        self.jan2.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    tela = Tela()
    tela.show()
    sys.exit(app.exec_())


