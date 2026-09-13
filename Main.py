# Importa a classe Calculadora do arquivo calculadora.py
from Calculadora import Calculadora

class InterfaceCalculadora:
    """Classe responsável por interagir com o usuário e exibir os dados."""
    def __init__(self):
        # A interface instancia a calculadora para poder usá-la
        self.calculadora = Calculadora()

    def iniciar(self):
        print("=== Calculadora Interativa ===")
        print("Digite os números e operadores passo a passo.")
        print("Para ver o resultado final, digite '=' quando o operador for solicitado.\n")

        equacao_formada = ""

        primeiro_num = input("Digite o primeiro número: ").strip()
        equacao_formada += primeiro_num
        print(f"-> Equação se formando: [ {equacao_formada} ]\n")

        while True:
            operador = input("Digite a operação (+, -, *, /) ou '=' para finalizar: ").strip()
            
            if operador == '=':
                break 
            
            if operador not in ['+', '-', '*', '/']:
                print("Operador inválido. Tente novamente.")
                continue

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


# --- Execução do Programa ---
if __name__ == "__main__":
    app = InterfaceCalculadora()
    app.iniciar()