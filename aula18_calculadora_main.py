from aula18_classe_calculadora import Calculadora

x = int(input('Digite o 1º número: '))
y = int(input('Digite o 2º número: '))
print()

calculo = Calculadora(x, y)

print(f'{calculo.get_numero1()} + {calculo.get_numero2()} = {calculo.set_somar()}\n'
      f'{calculo.get_numero1()} - {calculo.get_numero2()} = {calculo.set_subtrair()}\n'
      f'{calculo.get_numero1()} x {calculo.get_numero2()} = {calculo.set_multiplicar()}\n'
      f'{calculo.get_numero1()} / {calculo.get_numero2()} = {calculo.set_dividir()}\n')
