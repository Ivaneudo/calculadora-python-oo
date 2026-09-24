# 🚀 Calculadora Python Orientada a Objetos (POO)

*Como apresentado na nossa demonstração, esta não é apenas mais uma calculadora de terminal. É um motor matemático seguro e inteligente desenhado para ser robusto e completo!*

## ✨ O Poder por Trás da Tela

Você acabou de ver como a calculadora constrói passo a passo equações complexas (como `v 16 + 2 ^ 3 - 15 % 200 + 10 mod 3`) e entrega o resultado exato, respeitando perfeitamente a hierarquia matemática. E o mais impressionante: **tudo isso sem usar a função "preguiçosa" e insegura `eval()` do Python!**

### 🛠️ Principais Diferenciais e Recursos

- **Precedência Matemática Avançada em Múltiplas Etapas:** Resolução estrita por ordem de operações:
  1. Operações unárias: Raiz quadrada (`v` ou `sqrt`)
  2. Potenciação (`^`)
  3. Multiplicação (`*`), Divisão (`/`), Porcentagem (`%`) e Resto da divisão (`mod`)
  4. Adição (`+`) e Subtração (`-`)
- **Conjunto de Operações Expandido:**
  - **Porcentagem (`%`):** Calcula porcentagens de valores diretamente (ex: `15 % 200` resulta em `30`).
  - **Raiz Quadrada (`v` ou `sqrt`):** Suporte prático utilizando a letra **`v`** (pensado para teclados sem o símbolo `√`) ou a palavra-chave `sqrt`.
  - **Potenciação (`^`):** Elevação de potências simples e intuitiva (ex: `2 ^ 3`).
  - **Resto da Divisão (`mod`):** Retorna o resto da divisão inteira (ex: `10 mod 3`).
- **Arquitetura Orientada a Objetos:** Aplicação dos conceitos de POO (Composição e Encapsulamento) seguindo o *Princípio da Responsabilidade Única*, mantendo a regra de negócios separada da interface.
- **Segurança e Sanitização:** Tratamento via Expressões Regulares (`regex`) que convertem entradas para minúsculas e previnem injeções de código inseguras.
- **Interface Interativa Dinâmica:** Permite construir a equação passo a passo no terminal, acompanhando a evolução da expressão em tempo real e aceitando entradas insensíveis a maiúsculas/minúsculas.
- **Formatação Inteligente (Smart Float) & Tratamento de Erros:** Exibição arredondada para duas casas decimais em fracionários, limpeza visual para inteiros (ex: `4.0` vira `4`) e prevenção de erros (como divisão por zero e raiz de números negativos).

## 🧪 Exemplos de Operações (Casos de Uso)

Para demonstrar a capacidade e a robustez do motor matemático, abaixo estão alguns exemplos de equações suportadas, cobrindo desde operações básicas até expressões complexas e tratamento de exceções.

### Operações Básicas e Específicas

| Categoria | Equação de Entrada | Resultado | Descrição |
| :--- | :--- | :--- | :--- |
| **Soma e Subtração** | `25 + 15 - 10` | **30** | Validação de operações sequenciais de baixa prioridade. |
| **Multiplicação e Divisão** | `10 * 6 / 2` | **30** | Validação de operações sequenciais de alta prioridade. |
| **Potenciação** | `2 ^ 3` | **8** | Cálculo de expoentes suportado de forma nativa. |
| **Porcentagem** | `15 % 200` | **30** | Extração direta de 15% sobre o valor de 200. |
| **Resto (Módulo)** | `10 mod 3` | **1** | Retorno do resto da divisão inteira entre 10 e 3. |
| **Raiz Quadrada** | `v 144` (ou `sqrt 144`) | **12** | Resolução de operações unárias de alta prioridade. |
| **Logaritmo** | `100 log 10` | **2** | Cálculo do logaritmo de 100 na base 10. |

### Expressões Complexas e Precedência

| Categoria | Equação de Entrada | Resultado | Descrição |
| :--- | :--- | :--- | :--- |
| **Precedência Matemática** | `5 + 3 * 2 ^ 2` | **17** | Garante a ordem correta: potência (`2^2=4`), multiplicação (`3*4=12`), soma (`5+12=17`). |
| **Início Negativo** | `- v 9 + 3` | **0** | O motor lida perfeitamente com expressões iniciadas por operadores e valores negativos. |
| **Combinação de Símbolos** | `v 16 * 10 % 500` | **200** | Resolve a raiz (4), multiplica (40), e calcula a porcentagem (40% de 500). |

### Resiliência e Tratamento de Erros

A calculadora foi projetada para não falhar abruptamente. Entradas inválidas são capturadas e retornam mensagens amigáveis ao usuário:

*   **Divisão por Zero:** `5 / 0` ➔ Exibe `Erro: Divisão por zero não é permitida.`
*   **Módulo por Zero:** `5 mod 0` ➔ Exibe `Erro: Módulo (resto) por zero não é permitido.`
*   **Raiz Negativa:** `v -4` ➔ Exibe `Erro: Raiz quadrada de número negativo.`

## 📁 Estrutura do Projeto

O projeto está dividido em módulos essenciais e organizados:

```text
/
├── Operacoes/          # Classes especialistas (Soma.py, Divisao.py, Log.py, etc.)
├── Calculadora.py      # O Motor Matemático: Classe Calculadora (Lógica, Regex e Precedência)
└── Main.py             # A Interface: Classe InterfaceCalculadora (I/O e Loop do Usuário)