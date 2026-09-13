import re

class Calculadora:
    """Classe responsável apenas por realizar os cálculos matemáticos."""
    def __init__(self):
        self.operacoes_alta_prioridade = ['*', '/']
        self.operacoes_baixa_prioridade = ['+', '-']

    def _tokenizar(self, expressao: str) -> list:
        expressao = expressao.replace(" ", "")
        tokens_string = re.findall(r'\d+\.?\d*|[+\-*/]', expressao)
        
        tokens = []
        for token in tokens_string:
            if token in "+-*/":
                tokens.append(token)
            else:
                tokens.append(float(token))
        return tokens

    def _resolver_operacoes(self, tokens: list, operadores_alvo: list) -> list:
        i = 0
        while i < len(tokens):
            if tokens[i] in operadores_alvo:
                operador = tokens[i]
                numero_esq = tokens[i - 1]
                numero_dir = tokens[i + 1]
                
                if operador == '*':
                    resultado = numero_esq * numero_dir
                elif operador == '/':
                    if numero_dir == 0:
                        raise ZeroDivisionError("Erro: Divisão por zero não é permitida.")
                    resultado = numero_esq / numero_dir
                elif operador == '+':
                    resultado = numero_esq + numero_dir
                elif operador == '-':
                    resultado = numero_esq - numero_dir
                    
                tokens = tokens[:i - 1] + [resultado] + tokens[i + 2:]
                i -= 1
            else:
                i += 1
        return tokens

    def calcular(self, expressao: str) -> float:
        try:
            tokens = self._tokenizar(expressao)
            tokens = self._resolver_operacoes(tokens, self.operacoes_alta_prioridade)
            tokens = self._resolver_operacoes(tokens, self.operacoes_baixa_prioridade)
            return tokens[0]
        except Exception as e:
            print(f"\nErro matemático: {e}")
            return None