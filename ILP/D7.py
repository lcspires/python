# Leitura da entrada
n, m = map(int, input().split())
ratings = list(map(int, input().split()))
pontuacoes = []

# Lendo as pontuações dos problemas
for _ in range(n):
    problemas = list(map(int, input().split()))
    pontuacoes.append(sum(problemas))

# Encontrando a mediana
pontuacoes_ordenadas = sorted(pontuacoes)
mediana = pontuacoes_ordenadas[n // 2]

# Calculando o rating final e armazenando dados
participantes = []
for i in range(n):
    variacao = (pontuacoes[i] - mediana) // 100
    rating_final = ratings[i] + variacao
    participantes.append((pontuacoes[i], rating_final))

# Função para determinar a cor com base no rating final
def determinar_cor(rating):
    if rating < 1200:
        return "Gray"
    elif rating < 1400:
        return "Green"
    elif rating < 1600:
        return "Cyan"
    elif rating < 1900:
        return "Blue"
    elif rating < 2100:
        return "Purple"
    elif rating < 2500:
        return "Yellow"
    elif rating < 3000:
        return "Red"
    else:
        return "Red Nutella"

# Ordenando os participantes por pontuação decrescente
participantes.sort(key=lambda x: -x[0])

# Determinando a cor de cada participante
for _, rating_final in participantes:
    print(determinar_cor(rating_final))
