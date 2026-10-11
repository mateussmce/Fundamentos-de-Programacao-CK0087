"""
Exercício 6: atualizando o valor de uma variável

Uma urna de pesquisa começa com 150 fichas. A cada rodada, retiram-se 7 fichas.

São feitas 3 retiradas. Exiba o valor antes da primeira retirada e depois de cada uma das 3 retiradas.

Seu código deve funcionar para qualquer inteiro numero_de_fichas ( ≥21 ). Teste trocando 150 por 444.
"""

numero_fichas = 444
print(f"Número de fichas [1]: {numero_fichas}")

numero_fichas -= 7
print(f"Número de fichas [2]: {numero_fichas}")

numero_fichas -= 7
print(f"Número de fichas [3]: {numero_fichas}")

numero_fichas -= 7
print(f"Número de fichas [4]: {numero_fichas}")