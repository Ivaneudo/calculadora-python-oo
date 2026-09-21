# 🚀 Calculadora Python Orientada a Objetos (POO)

*Como apresentado na nossa demonstração, esta não é apenas mais uma calculadora de terminal. É um motor matemático seguro e inteligente desenhado para ser robusto e completo!*

## ✨ O Poder por Trás da Tela

Você acabou de ver como a calculadora constrói passo a passo equações complexas (como `v 16 + 2 ^ 3 - 15 % 200 + 10 mod 3`) e entrega o resultado exato, respeitando perfeitamente a hierarquia matemática[cite: 1, 3]. E o mais impressionante: **tudo isso sem usar a função "preguiçosa" e insegura `eval()` do Python!**

### 🛠️ Principais Diferenciais e Recursos

- **Precedência Matemática Avançada em Múltiplas Etapas:** Resolução estrita por ordem de operações[cite: 1, 3]:
  1. Operações unárias: Raiz quadrada (`v` ou `sqrt`)[cite: 1]
  2. Potenciação (`^`)[cite: 1]
  3. Multiplicação (`*`), Divisão (`/`), Porcentagem (`%`) e Resto da divisão (`mod`)[cite: 1]
  4. Adição (`+`) e Subtração (`-`)[cite: 1]
- **Conjunto de Operações Expandido:**
  - **Porcentagem (`%`):** Calcula porcentagens de valores diretamente (ex: `15 % 200` resulta em `30`)[cite: 1].
  - **Raiz Quadrada (`v` ou `sqrt`):** Suporte prático utilizando a letra **`v`** (pensado para teclados sem o símbolo `√`) ou a palavra-chave `sqrt`[cite: 1].
  - **Potenciação (`^`):** Elevação de potências simples e intuitiva (ex: `2 ^ 3`)[cite: 1].
  - **Resto da Divisão (`mod`):** Retorna o resto da divisão inteira (ex: `10 mod 3`)[cite: 1].
- **Arquitetura Orientada a Objetos:** Aplicação dos conceitos de POO (Composição e Encapsulamento) seguindo o *Princípio da Responsabilidade Única*, mantendo a regra de negócios separada da interface[cite: 1, 2, 3].
- **Segurança e Sanitização:** Tratamento via Expressões Regulares (`regex`) que convertem entradas para minúsculas e previnem injeções de código inseguras[cite: 1, 3].
- **Interface Interativa Dinâmica:** Permite construir a equação passo a passo no terminal, acompanhando a evolução da expressão em tempo real e aceitando entradas insensíveis a maiúsculas/minúsculas.
- **Formatação Inteligente (Smart Float) & Tratamento de Erros:** Exibição arredondada para duas casas decimais em fracionários, limpeza visual para inteiros (ex: `4.0` vira `4`) e prevenção de erros (como divisão por zero e raiz de números negativos)[cite: 1, 2, 3].

## 📁 Estrutura do Projeto[cite: 3]

O projeto está dividido em dois módulos essenciais[cite: 3]:

```text
/
├── Calculadora.py      # O Motor Matemático: Classe Calculadora (Lógica, Regex e Precedência)
└── Main.py             # A Interface: Classe InterfaceCalculadora (I/O e Loop do Usuário)