from random import choices

# simulação da função 'sample'

lista = ['maria', 'joao', 'vitor', 'italo', 'joana', 'sanssao']
while True:
    sorteio = choices(lista, k=2)
    if sorteio[0] == sorteio[1]:
        continue
    else:
        print(sorteio)
        break
