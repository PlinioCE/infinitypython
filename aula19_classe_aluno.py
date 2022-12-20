class Aluno:
    def __init__(self, nome, curso, tempo_acordado):
        self.nome = nome
        self.curso = curso
        self.tempo_acordado = tempo_acordado

    def estudar(self, tempo_estudando):
        self.tempo_acordado += tempo_estudando
        return self.tempo_acordado

    def dormir(self, tempo_dormindo):
        self.tempo_acordado -= tempo_dormindo
        return self.tempo_acordado


"""class Aluno:
    def __init__(self,n,c,tempoSemDormir):
        self.nome = n
        self.curso = c
        self.tempoSemDormir = tempoSemDormir
    def estudar(self,qtdeHorasDeEstudo):
        self.tempoSemDormir = self.tempoSemDormir   qtdeHorasDeEstudo
        return self.tempoSemDormir
    def dormir(self,qtdeHorasDeSono):
        self.tempoSemDormir = self.tempoSemDormir - qtdeHorasDeSono
        return self.tempoSemDormir

a1 = Aluno("Emanuel","ADS",12)
print("Qtde de horas sem dormir: ", a1.tempoSemDormir)
a1.estudar(4)
print("Qtde de horas sem dormir após ter estudado: ", a1.tempoSemDormir)
a1.dormir(6)
print("Qtde de horas sem dormir após ter dormido: ", a1.tempoSemDormir)"""