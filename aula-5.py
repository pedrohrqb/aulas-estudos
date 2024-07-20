# Try, except, else e finally

try: 
    print('Abriu o arquivo')
    # 8/0
except ZeroDivisionError:
    print('Error: Tentou dividir por 0')
else:
    print('Nenhum Error encontrado.')
finally: # O finally sempre será executado mesmo que ocorra um error.
    print('Fechou o arquivo')