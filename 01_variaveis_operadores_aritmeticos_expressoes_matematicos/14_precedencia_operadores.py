# 7 * 5 = 35
operacao1 = (7 * 5)

# 32 + 3.5 = 35.5
operacao2 = 2 ** 5 + (7 / 2)

# 2 + 9 = 11
operacao3 = -8 // -3 + 9

# 0,5 + 16 = 16.5
operacao4 = 2 % 3 / 4 + 8 * 2

# 35 + 35.5 - 11 * 16.5 => 35 + 35.5 - 181.5 = -111
expressao = operacao1 + operacao2 - operacao3 * operacao4

print(f"{operacao1} + {operacao2} - {operacao3} * {operacao4} = {expressao}")