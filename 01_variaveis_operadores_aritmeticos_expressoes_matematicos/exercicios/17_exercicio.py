"""
Exercício 17: Previsão de valor e tipo

Analise o código abaixo antes de executar e preveja o valor e o tipo de cada variável ao final. Depois execute e confira.
"""

a = 10
print(f"a = {a} => {type(a)}")

# b = 10 // 3 = 3 (int)
b = a // 3
print(f"b = {a} // {3} = {a // 3} => {type(a // 3)}")

# c = 10 % 3 => 10 = 3 * 3 + r => r = 10 - 9 => r = 1 => c = 1 (int)
c = a % 3
print(f"c = {a} % {3} = {a % 3} => {type(c)}")

# d = 10 / 2 => 5.0 (float)
d = a / 2
print(f"d = {a} / {2} = {a / 2} => {type(a / 2)}")

# e = 10 // 2 = 5 (int)
e = a // 2
print(f"e = {a} // {2} = {a // 2} => {type(a // 2)}")

# a = "dez" (str)
a = "dez"
print(f"\na = {a} => {type(a)}")

# b = 3 * 2 => b = 6
b = b * 2
print(f"b = {3} * {2} = {3 * 2} => {type(3 * 2)}")

# c = 1 ** 2 => c = 1 (str)
c = c ** 2
print(f"c = {1} ** {2} = {1 ** 2} => {type(1 ** 2)}")

# d = 5.0 + 1 => d = 6.0 (float)
d = d + 1
print(f"d = {5.0} + {1} = {5.0 + 1} => {type(5.0 + 1)}")

# e = 5 + 1.5 = 6.5 (float)
e = e + 1.5
print(f"e = {5} + {1.5} = {5 + 1.5} => {type(5 + 1.5)}")