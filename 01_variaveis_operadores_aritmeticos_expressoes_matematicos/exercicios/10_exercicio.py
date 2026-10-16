def titulo(titulo):
    print(f"\n{titulo}")
    print("="*50)

"""
Em cada item, substitua 'Substitua aqui' por uma expressão matemática.
Não introduza variáveis nesta célula de código.
Não responda mentalmente, use os operadores aritméticos!

Item A: Uma pesquisa de campo tem 100 questionários para serem separados em pilhas de 11.
Quantas pilhas completas serão formadas? Quantos questionários sobram?
"""

quantidade_questionarios = 100
quantidade_pilhas = 11

pilhas_completas = quantidade_questionarios // quantidade_pilhas
questionarios_sobrando = quantidade_questionarios % quantidade_pilhas

titulo("Item A")
print(f"quantidade_questionarios: {quantidade_questionarios}")
print(f"quantidade_pilhas: {quantidade_pilhas}")

print(f"\npilhas_completas: {pilhas_completas}")
print(f"questionarios_sobrando: {questionarios_sobrando}")

"""
Item B: Uma prova tem 60 questões e uma pessoa precisa acertar 70% delas para ser aprovada.

Quantas questões ela precisa acertar?
"""

quantidade_questoes_prova = 60
quantidade_minima_aprovacao = 0.7
quantidade_questoes_minima_aprovacao = int(quantidade_questoes_prova * quantidade_minima_aprovacao)
quantidade_questoes_minima_erro = int(quantidade_questoes_prova - quantidade_questoes_minima_aprovacao)

titulo("Item B")
print(f"Quantidade de questões da prova: {quantidade_questoes_prova}")
print(f"Quantidade mínima p/ aprovação: {quantidade_minima_aprovacao * 100}%")
print(f"Quantidade mínima de questões p/ aprovação: {quantidade_questoes_minima_aprovacao}")
print(f"Quantidade mínima de erros: {quantidade_questoes_minima_erro}")

"""
Item C: A nota final de uma disciplina é calculada pela média aritmética de 3 notas.

Calcule a nota final de uma pessoa que tirou notas 7.5, 9 e 6, respectivamente.
"""

primeira_nota, segunda_nota, terceira_nota = 7.5, 9, 6
media_aritmetica = (primeira_nota + segunda_nota + terceira_nota) / 3

titulo("Item C")
print(f"Nota1: {primeira_nota} | Nota2: {segunda_nota} | Nota3: {terceira_nota}")
print(f"Média aritmética: {media_aritmetica}")
print(f"Soma de notas: ({primeira_nota + segunda_nota + terceira_nota}) / {3} = {media_aritmetica}")

"""
Item D: Uma população de 100 indivíduos dobra de tamanho a cada ano.

Qual será o tamanho da população após 3 anos? E após 10 anos?
"""

quantidade_individuos = 100

titulo("Item D")
print(f"Quantidade de indivíduos: {quantidade_individuos}")

# Forma complexa
quantidade_individuos *= 2 # 100 * 2 = 200 (1)
quantidade_individuos *= 2 # 200 * 2 = 400 (2)
quantidade_individuos *= 2 # 400 * 2 = 800 (3)
print(f"Quantidade de índividuos após 3 anos: {quantidade_individuos}")

quantidade_individuos *= 2 # 800 * 2 = 1600 (4)
quantidade_individuos *= 2 # 1600 * 2 = 3200 (5)
quantidade_individuos *= 2 # 3200 * 2 = 6400 (6)
quantidade_individuos *= 2 # 6400 * 2 = 12800 (7)
quantidade_individuos *= 2 # 12800 * 2 = 25600 (8)
quantidade_individuos *= 2 # 25600 * 2 = 51200 (9)
quantidade_individuos *= 2 # 51200 * 2 = 102400 (10)
print(f"Quantidade de índividuos após 10 anos: {quantidade_individuos}")

# Forma simples
quantidade_individuos_absoluta = 100
quantidade_individuos = 100
print(f"\nQuantidade de índividuos: {quantidade_individuos}")

quantidade_individuos = quantidade_individuos_absoluta * (2 ** 3)
print(f"Após 3 anos: {quantidade_individuos}")

quantidade_individuos = quantidade_individuos_absoluta * (2 ** 10)
print(f"Após 10 anos: {quantidade_individuos}")

"""
Item E: O número 10 é par e o número 7 é ímpar.

Calcule o resto da divisão de cada um por 2.
"""

numero1, numero2 = 10, 7
divisor = 2
resto_numero1 = numero1 % divisor
resto_numero2 = numero2 % divisor

titulo("Item E")
print(f"\n1. {numero1} % {divisor} = {resto_numero1}")
print(f"{numero1} % {divisor} == {0} => {numero1 % divisor == 0}")

print(f"\n2. {numero2} % {divisor} = {resto_numero2}")
print(f"{numero2} % {divisor} != {0} => {numero2 % divisor != 0}")

"""
Item F: O IMC (Índice de Massa Corporal) é calculado dividindo a massa em kg pela altura ao quadrado em metros.

Calcule o IMC de uma pessoa com 70 kg e 1m e 70cm de altura.
"""

# peso = float(input("\nDigite seu peso em kg - Exemplo: 70 => "))
# altura = float(input("Digite sua altura em cm - Exemplo: 1.75 => "))

peso = 70
altura = 1.70

imc = peso / altura ** 2

titulo("Item F")
print(f"Peso: {peso:.2f}kg | altura: {altura:.2f}cm | imc: {imc}")

if imc < 18.5:
    # 45kg e 1.70cm
    print(f"Classificação: abaixo do peso com imc: {imc}")
elif 18.5 <= imc <= 24.9:
    # 60kg e 1.70cm
    print(f"Classificação: peso normal com imc: {imc}")
elif 25.0 <= imc <= 29.9:
    # 80kg e 1.70cm
    print(f"Classsificação: sobrepeso com imc: {imc}")
elif 30.0 <= imc <= 34.9:
    # 90kg e 1.70cm
    print(f"Classificação: obesidade grau I com imc: {imc}")
elif 35.0 <= imc <= 39.9:
    # 110kg e 1.70
    print(f"Classificação: obesidade grau II com imc: {imc}")
elif imc >= 40:
    # 120kg e 1.70
    print(f"Classificação: obesidade grau III com imc: {imc}")

"""
Item G: Um produto custa R$ 80,00 e está com 25% de desconto.

Qual o valor do desconto? Qual o preço final?
"""

preco_produto = 80
desconto = 0.25

desconto_total = preco_produto * desconto
preco_produto -= desconto_total

titulo("Item G")
print(f"Preço do produto: R$ {preco_produto} / Quantidade de desconto: {desconto * 100}%")
print(f"Valor descontado: {desconto_total} / Preço final: {preco_produto}")

preco_produto = 80

print(f"\nTotal {100}% => {preco_produto}")
print(f"{25}% => {preco_produto * desconto}")
print(f"{75}% => {preco_produto - (preco_produto * desconto)}")

"""
# Item H: Um ônibus percorreu 90 km em 1,5 h.

# Qual a velocidade média em km/h? E em m/s?
"""

distancia_total = 90
tempo_total = 1.5
velocidade_media_km_h = distancia_total / tempo_total
velocidade_media_m_s = velocidade_media_km_h / 3.6

titulo("Item H")
print(f"{distancia_total}km / {tempo_total}h = {velocidade_media_km_h}km/h")
print(f"{distancia_total * (10 ** 3)}m / {tempo_total * 3600}s = {velocidade_media_m_s:.2f}m/s")

print(f"\n{velocidade_media_km_h} km/h <=> {velocidade_media_m_s:.2f} m/s")

"""
# Item I: Quantos segundos tem 1 ano? Considere 1 ano = 365 dias.
"""

segundos, minutos, horas, dias = 60, 60, 24, 365

titulo("Item I")
print(f"1 minuto tem {segundos} segundos")

segundos *= minutos
print(f"60 minutos tem {segundos} segundos")

segundos *= horas
print(f"24 horas tem {segundos} segundos")

segundos *= dias
print(f"365 dias tem {segundos} segundos")