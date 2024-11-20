"""
Boas Práticas.

Para deixar o código mais legível em estruturas mais complexas.

Modo de usar:

Desenvolver a lógica dentro de uma função, modularizar.
Pois, facilita a reutilização e testes.

Separar entrada/saída pensando em legibilidade.
"""

def guessing_game(numero_secreto, numero_jogador):
    if numero_secreto == numero_jogador:
        return "Você acertou!"
    else:
        return "Você errou!"


# Lendo os números de entrada
X, Y = map(int, input().split())

# Chamando a função e exibindo o resultado
print(guessing_game(X, Y))
