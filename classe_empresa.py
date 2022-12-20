# classe_empresa.py

from time import sleep


class Funcionario:  # Superclasse
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def processamento(self):
        print('\nProcessando', end='')
        sleep(1)
        for contador in range(0, 3):
            print('.', end='')
            sleep(1)
        print()
        print('\nAcesso Liberado!')
        sleep(2)


class Estagiario(Funcionario):  # Subclasse
    def __init__(self, nome, cpf, salario, horas_trabalhadas):
        super().__init__(nome, cpf, salario)
        self.horas_trabalhadas = horas_trabalhadas

    def efetivar(self):
        if self.horas_trabalhadas >= 300:
            print(f'Parabéns, {self.nome}! Você está apto para ser efetivado.')
        else:
            if 300 - self.horas_trabalhadas > 1:
                print(f'{self.nome}, você não cumpriu a carga horária mínima.'
                      f'\nFaltam {300 - self.horas_trabalhadas}h a cumprir.')
            elif 300 - self.horas_trabalhadas == 1:
                print(f'{self.nome}, você não cumpriu a carga horária mínima.'
                      f'\nFalta {300 - self.horas_trabalhadas}h a cumprir.')

    def menu_estagiario(self):
        opcao = int(input(f'\nESCOLHA UMA OPÇÃO, {self.nome}:'
                          f'\n[1] - VERIFICAR STATUS'
                          f'\n[2] - SAIR\n'))
        if opcao == 1:
            Estagiario.efetivar(self)


class Gerente(Funcionario):  # Subclasse
    def __init__(self, nome, cpf, salario, senha, setor, qtd_equipe, comissao):
        super().__init__(nome, cpf, salario)
        self.senha = senha
        self.setor = setor
        self.qtd_equipe = qtd_equipe
        self.comissao = comissao

    def contratar(self):
        if self.qtd_equipe < 10:
            print(f'Necessária contratação de mais {10 - self.qtd_equipe} funcionários')
        elif self.qtd_equipe > 10:
            print(f'Necessária demissão. Há {self.qtd_equipe - 10} pessoas a mais na equipe.')
        else:
            print('Equipe completa!')

    def demitir(self):
        horas_trabalhadas = int(input('Quantas horas de trabalho tem o estagiário?: '))
        if horas_trabalhadas < 300:
            print('Será necessário demitir o estagiário.')
        else:
            print('O estagiário deve ser efetivado!')

    def menu_gerente(self):
        opcao = int(input(f'\nESCOLHA UMA OPÇÃO, {self.nome}:'
                          f'\n[1] - CONTRATAR'
                          f'\n[2] - DEMITIR'
                          f'\n[3] - SAIR\n '))
        if opcao == 1:
            Gerente.contratar(self)
        elif opcao == 2:
            Gerente.demitir(self)
