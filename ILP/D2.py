pontuacao_lucas = 0
pontuacao_pedro = 0

for x in range(3):
    L, P = map(int, input().split())
    pontuacao_lucas += L
    pontuacao_pedro += P

if pontuacao_lucas > pontuacao_pedro:
    print("Lucas")
elif pontuacao_pedro > pontuacao_lucas:
    print("Pedro")
else:
    print("Empate")
