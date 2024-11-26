def busca_binaria(lista, item):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == item:
            return True
        elif lista[meio] < item:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return False

# Leitura da entrada
n = int(input())  # Número de espécies
especies = [input().strip() for _ in range(n)]  # Lista de espécies
q = int(input())  # Número de requisições
for _ in range(q):
    especie = input().strip()  # Espécie a ser verificada
    if busca_binaria(especies, especie):
        print(f"{especie} vive!")
    else:
        print(f"{especie} foi extinto :(")
