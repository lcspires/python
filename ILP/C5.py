def add_large_numbers(num1, num2):
    # Garantir que num1 seja o menor e num2 o maior (em comprimento)
    if len(num1) > len(num2):
        num1, num2 = num2, num1

    # Inicializar o resultado e o carry
    result = []
    carry = 0

    # Inverter as strings para facilitar a soma da direita para a esquerda
    num1 = num1[::-1]
    num2 = num2[::-1]

    # Somar dígito a dígito
    for i in range(len(num2)):
        digit1 = int(num1[i]) if i < len(num1) else 0
        digit2 = int(num2[i])

        total = digit1 + digit2 + carry
        result.append(str(total % 10))  # Armazenar o dígito resultante
        carry = total // 10  # Atualizar o "vai-um"

    # Se sobrar um carry, adicionar ao final
    if carry:
        result.append(str(carry))

    # Reverter o resultado e retornar como string
    return ''.join(result[::-1])


# Leitura dos números de Fibonacci
fibonacci_n = input().strip()
fibonacci_n1 = input().strip()

# Calcula o próximo termo
fibonacci_n2 = add_large_numbers(fibonacci_n, fibonacci_n1)

# Imprime o resultado
print(fibonacci_n2)
