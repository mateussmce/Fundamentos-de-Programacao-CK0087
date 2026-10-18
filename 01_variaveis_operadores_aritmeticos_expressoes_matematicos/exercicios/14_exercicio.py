"""
Exercício 14: o que está acontecendo?

Explique o que o código abaixo faz. Teste com vários inteiros a e b. Depois, justifique por que funciona.
"""

a = 1
b = 200

# a = 1 e b = 200
print("Antes: a =", a, "| b =", b)

# a = 1 + 200 => a = 201
a = a + b
print(f"\na = {1} + {200} = {1 + 201}")

# b = 201 - 200 => b = 1
b = a - b
print(f"b = {201} - {200} = {201 - 200}")

# a = 201 - 1 = 200
a = a - b
print(f"a = {201} - {1} = {201 - 1}\n")

# a = 200 e b = 1
print("Depois: a =", a, "| b =", b)