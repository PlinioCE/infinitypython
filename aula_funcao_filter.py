"""
Sintaxe função filter
filter(<função>, <iteraveis>)
"""


def dentro_orcamento(lista):
    compras= []
    for preco in lista:
        if preco < 15:
            compras.append(preco)
    return compras


def verificar_preco(preco):
    if preco < 15:
        return preco
    else:
        return False


precos = [9.99, 15.50, 17.5, 20.89, 12.66, 8.81]
print(f'Produtos < R$ 15,00 : {dentro_orcamento(precos)}')

pode_comprar = list(filter(lambda preco: preco if preco < 15 else False, precos))
print(f'Produtos < 15 com filter: {pode_comprar}')

pode_comprar_2 = list(filter(verificar_preco, precos))
