"""
Exercício 16: Caixa eletrônico

Um caixa eletrônico precisa sacar o valor de R$ 287,00 usando o menor número possível de cédulas de R$ 100, R$ 50, R$ 20, R$ 10, R$ 5, R$ 2 e R$ 1.

Use // e % para calcular quantas cédulas de cada valor serão entregues.

Seu código deve funcionar para qualquer valor inteiro. Teste com 287, depois com 153 e 1000.
"""

def testar_cedula(titulo, cedula):
    valor_caixa = 287

    print("="*50)
    print(titulo)
    print(f"Quantidade de notas de ({cedula}): {valor_caixa // cedula}")
    print(f"Sobra: {valor_caixa % cedula}")

testar_cedula("Cédula: 100", 100)
testar_cedula("Cédula: 50", 50)
testar_cedula("Cédula: 10", 10)
testar_cedula("Cédula: 5", 5)
testar_cedula("Cédula: 2", 2)
testar_cedula("Cédula: 1", 1)

print("*"*100)

valor = 153
print(f"Valor: R$ {valor}\n")
print(f"Cédula 100: {valor // 100} + {valor % 100} = {(valor // 100) * 100 + valor % 100}")
print(f"Cédula 50: {valor // 50} + {valor % 50} = {(valor // 50) * 50 + valor % 50}")
print(f"Cédula 10: {valor // 10} + {valor % 10} = {(valor // 10) * 10 + valor % 10}")
print(f"Cédula 5: {valor // 5} + {valor % 5} = {(valor // 5) * 5 + valor % 5}")
print(f"Cédula 2: {valor // 2} + {valor % 2} = {(valor // 2) * 2 + valor % 2}")
print(f"Cédula 1: {valor // 1} + {valor % 1} = {(valor // 1) * 1 + valor % 1}")