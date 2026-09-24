class RestoDivisao:
    def calcular(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Erro: Módulo (resto) por zero não é permitido.")
        return a % b