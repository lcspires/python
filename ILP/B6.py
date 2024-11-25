def main():
    # Ler o tamanho da plantação
    n = int(input("Digite o tamanho da plantação (N x N): "))
    
    # Ler a matriz da plantação
    matriz = []
    print(f"Digite os pesos das abóboras para {n} linhas:")
    for _ in range(n):
        linha = list(map(int, input().split()))
        matriz.append(linha)
    
    # Ler as linhas específicas de Harry e Ron
    x, y = map(int, input("Digite as linhas X (Harry) e Y (Ron): ").split())

    # Inicializar o peso total coletado por Harry e Ron
    peso_harry = 0
    peso_ron = 0

    # Colheita de Harry (linha horizontal X)
    for coluna in range(n):
        peso_harry += matriz[x][coluna]

    # Colheita de Ron (coluna vertical Y)
    for linha in range(n):
        peso_ron += matriz[linha][y]

    # Tratar o ponto de interseção (X, Y)
    # Subtrair o peso da abóbora no ponto de interseção do total de Harry
    peso_harry -= matriz[x][y]

    # Exibir os resultados
    print(f"Peso total de Harry: {peso_harry}")
    print(f"Peso total de Ron: {peso_ron}")


# Execução do programa
if __name__ == "__main__":
    main()
