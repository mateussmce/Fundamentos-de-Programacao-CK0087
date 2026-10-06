numero1 = 16
numero2 = 7

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
divisao_inteira = numero1 // numero2
resto = numero1 % numero2
potenciacao = numero1 ** numero2

print(f"{numero1} + {numero2} = {soma}")
print(f"{numero1} - {numero2} = {subtracao}")
print(f"{numero1} * {numero2} = {multiplicacao}")
print(f"{numero1} / {numero2} = {divisao:.2f}")
print(f"{numero1} // {numero2} = {divisao_inteira}")
print(f"{numero1} % {numero2} = {resto}")
print(f"{numero1} ^ {numero2} = {potenciacao}")

# -16 + (-7) = -23
print(f"\n{-numero1} + {-numero2} = {-numero1 + -numero2}")

# -16 + 7 = -9
print(f"{-numero1} + {numero2} = {-numero1 + numero2}")

# 16 + (-7) = 9
print(f"{numero1} + {-numero2} = {numero1 + -numero2}")