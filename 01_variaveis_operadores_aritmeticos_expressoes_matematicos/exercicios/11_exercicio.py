"""
Exercício 11: Precedência e associatividade

Vimos que ** tem prioridade sobre *, /, //, %, que por sua vez têm prioridade sobre + e -.
Já a exponenciação é associativa à direita, ou seja, 2 ** 3 ** 2 é interpretado como 2 ** (3 ** 2), e não (2 ** 3) ** 2.
Os outros operadores (+, -, *, /, //, %) são associativos à esquerda, ou seja, 8 / 4 / 2 é (8 / 4) / 2, e não 8 / (4 / 2).
Além disso, note que +/- podem ser operadores unários: +3 (unário), -4 (unário), -(2+5) (- unário, + binário), -2+5 (- unário, + binário).
Quando unários, +/- têm precedência sobre *, /, //, %.

Antes de executar, calcule mentalmente o valor de cada expressão abaixo e anote em comentários. Depois execute e confira.
"""

# Previsões:
# 2 ** 3 ** 2 ->
# 8 / 4 / 2 ->
# 100 // 7 % 3 ->
# 2 + 3 * 4 ** 2 // 5 % 3 ->
# (2 + 3) * (4 - 1) ** 2 // 5 ->
# -3 ** 2 ->
# (-3) ** 2 ->
# 1 -- 2 ->

# 2 ** 3 ** 3 => 2 ** 9 => 512
print(f"{2} ** {3} ** {2} = {2 ** 3 ** 2}")

# 8 / 4 / 2 => 2 / 2 = 1
print(f"{8} / {4} / {2} = {8 / 4 / 2}")

# 100 // 7 % 3 => 14 % 3 = 14 = 3 * 4 + r => 14 = 12 + r => r = 14 - 12 = 2
print(f"{100} // {7} % {3} = {100 // 7 % 3}")

# 2 + 3 * 4 ** 2 // 5 % 3 => 2 + 3 * 16 // 5 % 3 => 2 + 48 // 5 % 3
# 2 + 9 % 3 => [2], 9 = 3 * 3 + r => r = 9 - 9 = 0, 2 + 0 = 2
print(f"{2} + {3} * {4} ** {2} // {5} % {3} = {2 + 3 * 4 ** 2 // 5 % 3}")

# (2 + 3) * (4 - 1) ** 2 // 5 => 9
# 5 * 3 ** 2 // 5 => 5 * 9 // 5 => 45 // 5 = 9
print(f"({2} + {3}) * ({4} - {1}) ** {2} // {5} = {(2 + 3) * (4 - 1) ** 2 // 5}")

# -3 ** 2 => -9
print(f"{-3} ** {2} = {-3 ** 2}")

# (-3) ** 2 ->
print(f"({-3}) ** {2} = {(-3) ** 2}")

# 1 -- 2 -> 1 - (-2) = 3
print(f"{1} -- {2} = {1 -- 2}")