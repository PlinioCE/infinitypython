class Carro:
    def __int__(self, marca, modelo, ano, velocidade, estado, cambio):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
        self.estado = estado
        self.cambio = cambio

    def ligar_carro(self):
        print('Veículo em funcionamento!')

    def desligar_carro(self):
        print('Veículo desligado!')

    def acelerar_carro(self):
        if 0 < self.velocidade < 20:
            marcha = 1
