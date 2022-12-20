# principal_empresa.py

from classe_empresa import *

while True:
    titulo= 'SISTEMA DFS TURMA 714 FOR'
    print('-' * 30)
    print(f'{titulo:^30}')
    print('-' * 30)
    print()
    funcao = int(input('INFORME SUA FUNÇÃO:'
                      '\n[1] - GERENTE'
                      '\n[2] - FUNCIONÁRIO'
                      '\n[3] - ESTAGIÁRIO'
                      '\n[4] - SAIR\n'))
    print('-' * 30)
    if funcao in range(1, 5):
        if funcao == 1:
            nome_gerente = str(input('Informe seu nome: ')).strip().title()
            cpf_gerente = int(input('Informe seu CPF (Somente números): '))
            senha_gerente = str(input('Informe a senha: '))
            salario_gerente = float(input('Informe seu salário: R$ '))
            setor_gerente = str(input('Informe o setor: ')).strip().title()
            equipe_gerente = int(input('Quantas pessoas na equipe: '))
            comissao_gerente = int(input('Informe a % da comissão: '))
            gerente1 = Gerente(nome_gerente, cpf_gerente, senha_gerente, salario_gerente, setor_gerente, equipe_gerente, comissao_gerente)
            Gerente.processamento(gerente1)
            Gerente.menu_gerente(gerente1)

        elif funcao == 2:
            nome_funcionario = str(input('Informe seu nome: ')).strip().title()
            cpf_funcionario = int(input('Informe seu CPF (Somente números): '))
            salario_funcionario = float(input('Informe seu salário: R$ '))
            funcionario1 = Funcionario(nome_funcionario, cpf_funcionario, salario_funcionario)
            Funcionario.processamento(funcionario1)

        elif funcao == 3:
            nome_estagiario = str(input('Informe seu nome: ')).strip().title()
            cpf_estagiario = int(input('Informe seu CPF (Somente números): '))
            salario_estagiario = float(input('Informe seu salário: R$ '))
            horas_estagiario = float(input('Informe a quantidade de horas trabalhadas: '))
            estagiario1 = Estagiario(nome_estagiario, cpf_estagiario, salario_estagiario, horas_estagiario)
            Estagiario.processamento(estagiario1)
            Estagiario.menu_estagiario(estagiario1)
        else:
            print('\nFINALIZANDO SISTEMA...')
            break
    else:
        print('FUNÇÃO NÃO ENCONTRADA!')
    saida = str(input('\nDeseja continuar? [S/N]: ')).upper().strip()
    if saida[0] in 'SY':
        continue
    else:
        print('\nFINALIZANDO SISTEMA...')
        break
