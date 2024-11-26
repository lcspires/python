def contar_inundados(mapa, h):
    contagem = 0
    for linha in mapa:
        for altura in linha:
            if altura <= h:
                contagem += 1
    return contagem

# Leitura da entrada
n, m = map(int, input().split())  # Largura e comprimento da foto
mapa = [list(map(int, input().split())) for _ in range(n)]

q = int(input())  # Número de consultas
consultas = [int(input()) for _ in range(q)]

# Respondendo às consultas
for h in consultas:
    print(contar_inundados(mapa, h))
