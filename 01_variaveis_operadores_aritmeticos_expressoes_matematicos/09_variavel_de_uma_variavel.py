nome_usuario_1 = "João"
nome_usuario_2 = "André"
nome_usuario_3 = "Felipe"

print(f"nome_usuario_1: {nome_usuario_1}")
print(f"nome_usuario_2: {nome_usuario_2}")
print(f"nome_usuario_3: {nome_usuario_3}")

nome_usuario_2 = nome_usuario_1
nome_usuario_1 = nome_usuario_3
nome_usuario_3 = "Miguel"

print(f"\nnome_usuario_1: {nome_usuario_1}")
print(f"nome_usuario_2: {nome_usuario_2}")
print(f"nome_usuario_3: {nome_usuario_3}")