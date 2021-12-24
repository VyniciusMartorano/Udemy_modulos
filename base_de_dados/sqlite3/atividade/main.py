import sqlite3

class Registro:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self,nome, telefone):
        consultar = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?,?)'
        self.cursor.execute(consultar, (nome, telefone))
        self.conn.commit()


    def buscar(self, valor):
        consultar = 'SELECT * FROM agenda WHERE nome LIKE?'
        self.cursor.execute(consultar, (f'%{valor}%',))
        print(f'Chave de busca "{valor}"')
        for linha in self.cursor.fetchall():
            id, nome, telefone = linha
            print(id, nome, telefone)

    def listavalores(self):
        self.cursor.execute('SELECT * FROM agenda')
        for linha in self.cursor.fetchall():
            id, nome, telefone = linha
            print(id, nome, telefone)


if __name__ == '__main__':
    registro = Registro('agenda.db')
    registro.inserir('italo',1111)
    registro.inserir('marcos luiz', 2222)
    registro.inserir('vyni luiza cius', 3333)
    registro.inserir('jose caludo', 4444)
    registro.buscar('luiz')