"""
PyQT é um toolkit desenvolvido em C++ utilizado por vários programas para
criação de aplicações GUI (Interface Gráfica). Também inclui diversas
funcionalidades, como: acesso a base de dados, threads, comunicação de rede,
etc...
pip install pyqt5
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout

class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Texto do botão')
        self.btn.setStyleSheet('font-size: 30px')
        self.btn.clicked.connect(lambda: print('Hello, World!'))
        self.btn.setStyleSheet('background-color: rgb(30,24,76)')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()





