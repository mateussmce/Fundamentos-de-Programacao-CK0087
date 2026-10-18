"""
Exercício 15: Prevendo tipos de expressões

Antes de executar, escreva em comentários qual tipo cada expressão produz. Depois confira com print(type(...)).

1. 10 / 2
2. 10 // 2
3. 10 % 2
4. 2 ** 0.5
5. 7 + 3.0
6. "7" + "3"
"""

# 10 / 2 = 5.0 (float)
print(f"1) {10} / {2} = {10 / 2} => {type(10 / 2)}")

# 10 // 2 = 5 (int)
print(f"2) {10} // {2} = {10 // 2} => {type(10 // 2)}")

# 10 = 2 * 5 + r => r = 10 - 10 => r = 0 (int)
print(f"3) {10} % {2} = {10 % 2} => {type(10 % 2)}")

# 2 ** 0.5 = 2 ** 1/2 => \sqrt{2} => (float)
print(f"{2} ** {0.5} = {2 ** 0.5} => {type(2 ** 0.5)}")

# 7 + 3.0 = 10.0 => (float)
print(f"{7} + {3.0} = {7 + 3.0} => {type(7 + 3.0)}")

# '7' + '3' = 73 => (str)
print(f"{'7'} + {'3'} = {'7' + '3'} => {type('7' + '3')}")

"""
Por que 10 / 2 e 10 // 2 têm tipos diferentes, mesmo ambos valendo 5?
"""

numero1 = 10
numero2 = 2

# Inclui a casa decimal (float)
print(f"\n{numero1} / {numero2} = {numero1 / numero2} => {type(numero1 / numero2)}")

# Ignora a casa decimal, apenas o número inteiro => (int)
print(f"{numero1} // {numero2} = {numero1 // numero2} => {type(numero1 // numero2)}")