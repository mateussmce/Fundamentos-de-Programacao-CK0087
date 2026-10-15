"""
Exercício 9: prevendo o valor de variáveis encadeadas

Antes de executar, tente prever o valor de cada variável do código abaixo.
Depois execute a célula e confira se suas previsões estavam certas.
"""

a = 5
b = a * 2
c = b + a
d = c // 4
e = c % 4

# a = 5
print(f"a: {a}")

# b = 5 * 2 => 10, b = 10
print(f"b: {b} = {a} * {2} => {a * 2}")

# c = 10 + 5
print(f"c: {b} + {a} => {b + a}")

# d = 15 // 4 => 3
print(f"d: {c} // {4} = {c // 4}")

# e = 15 % 4
# 15 - 12 = r => r = 3
print(f"e: {15} % {4} => {15 % 4}")