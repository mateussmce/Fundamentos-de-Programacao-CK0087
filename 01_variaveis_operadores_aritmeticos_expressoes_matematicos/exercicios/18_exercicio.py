"""
Exercício 18: Arredondamento para cima

A divisão inteira a // b sempre arredonda para baixo. Em problemas de logística, frequentemente precisamos arredondar para cima.

Exemplo: Você tem itens = 17 caixas para transportar em caminhões que comportam capacidade = 5 caixas cada.

- A divisão inteira dá 17 // 5 = 3, mas 3 caminhões comportam só 15 caixas, deixando 2 de fora. O número correto de caminhões necessários é 4.
- Se fossem 15 itens, 15 // 5 = 3 (exatamente 3 caminhões).

Escreva uma única expressão matemática usando apenas //, +, - que calcule o teto da divisão (itens / capacidade) para quaisquer inteiros positivos itens e capacidade.
"""

itens = 35
capacidade = 5

caminhoes_necessarios = (itens + capacidade - 1) // capacidade

print(f"Quantidade de caminhões necessários: {caminhoes_necessarios}")
print(f"({itens} + {capacidade} - {1}) // {capacidade} = {caminhoes_necessarios}")