"""
1. Considere as seguintes listas de bases = [10, 2, 5, 7, 8] e alturas = [5, 7, 6, 6, 5.5]
Utilize a função map para gerar uma nova lista com as áreas dos triangulos
area = base * altura / 2
"""

bases = [10, 2, 5, 7, 8]
alturas = [5, 7, 6, 6, 5.5]
areas_tri = list(map(lambda b, h: round(b * h / 2, 2), bases, alturas))

print(f'Áreas triângulos: {areas_tri}')

# def areas_triangulos(base):
#     areas = []
#     for valor in base:
#         area = base(valor) / 2
#         areas.append(area)
#     return areas
#
#
# bases = [10, 2, 5, 7, 8]
# alturas = [5, 7, 6, 6, 5.5]
# print(f'Áreas dos triângulos: {areas_triangulos(bases)}')

print()
"""
2. Considere as seguintes listas de pesos = [70, 50.6, 89.7, 45.5, 55] e alturas = [1.80, 1.54, 1.81, 1.47, 1.66]
utilize a função map para criar uma nova lista com os IMCs desses usuários
IMC = peso / altura ** 2
"""


def calcular_imc(peso, altura):
    imc = peso / altura ** 2
    return round(imc, 2)


alturas = [1.80, 1.54, 1.81, 1.47, 1.66]
pesos = [70, 50.6, 89.7, 45.5, 55]
imcs = list(map(calcular_imc, pesos, alturas))
print(f"IMCs = {imcs}")
print()
"""
3. Considere as seguintes listas de velocidade media = [100, 110, 80, 85, 90],
tempo em horas = [1, 2, 1, 3, 1] e consumo = [12, 10, 15, 13, 11].
Crie uma função que irá calcular a distancia percorrida baseado nas listas de tempo e velocidade.
Em seguida crie uma nova lista com a quantidade de litros gastos na viagem. 
"""
velocidade_media = [100, 110, 80, 85, 90]
tempo_em_horas = [1, 2, 1, 3, 1]
consumo = [12, 10, 15, 13, 11]


def distancia_percorrida(velocidade, tempo):
    distancia = round(velocidade * tempo, 2)
    return distancia


def consumo_veiculo(distancia, consumo):
    litros = round(distancia / consumo, 2)
    return litros

distancia_total = list(map(distancia_percorrida, velocidade_media, tempo_em_horas))
print(f'Distância total: {distancia_total}')
consumo_total = list(map(consumo_veiculo, distancia_total, consumo))
print(f'Consumo total: {consumo_total}')
