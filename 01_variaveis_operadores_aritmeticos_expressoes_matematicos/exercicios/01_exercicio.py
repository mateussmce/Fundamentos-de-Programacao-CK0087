"""
Exercício 1: Nomes de variáveis

Item A
Dentre as opções de nome abaixo, escolha o único válido como identificador de variável e crie uma variável com tal nome (o valor da variável pode ser um número qualquer).

Opções:

1_nota
nota final
nota_final
nota-final
nota#final
"""

#1_nota = 5 => não é permitido (iniciar com um número)
# nota final = 9 => não é permitido (espaço)
# nota-final = 8 => não é permitido ('-' como separador)
# nota#final = 4 => não é permitido ('#' como separador)

nota_final = 8.5
print(f"Nota final: {nota_final}")