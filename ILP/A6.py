def ler_matriz(linhas, colunas):
    """Lê a matriz do tamanho especificado."""
    matriz = []
    for _ in range(linhas):
        matriz.append(list(map(int, input().split())))
    return matriz


def aplicar_ataques(matriz, tentativas):
    """Aplica os ataques na matriz."""
    bugs_restantes = sum(sum(1 for p in linha if p > 0) for linha in matriz)
    for _ in range(tentativas):
        linha, coluna = map(int, input().split())
        linha, coluna = linha - 1, coluna - 1
        if matriz[linha][coluna] > 0:  # Apenas atacar se houver bug
            matriz[linha][coluna] -= 1
            if matriz[linha][coluna] == 0:  # Se o bug morreu, decrementar o contador
                bugs_restantes -= 1
    return bugs_restantes


def main():
    linhas, colunas = map(int, input().split())
    matriz = ler_matriz(linhas, colunas)

    tentativas = int(input())
    bugs_restantes = aplicar_ataques(matriz, tentativas)

    if bugs_restantes == 0:
        print("HASTA LA VISTA BABY")
    else:
        print("I'LL BE BACK")


if __name__ == "__main__":
    main()
