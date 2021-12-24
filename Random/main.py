import random
import string


# escolhe um numero entre A e B
inteiro = random.randint(1, 10)

# gerar um numero aleatorio usando a função range()
aleatorio = random.randrange(900, 1000, 10)

# gera um numero de ponto flutuante entre A e B
flutuante = random.uniform(1, 10)

# gera um numero de ponto flutuante entre 0 e 1
floatt = random.random()

#escolher uma opção em uma lista
lista = ['maria', 'joao','vitor','italo', 'joana','sanssao']
sorteio = random.choice(lista)

#escolher x opções em uma lista
lista2 = ['maria', 'joao','vitor','italo', 'joana','sanssao']
sorteio2 = random.choices(lista2, k=2)  #sortear 2 itens da lista
#se quiser que os itens nao se repitam no mesmo sorteio usar:
#random.sample()

#embaralhar lista
random.shuffle(lista2)

#gerar senha aleatoria
letras = string.ascii_letters
digitos = string.digits
caracteres = '$#%&*_-.'
geral = letras + digitos + caracteres
senha = ''.join(random.choices(geral, k=10))
print(senha)




