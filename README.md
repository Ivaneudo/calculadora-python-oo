# 🚀 Calculadora Python Orientada a Objetos (POO)

*Como apresentado na nossa demonstração, esta não é apenas mais uma calculadora de terminal. É um motor matemático seguro e inteligente desenhado para ser robusto!*

## ✨ O Poder por Trás da Tela

Você acabou de ver como a calculadora constrói passo a passo equações complexas (como `2 + 5 - 1 * 4 / 6`) e entrega o resultado exato, respeitando perfeitamente a precedência matemática. E o mais impressionante: **tudo isso sem usar a função "preguiçosa" e insegura `eval()` do Python!**

### 🛠️ Principais Diferenciais e Recursos

- **Precedência Matemática Real:** Multiplicação e divisão são rigorosamente resolvidas antes de somas e subtrações, graças a um algoritmo próprio de *tokenização* e varredura de listas em múltiplas passagens.
- **Arquitetura Orientada a Objetos:** O código aplica conceitos de POO (como Composição e Encapsulamento) e segue o *Princípio da Responsabilidade Única*. A regra de negócios (o "cérebro" matemático) é completamente isolada da interface com o usuário.
- **Segurança em Primeiro Lugar:** Sem atalhos de linguagem que abrem brechas. As expressões são limpas e interpretadas de forma customizada utilizando Expressões Regulares (`regex`).
- **Interface Interativa Dinâmica:** O usuário não joga uma string confusa de uma vez. Ele constrói a equação passo a passo, acompanhando a formação da estrutura matemática em tempo real.
- **Formatação Inteligente (Smart Float):** Resultados matemáticos são exibidos de forma esteticamente limpa. Decimais longos são arredondados para duas casas (`1.66`), e floats que representam inteiros (como `4.0`) são limpos visualmente para `4`.
- **Tratamento de Exceções:** Sistema preparado para evitar quebras por divisão por zero, capturando e informando o erro de forma amigável ao usuário.

## 📁 Estrutura do Projeto

O projeto foi dividido em dois módulos essenciais para facilitar a escalabilidade e manutenção:

```text
/
├── calculadora.py      # O Motor Matemático: Contém a classe `Calculadora` (Lógica e Regex)
└── main.py             # A Interface: Contém a classe `InterfaceCalculadora` (I/O e Loop de repetição)
```

## 🚀 Como Executar e Testar

1. Certifique-se de ter o Python 3.x instalado no seu ambiente.
2. Abra o terminal e navegue até a pasta onde os arquivos foram salvos.
3. Para iniciar a demonstração interativa, chame o arquivo da interface:

```bash
python main.py
```

4. Siga as instruções no terminal: digite o primeiro número, escolha a operação e vá construindo a sua equação.
5. Quando estiver pronto para ver o motor em ação, digite `=` no lugar de um operador matemático.

---
*Projeto concebido com foco em Boas Práticas, Segurança e Lógica Estruturada.*