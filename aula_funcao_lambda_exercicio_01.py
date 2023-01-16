area_triangulo = lambda base, altura: (base * altura) / 2
print(f'Área do triângulo = {area_triangulo(2, 6)} U.M')

area_trapezio = lambda base_maior, base_menor, altura: (base_maior + base_menor) * altura / 2
print(f'Área do trapézio = {area_trapezio(6, 4, 7)} U.M')

area_circulo = lambda raio: 3.14 * raio / 2
print(f'Área do círculo = {area_circulo(4)} U.M')

lam_maiuscula = lambda texto: texto.upper()
print(f'Nome: {lam_maiuscula("teste de texto")}')


def maiuscula(texto):
    texto = str(texto).upper()
    return texto


nome = str(input('Digite seu nome: '))
print(f'Seu nome é {maiuscula(nome)}.')

