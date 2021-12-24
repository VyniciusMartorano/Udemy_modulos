import sqlite3

class TabelaPreços:
    def __init__(self,arquivo):
        #self.conn = conexão com o server
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def registraproduto(self, NomeProduto, preço):
        comando = 'INSERT INTO dados (produto, preço) VALUES (?,?)'
        try:
            self.cursor.execute(comando, (NomeProduto, preço))
        except:
            print('O produto já esta Registrado!')
        self.conn.commit()

    def mostratabela(self):
        comando = 'SELECT * FROM dados'
        self.cursor.execute(comando)
        for linha in self.cursor.fetchall():
            id, nome, preço = linha
            print(f'ID: {id}, Nome: {nome}, Preço: R${preço}')

    def calcula(self,id, quant):
        comando = 'SELECT preço FROM dados WHERE id=?'
        self.cursor.execute(comando, (id,))
        for linha in self.cursor.fetchall():
            saida = linha[0] * quant
            print(saida)

    def deletaproduto(self,id):
        for linha in self.cursor.fetchall():
            comando = 'DELETE FROM dados WHERE id=?'
            self.cursor.execute(comando, (id,))
            self.conn.commit()
            print(f'{linha[1]} foi excluido do sistema')


    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    tabela = TabelaPreços('tabela.db')
    tabela.mostratabela()
    tabela.fechar()