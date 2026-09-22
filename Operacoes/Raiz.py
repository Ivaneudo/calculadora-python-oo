import math

class Raiz:
    def calcular(self, numero):
        if numero < 0:
            raise ValueError("Erro: Raiz quadrada de número negativo.")
        return math.sqrt(numero)