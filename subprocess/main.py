import subprocess

#windows -- ping

proc = subprocess.run([             #util para monitorar servidores
    'ping','187.60.88.13'],capture_output=True,text=True
                        #vai mandar a saida de dados
)                       #para 'proc.stdout'
                                                #text=True para a saida ser em
                                                #formatado de texto
saida = proc.stdout
print(saida)