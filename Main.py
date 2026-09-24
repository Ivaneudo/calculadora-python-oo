from Calculadora import Calculadora

class InterfaceCalculadora:
    def __init__(self):
        self.calculadora = Calculadora()

    def mostrar_menu(self):
        """Exibe o cabeçalho e a tabela de operadores."""
        print("\n" + "="*50)
        print(f"{'CALCULADORA INTERATIVA':^50}")
        print("="*50)
        print("+-----------+------------------------------------+")
        print("| Operador  | Descrição / Exemplo                |")
        print("+-----------+------------------------------------+")
        print("|  +        | Adição                             |")
        print("|  -        | Subtração                          |")
        print("|  *        | Multiplicação                      |")
        print("|  /        | Divisão                            |")
        print("|  ^        | Potenciação (Ex: 2 ^ 3)            |")
        print("|  %        | Porcentagem (Ex: 15 % 200)         |")
        print("|  mod      | Resto da divisão (Ex: 10 mod 3)    |")
        print("|  v / sqrt | Raiz quadrada (Ex: v 16)           |")
        print("|  log      | Logaritmo (Ex: 100 log 10)         |") 
        print("+-----------+------------------------------------+")
        print("Digite '=' quando o operador for solicitado para ver o resultado.\n")

    def mostrar_equacao(self, equacao: str):
        """Exibe a equação sendo formada em um bloco destacado."""
        print("\n" + "="*16 + " OPERAÇÃO " + "="*16)
        print(f"{equacao:^42}")
        print("="*42 + "\n")

    def iniciar(self):
        self.mostrar_menu()
        equacao_formada = ""

        primeiro_input = input("Digite o primeiro número (ou 'v' para raiz): ").strip().lower()
        
        if primeiro_input in ['v', 'sqrt']:
            equacao_formada += "v "
            self.mostrar_equacao(equacao_formada)
            num = input("Digite o número para calcular a raiz: ").strip()
            equacao_formada += num
            self.mostrar_equacao(equacao_formada)
        else:
            equacao_formada += primeiro_input
            self.mostrar_equacao(equacao_formada)

        while True:
            # Atualize o texto do input para incluir 'log'
            operador = input("Digite o operador (+, -, *, /, ^, %, mod, v, log) ou '=' para finalizar: ").strip().lower()
            
            if operador == '=':
                break 
            
            # 'log' adicionado à lista de verificação
            operadores_validos = ['+', '-', '*', '/', '^', '%', 'mod', 'v', 'sqrt', 'log']
            if operador not in operadores_validos:
                print("Operador inválido. Tente novamente.")
                continue

            if operador in ['v', 'sqrt']:
                equacao_formada += f" {operador} "
                self.mostrar_equacao(equacao_formada)
                proximo_num = input("Digite o número para a raiz: ").strip()
                equacao_formada += proximo_num
            else:
                equacao_formada += f" {operador} "
                self.mostrar_equacao(equacao_formada)
                proximo_num = input("Digite o próximo número: ").strip()
                equacao_formada += proximo_num
                
            self.mostrar_equacao(equacao_formada)

        self.exibir_resultado(equacao_formada)

    def exibir_resultado(self, equacao: str):
        resultado = self.calculadora.calcular(equacao)

        if resultado is not None:
            if isinstance(resultado, float):
                if resultado.is_integer():
                    resultado_formatado = f"{int(resultado)}"
                else:
                    resultado_formatado = f"{resultado:.2f}"
            else:
                resultado_formatado = str(resultado)
                
            print("\n" + "="*42)
            print(f"{'RESULTADO FINAL':^42}")
            print("="*42)
            print(f" Equação:   {equacao}")
            print(f" Resultado: {resultado_formatado}")
            print("="*42 + "\n")


if __name__ == "__main__":
    app = InterfaceCalculadora()
    app.iniciar()