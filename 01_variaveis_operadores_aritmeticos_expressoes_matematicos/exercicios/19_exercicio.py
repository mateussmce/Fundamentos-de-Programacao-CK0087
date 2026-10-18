"""
Exercício 19: Máximo de dois números

O Python tem uma função builtin max que calcula o máximo de dois números.

Apenas como exercício, em vez de usá-la, tente encontrar o maior valor entre a e b seguindo a estratégia abaixo:

O valor absoluto de um número  x  pode ser obtido através da raiz quadrada do seu quadrado:  |x|=x2−−√=(x2)0.5 . Aplique a fórmula:  max(a,b)=a+b+|a−b|2 .
"""

a = 101
b = 87

valor_absoluto_a = (a ** 2) ** 0.5
valor_absoluto_b = (b ** 2) ** 0.5

maior_valor = (valor_absoluto_a + valor_absoluto_b + abs(valor_absoluto_a - valor_absoluto_b)) / 2

print(f"({valor_absoluto_a} + {valor_absoluto_b} + |{valor_absoluto_a} - {valor_absoluto_b}|) / {2} = {maior_valor}")
print(f"Maior valor: {maior_valor}")