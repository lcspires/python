n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

digits = [0] * 101  # Lista para armazenar os dígitos

for i in range(n):
    if i % 4 == 0:
        digit = a[i] * b[i]
    elif i % 4 == 1:
        digit = a[i] - b[i]
    elif i % 4 == 2:
        digit = a[i] // b[i]
    else:
        digit = a[i] ** b[i]  # Usando o operador ** para exponenciação

    while digit >= 10:
        digit //= 10  # Obtendo o primeiro dígito

    if digit < 0:
        digit *= -1  # Tornando o dígito positivo, caso seja negativo

    digits[i] = digit

# Exibindo os 6 últimos dígitos
if n > 6:
    for i in range(n - 6, n):
        print(digits[i], end="")
else:
    for i in range(6):
        print(digits[i], end="")
