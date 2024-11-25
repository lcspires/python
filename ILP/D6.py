def main():
    # Leitura do mapa 10x10
    mapa = []
    for _ in range(10):
        linha = input().split()
        mapa.append(linha)

    # Criar uma cópia do mapa para evitar alterações durante a análise
    novo_mapa = [linha[:] for linha in mapa]

    # Direções para verificar os vizinhos (cima, baixo, esquerda, direita)
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Iterar por cada célula do mapa
    for i in range(10):
        for j in range(10):
            if mapa[i][j] == 't':  # Encontrar terrenos ('t')
                # Verificar os vizinhos
                for di, dj in direcoes:
                    ni, nj = i + di, j + dj
                    # Se estiver dentro do mapa e vizinho for água, transforme em praia
                    if 0 <= ni < 10 and 0 <= nj < 10 and mapa[ni][nj] == '*':
                        novo_mapa[i][j] = 'p'
                        break

    # Imprimir o novo mapa corrigido
    for linha in novo_mapa:
        print(" ".join(linha))


# Execução do programa
if __name__ == "__main__":
    main()
