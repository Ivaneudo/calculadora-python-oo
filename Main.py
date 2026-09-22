from Calculadora import Calculadora

class InterfaceCalculadora:
    def __init__(self):
        self.calculadora = Calculadora()

    def iniciar(self):
        print("=== Calculadora Interativa ===")
        print("Operadores disponíveis:")
        print("  +   : Adição")
        print("  -   : Subtração")
        print("  *   : Multiplicação")
        print("  /   : Divisão")
        print("  ^   : Potenciação (Ex: 2 ^ 3)")
        print("  %   : Porcentagem (Ex: 15 % 200 calcula 15% de 200)")
        print("  mod : Resto da divisão (Ex: 10 mod 3)")
        print("  v   : Raiz quadrada (Ex: v 16 ou sqrt 16)")
        print("Para ver o resultado final, digite '=' quando o operador for solicitado.\n")

        equacao_formada = ""

        primeiro_input = input("Digite o primeiro número (ou 'v' para raiz): ").strip().lower()
        
        if primeiro_input in ['v', 'sqrt']:
            equacao_formada += "v "
            print(f"-> Equação se formando: [ {equacao_formada} ]\n")
            num = input("Digite o número para calcular a raiz: ").strip()
            equacao_formada += num
            print(f"-> Equação se formando: [ {equacao_formada} ]\n")
        else:
            equacao_formada += primeiro_input
            print(f"-> Equação se formando: [ {equacao_formada} ]\n")

        while True:
            operador = input("Digite o operador (+, -, *, /, ^, %, mod, v) ou '=' para finalizar: ").strip().lower()
            
            if operador == '=':
                break 
            
            operadores_validos = ['+', '-', '*', '/', '^', '%', 'mod', 'v', 'sqrt']
            if operador not in operadores_validos:
                print("Operador inválido. Tente novamente.")
                continue

            if operador in ['v', 'sqrt']:
                equacao_formada += f" {operador} "
                print(f"-> Equação se formando: [ {equacao_formada} ]\n")
                proximo_num = input("Digite o número para a raiz: ").strip()
                equacao_formada += proximo_num
            else:
                equacao_formada += f" {operador} "
                print(f"-> Equação se formando: [ {equacao_formada} ]\n")
                proximo_num = input("Digite o próximo número: ").strip()
                equacao_formada += proximo_num
                
            print(f"-> Equação se formando: [ {equacao_formada} ]\n")

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
                
            print("\n" + "="*30)
            print(f"Equação Final: {equacao}")
            print(f"Resultado:     {resultado_formatado}")
            print("="*30 + "\n")


if __name__ == "__main__":
    app = InterfaceCalculadora()
    app.iniciar()