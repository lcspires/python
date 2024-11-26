n = int(input())  # Número de planetas
planetas = input().split()
codigo_planeta = {planetas[i]: i for i in range(n)}

x = int(input())  # Número de planetas para visitar
missao = [input().strip() for _ in range(x)]

# Matriz de distâncias
distancias = [list(map(int, input().split())) for _ in range(n)]

# Calculando a distância total
distancia_total = 0
posicao_atual = 0  # Yoda começa do planeta na posição 0
for planeta in missao:
    pos_planeta = codigo_planeta[planeta]
    distancia_total += distancias[posicao_atual][pos_planeta]
    posicao_atual = pos_planeta

print(distancia_total)
