from datetime import datetime, timedelta

#timestamp transforma a data em um numero

data = datetime.strptime('10/09/2021 20:00:00', '%d/%m/%Y %H:%M:%S')   #setar data e formato
print(data)
'''data = data + timedelta(days=5)     #adicionar 5 dias a 'data'
data = data + timedelta()'''
print('data formatada:')
print(data.strftime('%d/%m/%Y %H:%M:%S'))
