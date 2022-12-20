from aula18_classe_livro import Livro

nome_livro = str(input('Informe o nome do livro: ')).title()
paginas = int(input('Informe a quantidade de páginas: '))
autor = str(input('Informe o nome do autor: ')).title()
preco = float(input('Informe o preço do livro: R$ '))

livro = Livro(nome_livro, paginas, autor, preco)

print(f'NOME DO LIVRO: {livro.nome}\n'
      f'QTD DE PÁGINAS: {livro.paginas}\n'
      f'AUTOR: {livro.autor}\n'
      f'PREÇO: R$ {livro.get_preco():.2f}\n')

novo_preco = float(input('Informe o novo preço do livro: R$ '))

print(f'NOME DO LIVRO: {livro.nome}\n'
      f'QTD DE PÁGINAS: {livro.paginas}\n'
      f'AUTOR: {livro.autor}\n'
      f'PREÇO: R$ {livro.set_preco(novo_preco):.2f}\n')
