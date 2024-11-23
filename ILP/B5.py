n = int(input())
for _ in range(n):
    # Lê o nome completo e divide em palavras
    nome_completo = input().split()
    
    # Abrevia os primeiros nomes
    abreviacao = " ".join([nome[0].upper() + "." for nome in nome_completo[:-1]])
    
    # Último nome com a primeira letra maiúscula
    ultimo_nome = nome_completo[-1].capitalize()
    
    # Combina as abreviações com o último nome
    print(f"{abreviacao} {ultimo_nome}")
