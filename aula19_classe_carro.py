class Carro:
    # MÉTODO CONSTRUTOR
    def __init__(self):
        self.km_por_litro = 0
        self.capacidade_tanque = 50
        self.quantidade_combustivel = 0

    # MÉTODOS
    def andar(self, distancia):
        if self.quantidade_combustivel > 0:
            if self.quantidade_combustivel >= distancia / self.km_por_litro:
                combustivel_utilizado = distancia / self.km_por_litro
                self.quantidade_combustivel -= combustivel_utilizado
                return self.quantidade_combustivel
            else:
                print('Combustível Insuficiente! Necessário Abastecimento!')
        else:
            print('TANQUE VAZIO! FAVOR ABASTECER!')

    def abastecer(self, litros):
        if 0 < litros + self.quantidade_combustivel <= self.capacidade_tanque:
            self.quantidade_combustivel += litros
            print(f'Realizado abastecimento de {litros} litros! \
                        \nNÍVEL: {self.quantidade_combustivel:.2f} litros.')
        elif litros + self.quantidade_combustivel > self.capacidade_tanque:
            print('Capacidade do tanque excedida, será considerado tanque cheio!')
            self.quantidade_combustivel = 50
        else:
            print('Quantidade insuficiente!')
        return self.quantidade_combustivel

    def nivel_combustivel(self):
        if self.quantidade_combustivel <= 0.09:
            print(f'TANQUE VAZIO!\nNÍVEL: {self.quantidade_combustivel:.2f} litro.')
        elif 0.09 < self.quantidade_combustivel <= 10:
            print(f'RESERVA DE COMBUSTÍVEL!\nNÍVEL: {self.quantidade_combustivel:.2f} litros.')
        elif self.quantidade_combustivel > 10:
            print(f'NÍVEL: {self.quantidade_combustivel:.2f} litros.')
        print()

    def autonomia(self):
        print(f'AUTONOMIA: {self.quantidade_combustivel * self.km_por_litro:.0f} Km.')
        print()
