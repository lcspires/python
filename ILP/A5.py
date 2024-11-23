aluno = input()
centro_oeste = {"Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"}
sul = {"Paraná", "Santa Catarina", "Rio Grande do Sul"}
estados_validos = centro_oeste | sul  # União dos dois conjuntos
acertos = 0

for _ in range(6):
    estado = input()
    if estado in estados_validos:
        acertos += 1

print(f"{aluno}, sua pontuação é de {acertos} pontos.")
