class Divisao:
    # self, recebe um objeto self.div, equivalente ao this do Java
    def calcular(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Erro: Divisão por zero não é permitida.") 
        return a / b