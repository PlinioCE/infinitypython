class Livro:
    def __init__(self, nome, paginas, autor, preco):
        self.nome = nome
        self.paginas = paginas
        self.autor = autor
        self.preco = preco

    def get_preco(self):
        return self.preco

    def set_preco(self, novo_preco):
        self.preco = novo_preco
        return self.preco
