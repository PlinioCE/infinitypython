from random import randint
from time import sleep

lista_sorteio = []

while len(lista_sorteio) < 6:
    dezena = randint(1, 60)
    if dezena not in lista_sorteio:
        lista_sorteio.append(dezena)
    else:
        continue

lista_sorteio_ordem = sorted(lista_sorteio)
# print(lista_sorteio_ordem)
print()
print('-' * 15, ' MEGA DA VIRADA 2022 ', '-' * 15)

lista_numeros = []

contador = 1
while len(lista_numeros) < 6:
    numero = int(input(f'Informe a {contador}ª dezena: '))
    if numero not in lista_numeros:
        lista_numeros.append(numero)
        contador += 1
    else:
        print('Número já informado!')
print('-' * 53)
print('VAMOS AO SORTEIO!')
for indice in range(0, 6):
    print(f'{indice+1}ª dezena sorteada: {lista_sorteio[indice]}')
    sleep(5)

lista_numeros_ordem = sorted(lista_numeros)
# print(lista_numeros_ordem)
print()
print('-' * 15, ' MEGA DA VIRADA 2022 ', '-' * 15)
if lista_sorteio_ordem == lista_numeros_ordem:
    print(f'\nNÚMEROS SORTEADOS: {lista_sorteio_ordem}')
    print('\nPARABÉNS! VOCÊ É O MAIS NOVO MILIONÁRIO!!!')
else:
    print('\nCONFIRA SEU JOGO')
    print(f'NÚMEROS SORTEADOS: {lista_sorteio_ordem}'
          f'\nNÚMEROS APOSTADOS: {lista_numeros_ordem}')
