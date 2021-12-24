from calendar import mdays
from datetime import datetime

dt = datetime.now()

mes_atual = int(dt.strftime('%m'))
print(f'O mes {mes_atual} tem {mdays[mes_atual]} dias') #mostra a quantidade de dias do mes_atual

print(mes_atual)

'''
print(mdays)
retorna:
[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
'''