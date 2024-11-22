n = int(input())
kills = list(map(int, input().split()))

# Evitando kills.sort(), por enquanto.
for i in range(n):
    for j in range(0, n - i - 1):
        if kills[j] > kills[j + 1]:
            # Troca os elementos se estiverem na ordem errada
            kills[j], kills[j + 1] = kills[j + 1], kills[j]

# map(str, kills) converte cada elemento de kills (que é uma lista de inteiros) em uma string
# join() as une com espaços entre eles

print(" ".join(map(str, kills)))
