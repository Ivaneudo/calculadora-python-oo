class Divisao:
    def calcular(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Erro: Divisão por zero não é permitida.") #
        return a / b