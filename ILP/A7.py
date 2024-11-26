# Entrada: quantidade de clientes
n = int(input())

# Entrada: números das fichas
fichas = list(map(int, input().split()))

# Ordenação manual usando o método de seleção
for i in range(n - 1):
    menor = i
    for j in range(i + 1, n):
        if fichas[j] < fichas[menor]:
            menor = j
    # Troca o menor elemento encontrado com o elemento atual
    fichas[i], fichas[menor] = fichas[menor], fichas[i]

# Determinando o índice do elemento no meio
indice_meio = n // 2

# Saída: número da ficha vencedora
print(fichas[indice_meio])
