import pymysql.cursors

"""
OPERAÇÕES POSSIVEIS COM A BASE DE DADOS
CRUID - CREATE - READ - UPDATE - DELETE
"""






conexao = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    db='clientes',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

'''with conexao.cursor() as cursor:
    sql = 'INSERT OR IGNORE INTO clientes (nome, sobrenome) VALUES (%s,%s)'
    cursor.execute(sql, ('Jack', 'Sparrow'))
    cursor.execute(sql, ('Vynicius', 'Martorano'))
    conexao.commit()  #enviar dados para a base de dados
'''


'''
Para enviar mais de um valor é preciso usar o .executemany( [lista] ) que recebe uma lista

with conexao.cursor() as cursor:
   sql = 'INSERT INTO clientes (nome, sobrenome) VALUES (%s,%s)'
   dados = [
       ('joao', 'neto'),
       ('cleiton', ' MARTORANO'),
       ('sanssao', 'natan')
   ]
   cursor.executemany(sql, dados)
   conexao.commit()
'''

'''
DELETAR UM VALOR PELO ID

with conexao.cursor() as cursor:
    sql = 'DELETE FROM clientes WHERE id=%s'
    cursor.execute(sql, (18,))
    conexao.commit()
'''

'''
DELETAR MAIS DE UM VALOR PELO ID

with conexao.cursor() as cursor:
    sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
    cursor.execute(sql, (17,19,20))
    conexao.commit()
'''

'''
MUDAR VALOR PELO ID

with conexao.cursor() as cursor:
    sql = 'UPDATE clientes SET sobrenome=%s WHERE id=%s'
    cursor.execute(sql, ('Otavio', 1))
    conexao.commit()
'''


with conexao.cursor() as cursor:#selecione tudo de clientes em ordem crescente ordene pelo id com limite de 100 pessoas
    cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100') #ASC = crescente, DESC = decrescente
    resultado = cursor.fetchall()
    with open('dados.txt','w') as arq:
        for linha in resultado:
            arq.write(f"{linha['id']},{linha['nome']}, {linha['sobrenome']}, {linha['idade']}, {linha['peso']}\n")
            print(linha['id'],linha['nome'], linha['sobrenome'], linha['idade'], linha['peso'])
            #id, nome, sobrenome, idade, peso = linha
            #print(id, nome, sobrenome, idade, peso)





cursor.close()
conexao.close()