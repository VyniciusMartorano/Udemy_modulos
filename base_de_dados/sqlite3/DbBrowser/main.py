import sqlite3

class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?,?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda set nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self,id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda ')
        for linha in self.cursor.fetchall():
            id, nome, telefone = linha
            print(id, nome, telefone)

    def fechar(self):
        self.cursor.close()
        self.conn.close()

"""
agenda.inserir('Vynicius', '111111')
agenda.inserir('Maria', '222222')
agenda.inserir('Rose', '333333')
agenda.inserir('Guilherme', '444444')
agenda.inserir('José', '555555')
"""

if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    try:
        agenda.listar()
        print()


    except:
        print('Esse cadastro já existe')