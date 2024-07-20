# Try, except, else e finally

try:
    a = 18
    b = 0
    c = a / b 
except ZeroDivisionError as error:
    print(f'ERROR: {error} / NAME ERROR: {error.__class__.__name__}')
except NameError:
    print('Variável não declarada.')

print('Programa continua.')