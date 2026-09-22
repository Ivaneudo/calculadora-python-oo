import re
from Operacoes.Soma import Soma
from Operacoes.Multiplicacao import Multiplicacao
from Operacoes.Divisao import Divisao
from Operacoes.Potencia import Potenciacao
from Operacoes.Log import Logaritmo
from Operacoes.Porcentagem import Porcentagem
from Operacoes.Raiz import Raiz

class Calculadora:
    def __init__(self):
        self.soma = Soma()
        self.mult = Multiplicacao()
        self.div = Divisao()
        self.pot = Potenciacao()
        self.log = Logaritmo()
        self.porc = Porcentagem()
        self.raiz = Raiz()

        self.operacoes_nivel_1 = ['^', 'log', '%']
        self.operacoes_nivel_2 = ['*', '/']
        self.operacoes_nivel_3 = ['+', '-']

    def _tokenizar(self, expressao: str) -> list:
        expressao = expressao.replace(" ", "")
        tokens_string = re.findall(r'[Vv]?\d+\.?\d*|log|[+\-*/^%]', expressao)
        
        tokens = []
        i = 0
        while i < len(tokens_string):
            token = tokens_string[i]
            
            # Identifica se o '-' é um sinal negativo (unário) e não uma subtração
            if token == '-' and (i == 0 or tokens_string[i-1] in ['+', '-', '*', '/', '^', '%', 'log']):
                if i + 1 < len(tokens_string):
                    next_token = tokens_string[i+1]
                    # Aplica o sinal negativo no número ou na raiz
                    if next_token.upper().startswith('V'):
                        numero = float(next_token[1:])
                        tokens.append(-self.raiz.calcular(numero))
                    else:
                        tokens.append(-float(next_token))
                    i += 2
                    continue
                else:
                    raise ValueError("Expressão terminada em sinal negativo.")

            # Trata operadores e números positivos/raízes padrão
            if token in ['+', '-', '*', '/', '^', '%', 'log']:
                tokens.append(token)
            elif token.upper().startswith('V'):
                numero = float(token[1:])
                tokens.append(self.raiz.calcular(numero))
            else:
                tokens.append(float(token))
            
            i += 1
            
        return tokens

    def _resolver_operacoes(self, tokens: list, operadores_alvo: list) -> list:
        i = 0
        while i < len(tokens):
            if tokens[i] in operadores_alvo:
                operador = tokens[i]
                numero_esq = tokens[i - 1]
                numero_dir = tokens[i + 1]
                
                if operador == '*':
                    resultado = self.mult.calcular(numero_esq, numero_dir)
                elif operador == '/':
                    resultado = self.div.calcular(numero_esq, numero_dir)
                elif operador == '+':
                    resultado = self.soma.adicionar(numero_esq, numero_dir)
                elif operador == '-':
                    resultado = self.soma.subtrair(numero_esq, numero_dir)
                elif operador == '^':
                    resultado = self.pot.calcular(numero_esq, numero_dir)
                elif operador == 'log':
                    resultado = self.log.calcular(numero_esq, numero_dir)
                elif operador == '%':
                    resultado = self.porc.calcular(numero_esq, numero_dir)
                    
                tokens = tokens[:i - 1] + [resultado] + tokens[i + 2:]
                i -= 1
            else:
                i += 1
        return tokens

    def calcular(self, expressao: str) -> float:
        try:
            tokens = self._tokenizar(expressao)
            tokens = self._resolver_operacoes(tokens, self.operacoes_nivel_1)
            tokens = self._resolver_operacoes(tokens, self.operacoes_nivel_2)
            tokens = self._resolver_operacoes(tokens, self.operacoes_nivel_3)
            return tokens[0]
        except Exception as e:
            print(f"\nErro matemático: {e}")
            return None