contador = 0
torc_fec = torc_csc = torc_fac = torc_cec = torc_outro = 0
morador_fortaleza = morador_caucaia = morador_outro = 0
soma_salario_fec = caucaia_fac = fortaleza_csc = 0

while contador != 10:
    time = int(input('Qual seu time do coração?\n'
                     '[1] - FEC\n'
                     '[2] - CEARÁ\n'
                     '[3] - Ferroviário\n'
                     '[4] - Caucaia\n'
                     '[5] - Outros\n'))
    print()
    match time:
        case 1:
            torc_fec += 1
        case 2:
            torc_csc += 1
        case 3:
            torc_fac += 1
        case 4:
            torc_cec += 1
        case 5:
            torc_outro += 1

    cidade = int(input('Onde você mora?\n'
                       '[1] - Fortaleza\n'
                       '[2] - Caucaia\n'
                       '[3] - Outros\n'))
    print()
    match cidade:
        case 1:
            morador_fortaleza += 1
        case 2:
            morador_caucaia += 1
        case 3:
            morador_outro += 1

    salario = float(input('Qual seu salário? R$ '))
    print()
    if time == 1:
        soma_salario_fec += salario
        media_fec = soma_salario_fec / torc_fec

    if time == 3 and cidade == 2:
        caucaia_fac += 1

    if time == 2 and cidade == 1:
        fortaleza_csc += 1

    contador += 1

print('********** RESULTADO **********')
print('*******************************')
print(f'********* TORCEDORES *********\n'
      f'FEC: {torc_fec} torcedores\n'
      f'CSC: {torc_csc} torcedores\n'
      f'FAC: {torc_fac} torcedores\n'
      f'CEC: {torc_cec} torcedores\n'
      f'Outros: {torc_outro} torcedores')
print('*******************************')
print()
print('******** MÉDIA SALARIAL *******')
print('*******************************')
print(f'FEC: R$ {media_fec:.2f}')
print('*******************************')
print()
print('***** MORADORES de CAUCAIA ****')
print('*******************************')
print(f'Time: Ferroviário\n'
      f'{caucaia_fac} pessoas')
print('*******************************')
print()
print('**** MORADORES de FORTALEZA ***')
print('*******************************')
print(f'Time: CEARÁ\n'
      f'{fortaleza_csc} pessoas')
print('*******************************')
print()
