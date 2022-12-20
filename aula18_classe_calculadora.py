class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        self.resultado = None

    def set_somar(self):
        self.resultado = self.numero1 + self.numero2
        return self.resultado

    def set_subtrair(self):
        self.resultado = self.numero1 - self.numero2
        return self.resultado

    def set_multiplicar(self):
        self.resultado = self.numero1 * self.numero2
        return self.resultado

    def set_dividir(self):
        self.resultado = self.numero1 / self.numero2
        return self.resultado

    def get_numero1(self):
        return self.numero1

    def get_numero2(self):
        return self.numero2
