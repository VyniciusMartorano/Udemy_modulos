from datetime import datetime

data = datetime(2021,1,26,14,40,30)
                    #dia = '%d'     #hora = '%H'
                    # #mes = '%m'   #minuto = '%M'
                    #ano = '%Y'     #segundo = '%S'
print(data.strftime('%d/%m/%y %H:%M:%S'))

print(data.hour, data.day)

