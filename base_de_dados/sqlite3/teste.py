import sqlite3

#cria a base de dados
#caminho
conexao = sqlite3.connect(r'C:\Users\vynic\Videos\BD_dados.db')
cursor = conexao.cursor()

comand = 'CREATE TABLE IF NOT EXISTS clientes(' \
         'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
         'nome TEXT,' \
         'peso REAL' \
         ')'
cursor.execute(comand,)

comand = 'INSERT INTO clientes (nome,peso) VALUES (?,?)'
cursor.execute(comand,('Vynicius martorano', 15.5))
conexao.commit()

cursor.close()
conexao.close()