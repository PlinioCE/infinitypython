def area_quadrado(lado: float) -> float:
    area = lado ** 2
    return area

print(f'Área do quadrado = {area_quadrado(5)}')


"""
Sintaxe função lambda

<variável> = lambda <parametros>: <código>
"""


area_quad = lambda lado: lado**2

print(f'Área do quadrado utilizando lambda = {area_quad(6)}')
