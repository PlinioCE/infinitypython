"""1. Considere a seguinte lista = [11, 12, 13, 15, 21, 50, 42, 62].
Utilize a função filter para gerar uma nova lista apenas com números pares."""


def listar_pares(lista):
    pares = []
    for numeros in lista:
        if numeros % 2 == 0:
            pares.append(numeros)
    return pares


lista_numeros = [11, 12, 13, 15, 21, 50, 42, 62]
print(f'Lista de números pares: {listar_pares(lista_numeros)}')

pares = list(filter(lambda pares: pares if pares % 2 == 0 else False, lista_numeros))
print(f'Lista pares com filter: {pares}')
print()


"""2. Considere a seguinte lista de nomes = ["Abrãao", "Amanda", "Vanessa", "João", "Emanuel", "Alex"],
utilize a função filter para criar uma nova lista com apenas os nomes das pessoas que iniciam com vogal."""


def nome_vogal(nome):
    lista_vogal = []
    for vogal in nome:
        if vogal[0] in 'AaEeIiOoUu':
            lista_vogal.append(vogal)
    return lista_vogal


nomes = ["Abrãao", "Amanda", "Vanessa", "João", "Emanuel", "Alex"]
print(f'Lista de nomes iniciados com vogal: {nome_vogal(nomes)}')


# def filtroNome(nome):
#     if nome[0].upper() in "AEIOU":
#         return nome
#     else:
#         return False
#
# nomes = ["Abrãao", "Amanda", "Vanessa", "João", "Emanuel", "Alex"]
# nomesVogais = list(filter(filtroNome, nomes))
# print(f'Nomes com vogais = {nomesVogais}')
#
# nomes_iniciados_vogal = list(filter(lambda vogal: vogal if vogal in 'AaEeIiOoUu' else False, nomes))
# print(f'Lista de nomes vogais com filter: {nomes_iniciados_vogal}')
