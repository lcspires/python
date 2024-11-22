n = int(input())  # Lê o número de elementos
steps = list(map(int, input().split()))  # Lê os N valores em uma única linha

# Calcula a soma acumulada
accumulated_steps = [0] * (n + 1)
for i in range(1, n + 1):
    accumulated_steps[i] = accumulated_steps[i - 1] + steps[i - 1]

q = int(input())  # Lê o número de consultas

# Processa as consultas
for _ in range(q):
    interval_1, interval_2 = map(int, input().split())
    print(accumulated_steps[interval_2] - accumulated_steps[interval_1 - 1])
