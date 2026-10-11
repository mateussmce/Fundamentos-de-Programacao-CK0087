preco_produto = 345.90
desconto = 0.1
print(f"preco_produto: R$ {preco_produto}")
print(f"desconto: {(desconto * 100)}%")

print(f"\n{preco_produto} - ({preco_produto} * {desconto}) [{(preco_produto * desconto):.2f}] = {preco_produto}")
preco_produto = preco_produto - (preco_produto * desconto)
print(f"Preço atualizado: R$ {preco_produto}")

print("\nAtribuição composta: ")
preco_produto2 = 40.90

preco_produto2 += (preco_produto2 * 0.2)
print(f"Adição: {40.90} + ({40.90} * {0.2}) [{40.90 * 0.2}] = R$ {preco_produto2}")

preco_produto2 -= (preco_produto2 * 0.2)
print(f"Subtração: {49.08} - ({49.08} * {0.2}) = R$ {preco_produto2:.2f}")

preco_produto2 *= 4
print(f"Multiplicação: {39.264} * {4} = R$ {preco_produto2:.2f}")

preco_produto2 /= 5
print(f"Divisão: {157.06} / {5} = {preco_produto2:.2f}")

# 99 / 33.5 = 2.955223880597015 => 99 // 33.5 = 2

preco_produto2 //= 2
print(f"Divisão inteira: {31.41} // {2} = {31.41 // 2}")

preco_produto2 %= 2
print(f"Resto: {15.0} % {2} = {preco_produto2}")