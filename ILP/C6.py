def main():
    # Leitura do número de brinquedos e dias
    n, m = map(int, input().split())

    # Inicializar a matriz de variações e a matriz de somas prefixadas
    matriz = []
    prefix_sum = []

    # Leitura da matriz de variações e cálculo das somas prefixadas
    for _ in range(n):
        linha = list(map(int, input().split()))
        matriz.append(linha)

        # Construção da soma prefixada para a linha atual
        prefix = [0] * (m + 1)
        for j in range(1, m + 1):
            prefix[j] = prefix[j - 1] + linha[j - 1]
        prefix_sum.append(prefix)

    # Leitura do número de requisições
    q = int(input())

    # Processamento das requisições
    resultados = []
    for _ in range(q):
        k, a, b = map(int, input().split())
        k -= 1  # Ajuste para índice 0-based
        # Cálculo da soma no intervalo [a, b]
        resultado = prefix_sum[k][b] - prefix_sum[k][a - 1]
        resultados.append(resultado)

    # Impressão dos resultados
    print("\n".join(map(str, resultados)))


# Execução do programa
if __name__ == "__main__":
    main()
