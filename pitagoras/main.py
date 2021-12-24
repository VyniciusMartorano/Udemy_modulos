import sys
from pitagoras.arquivo import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from math import sqrt

class Pitagoras(QMainWindow, Ui_QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.calcular.clicked.connect(self.mostradisplay)
        self.calcular.clicked.connect(self.fazconta)

    
    def fazconta(self):
        hipo = self.inputHipo.text()
        cat1 = self.inputCateto1.text()
        cat2 = self.inputCateto2.text()
        #quando as caixas de 'hipo, cat1 e cat2' estão vazias elas retornam: ''
        if hipo == '' and cat1 == '' and cat2 == '':
            hipo = cat1 = cat2 = 0
        elif hipo == '' and float(cat1) > 0 and float(cat2) > 0:
            hipo = 0
        elif cat1 == '' and float(hipo) > 0 and float(cat2) > 0:
            cat1 = 0
        elif cat2 == '' and float(hipo) > 0 and float(cat1) > 0:
            cat2 = 0




        try:
            hipo = float(hipo)
            cat1 = float(cat1)
            cat2 = float(cat2)
        except:
            self.Resultado.setText('Calculo inválido.')
        else:
            if hipo == 0 and cat1 == 0 and cat2 == 0:
                self.Resultado.setText('Faltam valores.')
                return

            if hipo == 0:
                try:
                    result = sqrt(cat1**2 + cat2**2)
                    self.Resultado.setText(f'Hipo = {result}')
                except:
                    self.Resultado.setText('Erro')

            elif cat1 == 0:
                try:
                    result = sqrt(cat2**2 - hipo**2)
                    self.Resultado.setText(f'Cat1 = {result}')
                except:
                    self.Resultado.setText('Erro')

            elif cat2 == 0:
                try:
                    result = sqrt(hipo**2 + cat1**2)
                    self.Resultado.setText(f'Cat2 = {result}')
                except:
                    self.Resultado.setText('Erro')



    def mostradisplay(self,hipo=0,cat1=0,cat2=0):
        hipo = self.inputHipo.text()
        if hipo == '':
            hipo = 'Hipo'
        cat1 = self.inputCateto1.text()
        if cat1 == '':
            cat1 = 'Cat1'
        cat2 = self.inputCateto2.text()
        if cat2 == '':
            cat2 = 'Cat2'
        self.display.setText(f'{hipo}**2 = {cat1}**2 + {cat2}**2')



if __name__ == "__main__":
    qt = QApplication(sys.argv)
    pita = Pitagoras()
    pita.show()
    qt.exec_()
