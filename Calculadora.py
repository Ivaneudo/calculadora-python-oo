import math
import re
from Operacoes.Soma import Soma
from Operacoes.Multiplicacao import Multiplicacao
from Operacoes.Divisao import Divisao
from Operacoes.Potencia import Potenciacao
from Operacoes.Log import Logaritmo
from Operacoes.Porcentagem import Porcentagem
from Operacoes.Raiz import Raiz
from Operacoes.RestoDivisao import RestoDivisao

class Calculadora:
    """Classe responsável por realizar os cálculos matemáticos."""
    def __init__(self):
        self.operacoes_potencia = ['^']
        self.operacoes_alta_prioridade = ['*', '/', '%', 'mod', 'log'] 
        self.operacoes_baixa_prioridade = ['+', '-']
        
        # Instanciação das classes de operações
        self.soma = Soma()
        self.mult = Multiplicacao()
        self.div = Divisao()
        self.pot = Potenciacao()
        self.log = Logaritmo()
        self.porc = Porcentagem()
        self.raiz = Raiz()
        self.resto = RestoDivisao()

    def _tokenizar(self, expressao: str) -> list:
        expressao = expressao.replace(" ", "").lower()
        tokens_string = re.findall(r'\d+\.?\d*|sqrt|mod|log|[+\-*/^%v]', expressao)
        
        tokens = []
        for token in tokens_string:
            if token in "+-*/^%v" or token in ["sqrt", "mod", "log"]:
                tokens.append(token)
            elif token.upper().startswith('V'):
                numero = float(token[1:])
                tokens.append(self.raiz.calcular(numero))
            else:
                tokens.append(float(token))
        
        # Trata expressões iniciadas com operador unário (+ ou -) para evitar loop infinito
        if tokens and tokens[0] in ['-', '+']:
            tokens.insert(0, 0.0)
            
        return tokens

    def _resolver_unarios(self, tokens: list) -> list:
        """Resolve operações unárias como Raiz Quadrada (v ou sqrt)."""
        i = 0
        while i < len(tokens):
            if tokens[i] in ['v', 'sqrt']:
                if i + 1 < len(tokens) and isinstance(tokens[i + 1], (int, float)):
                    numero_dir = tokens[i + 1]
                    resultado = self.raiz.calcular(numero_dir)
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
                
                # Delegação direta para as classes especializadas
                match operador:
                    case '+':
                        resultado = self.soma.adicionar(numero_esq, numero_dir)
                    case '-':
                        resultado = self.soma.subtrair(numero_esq, numero_dir)
                    case '*':
                        resultado = self.mult.calcular(numero_esq, numero_dir)
                    case '/':
                        resultado = self.div.calcular(numero_esq, numero_dir)
                    case '^':
                        resultado = self.pot.calcular(numero_esq, numero_dir)
                    case '%':
                        resultado = self.porc.calcular(numero_esq, numero_dir)
                    case 'log':
                        resultado = self.log.calcular(numero_esq, numero_dir)
                    case 'mod':
                        resultado = self.resto.calcular(numero_esq, numero_dir)
                    
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