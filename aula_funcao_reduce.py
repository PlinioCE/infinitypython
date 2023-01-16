from functools import reduce
lista = [1, 2, 3, 4, 5, 6]

resultado = reduce(lambda x, y: x + y, lista)
print(resultado)