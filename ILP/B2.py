#Evitando crash do programa com (try/except)

def obter_mes(numero_mes):
    """
    Retorna o nome do mês correspondente ao número fornecido.

    Args:
        numero_mes (int): Número do mês (1 a 12).

    Returns:
        str: Nome do mês correspondente.
    """
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    if 1 <= numero_mes <= 12:
        return meses[numero_mes - 1]
    else:
        raise ValueError("Número do mês deve estar entre 1 e 12.")

try:
    num_mes = int(input("Digite o número do mês: "))
    print(obter_mes(num_mes))
except ValueError as e:
    print(f"Entrada inválida: {e}")
