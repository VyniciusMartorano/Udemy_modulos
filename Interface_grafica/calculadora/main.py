import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy
from time import sleep


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculator of Martorano')   #mudar nome da janela
        self.setFixedSize(400, 400)     #deixar o tamanho da janela fixo
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)   #5 colunas
        self.display.setDisabled(True) #desativar a entrada de texto pelo display

        #estilo da janela
        self.display.setStyleSheet(
            '* {background: white; color: #000; font-size: 40px;}'
        )

        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)  #redimensiona automaticamente os botões de acordo com o espaço

        self.setCentralWidget(self.cw)

        self.add_btn(QPushButton('7'), 1, 0, 1, 1)  #ADICIONAR BOTAO
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)  #ADICIONAR BOTAO
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)  #ADICIONAR BOTAO
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)  #ADICIONAR BOTAO
        self.add_btn(
            QPushButton('C'), 1, 4, 1, 1,
            lambda: self.display.setText(''),'36c6d4'
        )  #ADICIONAR BOTAO

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)  # ADICIONAR BOTAO
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)  # ADICIONAR BOTAO
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)  # ADICIONAR BOTAO
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)  # ADICIONAR BOTAO
        self.add_btn(
            QPushButton('<--'), 2, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1]
            ), 'e41d1d'
        )  # ADICIONAR BOTAO

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)  # ADICIONAR BOTAO
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)  # ADICIONAR BOTAO
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)  # ADICIONAR BOTAO
        self.add_btn(QPushButton('/'), 3, 3, 1, 1)  # ADICIONAR BOTAO
        self.add_btn(QPushButton(''), 3, 4, 1, 1)  # ADICIONAR BOTAO

        self.add_btn(QPushButton('.'), 4, 2, 1, 1)  # ADICIONAR BOTAO
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)  # ADICIONAR BOTAO
        self.add_btn(QPushButton(''), 4, 0, 1, 1)  # ADICIONAR BOTAO
        self.add_btn(QPushButton('*'), 4, 3, 1, 1)  # ADICIONAR BOTAO
        self.add_btn(
            QPushButton('='), 4, 4, 1, 1,
            self.eval_igual, 'e88933'
        )

    def eval_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))  #eval avalia se a conta esta correta
            )
        except:
            self.display.setText('Conta inválida.')


    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, color=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)
        if color:
            btn.setStyleSheet(f'background: #{color}; font-weight: 700; color: #fff')

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()