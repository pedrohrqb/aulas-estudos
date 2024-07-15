# Mapppeamento de dados em list comprehension

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    produto
    for produto in produtos
]

# o '*' É o desempacotamento, assim a lista fica ordenada.
print(*novos_produtos, sep='\n') # o 'sep' junto com o desempacotamento, usa o quebra-linha para enfileirar a lista.