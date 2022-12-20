from datetime import datetime


class Pessoa:
    def __init__(self, nome, ano_nascimento, altura):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
        self.altura = altura

    def set_nome(self, novo_nome):
        self.nome = novo_nome
        return self.nome

    def set_data_nascimento(self, novo_ano_nascimento):
        self.ano_nascimento = novo_ano_nascimento
        return self.ano_nascimento

    def set_altura(self, nova_altura):
        self.altura = nova_altura / 100
        return self.altura

    def get_nome(self):
        return self.nome

    def get_data_nascimento(self):
        return self.ano_nascimento

    def get_altura(self):
        self.altura = self.altura / 100
        return self.altura

    def calcular_idade(self):
        ano_atual = datetime.today().year
        idade = ano_atual - self.ano_nascimento
        return idade
