import math

def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Leitura da entrada
n = int(input())  # Número de mundos
mundos = {}
for _ in range(n):
    nome, x, y = input().split()
    mundos[nome] = (int(x), int(y))

m = int(input())  # Número de missões
missao = input().split()

# Calculando a distância total
distancia_total = 0
x_atual, y_atual = 0, 0  # Começando na capital (0, 0)
for mundo in missao:
    x_mundo, y_mundo = mundos[mundo]
    distancia_total += calcular_distancia(x_atual, y_atual, x_mundo, y_mundo)
    x_atual, y_atual = x_mundo, y_mundo

print(f"{distancia_total:.1f}")
