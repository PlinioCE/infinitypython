# CHAMADA ALUNOS

chamada_alunos = {}
contador = 0
while True:
    contador += 1
    nome_aluno = str(input('Digite o nome do(a) aluno(a): '))
    chamada_alunos[str(contador)] = nome_aluno
    saida = str(input('Deseja adicionar outro(a) aluno(a)? [S/N] ')).upper().strip()
    if saida == 'N':
        break
print()
for numero, nome in chamada_alunos.items():
    print(f'{nome}, seu número de chamada é: {numero}')
