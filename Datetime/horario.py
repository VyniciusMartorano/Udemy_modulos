from datetime import datetime

#pega a data e horario atual 
date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(date)