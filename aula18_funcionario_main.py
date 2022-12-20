from aula18_classe_funcionario import Funcionario

nome = str(input('Informe o nome do(a) funcionário(a): ')).title()
salario = float(input('Informe o salário do(a) funcionário(a): R$ '))
percentual_de_aumento = float(input('Informe a porcentagem de aumento: '))

empregado = Funcionario(nome, salario)

print(f'NOME:{empregado.nome}\n'
      f'SALÁRIO: R$ {empregado.salario:.2f}\n'
      f'NOVO SALÁRIO: R$ {empregado.aumentar_salario(percentual_de_aumento):.2f}')
