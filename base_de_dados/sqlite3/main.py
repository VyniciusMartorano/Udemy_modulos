import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

"""
                #id é o identificador da tabela
#criar tabela
cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ') ')


#inserir registro na tabela
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?), ("Vynicius Martorano", 67.5)')


#adicionar dicionario (colocar dois pontos antes da variavel)
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome,:peso)',{'nome':'joaozinho','peso':87.4})


cursor.execute('INSERT INTO clientes VALUES (:id,:nome,:peso)',{'id':None,'nome':'Daniel Senna','peso':57.4})


#executar o cursor
conexao.commit()
"""

#mudar o nome pelo id do cliente usando dicionario
cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id',{'nome':'Italo chimpanzé', 'id':2})
conexao.commit()


#deletar um cliente da base de dados pelo id
cursor.execute('DELETE FROM clientes WHERE id=:id', {'id': 4})



#mostrar valores da tabela
cursor.execute('SELECT * FROM clientes')


"""
#buscar todos os valores
for linha in cursor.fetchall():
    identificador, nome, peso = linha
    print(identificador, nome, peso)

    '''print(f'ID: {identificador}'
          f'\nNome: {nome}'
          f'\nPeso: {peso}')'''
"""

#selecionar as pessoas que tiverem com peso maior que 60
cursor.execute('SELECT id, nome, peso FROM clientes WHERE peso > :limite', {'limite': 60})
for linha in cursor.fetchall():
    identificador, nome, peso = linha
    print(identificador,nome,peso)





cursor.close()
conexao.close()