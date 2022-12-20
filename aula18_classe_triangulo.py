# declaração da classe
class Triangulo:
    # declaração dos atributos
    # lado_a = None
    # lado_b = None
    # lado_c = None

    # declaração do método construtor
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    # declaração dos métodos
    def calcular_perimetro(self):
        if self.lado_a + self.lado_b > self.lado_c or \
                self.lado_a + self.lado_c > self.lado_b or \
                self.lado_b + self.lado_c > self.lado_a:
            perimetro = self.lado_a + self.lado_b + self.lado_c
        else:
            print('As medidas informadas não formam um triângulo!')
        return perimetro

    def get_maior_lado(self):
        if self.lado_a + self.lado_b > self.lado_c or \
                self.lado_a + self.lado_c > self.lado_b or \
                self.lado_b + self.lado_c > self.lado_a:
            maior_lado = self.lado_a
            print(f'O maior lado do triângulo é o Lado A, com {self.lado_a}u.m.')
            if self.lado_b > maior_lado:
                maior_lado = self.lado_b
                print(f'O maior lado do triângulo é o Lado B, com {self.lado_b}u.m.')
            elif self.lado_c > maior_lado:
                maior_lado = self.lado_c
                print(f'O maior lado do triângulo é o Lado C, com {self.lado_c}u.m.')
        else:
            print('As medidas informadas não formam um triângulo!')
        return maior_lado
