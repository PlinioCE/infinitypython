def gerar_areas(lista):
    areas = []
    for lado in lista:
        area = round(lado ** 2, 2)
        areas.append(area)
    return areas


lados = [5, 7, 4, 8, 9.5, 7.5, 6.6]
print(f'Áreas = {gerar_areas(lados)}')
areas = [25, 49, 16, 64, 90.25, 56.25, 43.56]

"""
Sintaxe função map

map(<função>, <iteraveis>)
"""

lados = [5, 7, 4, 8, 9.5, 7.5, 6.6]
novas_areas = list(map(lambda lado: round(lado ** 2, 2), lados))
print(f'Áreas da lista: {novas_areas}')

nomes = ['joão', 'maria', 'francisco', 'mariana', 'julia']
nomes_corrigidos = list(map(lambda nome: nome.tittle(), nomes))
print(f'Nomes corrigidos: {nomes_corrigidos}')


def area_circulo(raio):
    area = 3.14 * raio ** 2
    return round(area, 2)


raios = [7.5, 5, 3.3, 2.8, 9, 10.5]
areas_circulos = list(map(area_circulo, raios))

print(f'Áreas círculos: {areas_circulos}')
