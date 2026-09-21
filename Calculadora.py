import math
import re

class Calculadora:
    """Classe responsável por realizar os cálculos matemáticos."""
    def __init__(self):
        self.operacoes_potencia = ['^']
        self.operacoes_alta_prioridade = ['*', '/', '%', 'mod']
        self.operacoes_baixa_prioridade = ['+', '-']

    def _tokenizar(self, expressao: str) -> list:
        # Converter para minúsculas facilita aceitar 'V' ou 'v'
        expressao = expressao.replace(" ", "").lower()
        tokens_string = re.findall(r'\d+\.?\d*|sqrt|mod|[+\-*/^%v]', expressao)
        
        tokens = []
        for token in tokens_string:
            if token in "+-*/^%v" or token in ["sqrt", "mod"]:
                tokens.append(token)
            else:
                tokens.append(float(token))
        return tokens

    def _resolver_unarios(self, tokens: list) -> list:
        """Resolve operações unárias como Raiz Quadrada (v ou sqrt)."""
        i = 0
        while i < len(tokens):
            if tokens[i] in ['v', 'sqrt']:
                if i + 1 < len(tokens) and isinstance(tokens[i + 1], (int, float)):
                    numero_dir = tokens[i + 1]
                    if numero_dir < 0:
                        raise ValueError("Não existe raiz quadrada de número negativo nos números reais.")
                    resultado = math.sqrt(numero_dir)
                    tokens = tokens[:i] + [resultado] + tokens[i + 2:]
                else:
                    raise ValueError("Sintaxe incorreta para raiz quadrada.")
            else:
                i += 1
        return tokens

    def _resolver_operacoes(self, tokens: list, operadores_alvo: list) -> list:
        i = 0
        while i < len(tokens):
            if tokens[i] in operadores_alvo:
                operador = tokens[i]
                numero_esq = tokens[i - 1]
                numero_dir = tokens[i + 1]
                
                if operador == '^':
                    resultado = numero_esq ** numero_dir
                elif operador == '*':
                    resultado = numero_esq * numero_dir
                elif operador == '/':
                    if numero_dir == 0:
                        raise ZeroDivisionError("Erro: Divisão por zero não é permitida.")
                    resultado = numero_esq / numero_dir
                elif operador == '%':
                    resultado = (numero_esq * numero_dir) / 100
                elif operador == 'mod':
                    resultado = numero_esq % numero_dir
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
            tokens = self._resolver_unarios(tokens)
            tokens = self._resolver_operacoes(tokens, self.operacoes_potencia)
            tokens = self._resolver_operacoes(tokens, self.operacoes_alta_prioridade)
            tokens = self._resolver_operacoes(tokens, self.operacoes_baixa_prioridade)
            
            if tokens:
                return tokens[0]
            return None
        except Exception as e:
            print(f"\nErro matemático: {e}")
            return None