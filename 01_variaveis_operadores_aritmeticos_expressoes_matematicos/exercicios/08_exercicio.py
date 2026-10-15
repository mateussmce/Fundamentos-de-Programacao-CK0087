"""
Exercício 8: trocando valores entre variáveis

Considere a = 10 e b = 20. Escreva um código que troque os valores, de modo que ao final a valha 20 e b valha 10.
Seu código deve funcionar até mesmo se alterarmos os valores iniciais 10 e 20.
Ou seja, se a é inicialmente 5 e b é inicialmente 15, então a valerá 15 e b valerá ao final da troca.

Há várias soluções possíveis. Tente uma solução que define outra variável!
"""

variavel_a = 10
variavel_b = 20
variavel_troca = variavel_a
print("Antes da alteração: ")
print(f"variavel_a: {variavel_a} / variavel_b: {variavel_b} / variavel_troca: {variavel_troca}")

variavel_a = variavel_b
variavel_b = variavel_troca
print("\nDepois da alteração: ")
print(f"variavel_a: {variavel_a} / variavel_b: {variavel_b} / variavel_troca: {variavel_troca}")