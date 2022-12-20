from aula19_classe_aluno import Aluno

nome_aluno = str(input('Nome do(a) aluno(a): ')).title()
curso_aluno = str(input('Curso do(a) aluno(a): ')).title()
horas_acordado = float(input('Há quantas horas o(a) aluno(a) está acordado? '))

aluno = Aluno(nome_aluno, curso_aluno, horas_acordado)
print()
estudara = str(input('O(A) aluno(a) pretende estudar? [S/N]: ')).upper()
print()
if estudara[0] == 'S':
    tempo_estudo = float(input('Quantas horas o(a) aluno(a) pretende estudar? '))
    aluno.estudar(tempo_estudo)
    print(f'Quantidade de hora')
else:
    tempo_sono = float(input('Quantas horas o(a) aluno(a) pretende dormir? '))
    aluno.dormir(tempo_sono)
print()
