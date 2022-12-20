conta_jogador = soma_idade = soma_peso = 0
time_jogador = []
nome_jogador = []
idade_jogador = []
peso_jogador = []
for equipes in range(0, 2):
    time = str(input('Nome do time: ')).upper()
    for jogador in range(1, 3):
        nome = str(input(f'Nome do {jogador}º atleta do {time}: ')).title()
        idade = int(input(f'Idade do {jogador}º atleta do {time}: '))
        peso = float(input(f'Peso do {jogador}º atleta do {time}: '))
        print()
        time_jogador.append(time)
        nome_jogador.append(nome)
        idade_jogador.append(idade)
        peso_jogador.append(peso)
        conta_jogador += 1
        soma_idade += idade
        soma_peso += peso
        media_idade = soma_idade / conta_jogador
        media_peso = soma_peso / conta_jogador
        lista_jogador = [time_jogador, nome_jogador, idade_jogador, peso_jogador]
    lista_time = [lista_jogador]
print(lista_time)
