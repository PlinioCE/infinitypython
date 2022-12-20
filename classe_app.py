from abc import ABC, abstractmethod
from time import sleep


class App:
    def __init__(self, nome, consumo_memoria, consumo_bateria):
        self.nome = nome
        self.consumo_memoria = consumo_memoria
        self.consumo_bateria = consumo_bateria


class Smartphone(ABC):
    def __init__(self, fabricante, memoria, armazenamento):
        self.fabricante = fabricante
        self.memoria = memoria
        self.armazenamento = armazenamento
        self.bateria = 100
        self.memoria_utilizada = 0
        self.status = False
        self.app_aberto = []

    def ligar(self):
        if not self.status:
            self.status = True
            print('\nIniciando, aguarde', end='')
            for contagem in range(0, 3):
                sleep(1)
                print('.', end='')
            print('\nCarregando arquivos do sistema', end='')
            for contagem in range(0, 3):
                sleep(1)
                print('.', end='')
            print('\nSmarthone ligado!')
        else:
            print('\nSmartphone desligado!')

    def desligar(self):
        if self.status:
            self.status = False
            print('\nDesligando, aguarde', end='')
            for contagem in range(0, 3):
                sleep(1)
                print('.', end='')
            print('\nFinalizando arquivos do sistema', end='')
            for contagem in range(0, 3):
                sleep(1)
                print('.', end='')
            print('\nSmarthone desligado!')
        else:
            print('\nSmartphone ligado!')

    @abstractmethod
    def abrir_app(self, nome, consumo_memoria, consumo_bateria):
        pass

    def fechar_app(self, nome):
        pass

    def listar_app(self):
        pass

    def exibir_dados(self):
        print(f'FABRICANTE: {self.fabricante}'
              f'\nTOTAL MEMÓRIA RAM: {self.memoria} GB'
              f'\nMEMÓRIA DISPONÍVEL: {self.memoria - self.memoria_utilizada} GB'
              f'\nARMAZENAMENTO: {self.armazenamento} GB'
              f'\nBATERIA: {self.bateria}%')


class Galaxy(Smartphone):

    def abrir_app(self, nome, consumo_memoria, consumo_bateria):
        self.memoria_utilizada = self.memoria - ()

    def fechar_app(self, nome):
        pass

    def listar_app(self):
        pass


class Iphone(Smartphone):

    def abrir_app(self, nome, consumo_memoria, consumo_bateria):
        self.memoria_utilizada = self.memoria - (self.memoria * 0.2)

    def fechar_app(self, nome):
        self.bateria -= 1

    def listar_app(self):
        self.bateria -= 1

