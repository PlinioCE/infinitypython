from aula19_classe_carro import Carro
from time import sleep

carro = Carro()
print('*********** MERCEDES-BENZ ************')
print('***** BEM-VINDO(A), CONDUTOR(A)! *****')
print('*********** SISTEMA LIGADO ***********')
print('**************************************')
print()
while True:
    print('*********** MERCEDES-BENZ ************')
    print('**************** MENU ****************')
    menu = int(input('Escolha uma opção:\n'
                     '[1] - DIRIGIR\n'
                     '[2] - MEDIDOR DE COMBUSTÍVEL\n'
                     '[3] - ABASTECER\n'
                     '[4] - AUTONOMIA\n'
                     '[5] - DESLIGAR VEÍCULO\n'
                     '**************************************\n'))
    print()
    match menu:
        case 1:
            modo_conducao = int(input('Defina um modo de condução:\n'
                                      '[1] - ECO\n'
                                      '[2] - STANDARD\n'
                                      '[3] - SPORT\n'))
            match modo_conducao:
                case 1:
                    carro.km_por_litro = 19
                case 2:
                    carro.km_por_litro = 12
                case 3:
                    carro.km_por_litro = 5
            percurso = float(input('Quantos quilômetros tem o percurso? '))
            carro.andar(percurso)
            print()
            sleep(1)
        case 2:
            carro.nivel_combustivel()
        case 3:
            quantidade = int(input('Quantos litros deseja abastecer? '))
            print()
            carro.abastecer(quantidade)
            print()
            sleep(1)
        case 4:
            carro.autonomia()
            sleep(1)
            continue
        case 5:
            print('*********** MERCEDES-BENZ ************')
            print('***** OBRIGADO E VOLTE SEMPRE!!! *****')
            print('********* DESLIGANDO SISTEMA *********')
            print('**************************************')
            sleep(2)
            break
