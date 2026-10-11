"""
Exercício 4: x = y versus x = 'y'

Antes de executar, tente prever: o que o código abaixo vai mostrar? Qual é a diferença entre x = y e x = 'y'?

Execute a célula abaixo e confira se sua previsão estava certa.
"""

x = 90
y = 100
print(f"x: {x} [{type(x)}], y: {y} [{type(y)}]")

x = 'y'
print(f"{x} [{type(x)}]")

x = y
print(f"{x} [{type(x)}]")