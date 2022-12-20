from classe_app import *

while True:
    marca = int(input('ESCOLHA UMA OPÇÃO:'
                      '\n[1] - iPhone'
                      '\n[2] - Galaxy'
                      '\n[3] - SAIR\n'))
    if marca == 3:
        break

    if marca == 1:
        fabricante = str(input('Informe a fabricante do iPhone: ')).title().strip()
        memoria_ram = int(input('Informe a memória RAM(GB) do iPhone: '))
        armazenamento = int(input('Informe o armazenamento(GB) do iPhone: '))
        iphone = Iphone(fabricante, memoria_ram, armazenamento)
        iphone.ligar()
        print()
        iphone.exibir_dados()
        iphone.desligar()
        print()
