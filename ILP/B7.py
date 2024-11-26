# Entrada: quantidade de livros
n = int(input())

# Lista para armazenar os tamanhos dos livros
livros = []

# Leitura dos tamanhos dos livros
for _ in range(n):
    livros.append(input().strip())

# Ordenação manual usando o método de seleção (Selection Sort) em ordem decrescente
for i in range(n - 1):
    maior = i
    for j in range(i + 1, n):
        if len(livros[j]) > len(livros[maior]):
            maior = j
    # Troca o maior elemento encontrado com o elemento atual
    livros[i], livros[maior] = livros[maior], livros[i]

# Saída: livros organizados
for livro in livros:
    print(livro)
