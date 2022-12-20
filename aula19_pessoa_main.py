from aula19_classe_pessoa import Pessoa

nome = str(input('Informe seu nome: ')).title()
nascimento = str(input('Informe a data de nascimento (dd/mm/aaaa): ')).split('/')
altura = int(input('Informe sua altura(cm): '))

pessoa = Pessoa(nome, int(nascimento[2]), altura)
print()
print(f'{pessoa.get_nome()} tem {pessoa.calcular_idade()} anos e {pessoa.get_altura():.2f}m.')
