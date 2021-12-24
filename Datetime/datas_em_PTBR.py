from datetime import datetime
from locale import LC_ALL, setlocale
setlocale(LC_ALL,'pt_BR.utf-8') #muda o idioma para o do local atual ou para o selecionado no segundo argumento
dt = datetime.now() #data atual
formatado = dt.strftime('%A, %d de %B de %Y')
print(formatado)

