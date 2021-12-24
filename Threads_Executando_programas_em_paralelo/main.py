from threading import Thread
from time import sleep
from threading import Lock


class MyThread(Thread):
    def __init__(self, texto,tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)



'''t1 = MyThread('Thread1', 3)
t1.start()

t2 = MyThread('Thread2', 5)
t2.start()

t3 = MyThread('Thread3', 8)
t3.start()
for i in range(10):
    print(i)
    sleep(1)'''

"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('hello word! 1',5))
t1.start()

while t1.is_alive():    #enquanto a thread estiver funcionando
    print('Esperando a thread finalizar.')    #execute tal coisa
    sleep(1)
print('Thread acabou!')
"""

class Ingresso:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire() #esse metodo so deixa passar 1 pedido por vez
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release() #liberar para passsar mais pedidos
            return
        sleep(1/2)
        print(f'Voce comprou {quantidade} ingresso(s).'
              f'Ainda temos {self.estoque-quantidade}')
        self.estoque -= quantidade
        self.lock.release() #libera a passagem para mais pedidos




ingressos = Ingresso(10)
threads = []
for i in range(1,20):
    t = Thread(target=ingressos.comprar, args=(i,))
    threads.append(t)

for t in threads:
    t.start()

executando = True
while executando:
    executando = False

    for t in threads:
        if t.is_alive():
            executando = True

print(ingressos.estoque)


