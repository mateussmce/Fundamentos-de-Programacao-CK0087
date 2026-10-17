"""
Exercício 12: Extraindo e remontando dígitos

Dado o número 847, use os operadores // e % para:

1. Extrair o dígito das centenas (8), o das dezenas (4) e o das unidades (7).
2. Calcular a soma dos dígitos (8 + 4 + 7 = 19).
3. Construir o número invertido (748).

Seu código deve funcionar para qualquer número de 3 dígitos. Teste trocando 847 por 123 e depois por 905.
"""

numero = 847
# numero = 123
# numero = 905

centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10
soma_digitos = centena + dezena + unidade

print(f"Número: {numero} <=> {centena}{dezena}{unidade}")
print(f"Soma dos dígitos: {centena} + {dezena} + {unidade} = {soma_digitos}")