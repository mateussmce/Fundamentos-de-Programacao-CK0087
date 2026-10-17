"""
Exercício 13: Conversão de tempo

Um vídeo tem 98765 segundos de duração.
Converta esse valor para horas, minutos e segundos, usando // e %.

Exemplo: 3661 segundos = 1 hora, 1 minuto e 1 segundo.
Seu código deve funcionar para qualquer inteiro total_segundos. Teste trocando 98765 por 3661.
"""

tempo_segundos = 98765
# tempo_segundos = 3661

horas = tempo_segundos // 3600
minutos = (tempo_segundos % 3600) // 60
segundos = tempo_segundos % 60


print(f"\nTempo em segundos: {tempo_segundos}")
print(f"\nQuatidade de segundos: {segundos}")
print(f"Quantidade de horas: {horas}")
print(f"Quantidade de minutos: {minutos}")