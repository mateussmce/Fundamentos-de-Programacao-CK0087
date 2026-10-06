quantidade_pessoas = 189
quantidade_pessoas_por_grupo = 14

# Quantos grupos de 8 pessoas é possível formar a partir de 97 pessoas?
quantidade_grupos = quantidade_pessoas // quantidade_pessoas_por_grupo
quantidade_pessoas_sem_grupo = quantidade_pessoas % quantidade_pessoas_por_grupo

print(f"Quantidade de pessoas: {quantidade_pessoas}")
print(f"Quantidade de pessoas por grupo: {quantidade_pessoas_por_grupo}")
print(f"Quantidade de grupos: {quantidade_grupos}")
print(f"Quantidade de pessoas (sem grupo): {quantidade_pessoas_sem_grupo}")