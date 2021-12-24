"""
Pilhas e Filas

Pilha (stack) - LIFO - last in, first out.
    Exemplo: Pilha de livros que são adicionados um sobre o outro

Fila (qeue) - FIFO - first in, first out.
    Exemplo: Uma fila de banco (ou qualquer fila da vida real)
Filas podem ter efeitos colaterais em desempenho, porque a cada item
alterado, todos os indices serão modificados.
"""
"""
PILHA

livros = list()
livros.append('Livro 1')        #1
livros.append('Livro 2')        #2
livros.append('Livro 3')        #3
livros.append('Livro 4')        #4
livros.append('Livro 5')        #5


                             #livro removido
livro_removido = livros.pop()   #5
livro_removido = livros.pop()   #4
livro_removido = livros.pop()   #3
livro_removido = livros.pop()   #2
livro_removido = livros.pop()   #1
                #o primeiro livro a entrar é o ultimo a sair

print(livros, livro_removido)
"""





"""
#A Primeira pessoa que entra na fila é a primeira a sair dela
from collections import deque
fila = deque(maxlen=5)

'Maxlen' é um argumento opcional para indicar o maximo
de elementos na listaz
"""
"""
fila.append('italo')
fila.append('vitor')
fila.append('marcos')
fila.append('mario')
fila.append('joao')
            #apaga o primeiro elemento da fila
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')

print()
print(f'Pessoas restantes: ')
for nome in fila:
    print(nome)
"""


"""
from collections import deque
fila = deque(maxlen=5)

fila.append('italo')
fila.append('vitor')
fila.append('marcos')
fila.append('mario')
fila.append('joao')
#ja que o maximo de itens permitidos na lista é 5,
#quando for adicionado outro item, o primeiro item
#a ser adicionado vai ser excluido.
#desta forma o item 'italo' vai ser excluido
fila.append('silvia')


for nome in fila:
    print(nome)
"""


from collections import deque
from time import sleep

'''fila = deque(maxlen=10)

for i in range(100):
    fila.append(i)
    print(fila)
    sleep(1)
'''
#inserir item na fila em um lugar especifico

fila = deque()
fila.extend([10,20,30,40,50,60])
#fila.insert(2,'vitor')
#print(fila.index(40))   #descobrir qual o indice que esta o valor 40
fila.rotate(1)     #colocar o ultimo elemento para o primeiro indice da fila
print(fila)





















