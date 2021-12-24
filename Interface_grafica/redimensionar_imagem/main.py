import sys
from Interface_grafica.redimensionar_imagem.arquivo import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class Novo(QMainWindow, Ui_mainwindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.abrir_imagem())    #quando clicar no botao execute a função abrir_imagem


    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Imagem',
            r'C:\Users\vynic\Pictures\imagens',
        )
        self.inputAbrirArquivo.setText(imagem)
        self.original_Img = QPixmap(imagem)
        self.labelImg.setPixmap(self.original_Img)
        self.inputLargura.setText(str(self.original_Img.width()))
        self.inputAltura.setText(str(self.original_Img.height()))

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()
