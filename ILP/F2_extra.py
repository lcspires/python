def calcular_peso_ideal(altura):
    """
    Calcula o peso ideal para uma altura dada com base no IMC saudável (entre 18,5 e 24,9).
    
    Args:
        altura (float): A altura da pessoa em metros.
    
    Returns:
        tuple: Peso mínimo, peso máximo e peso ideal (média).
    """
    # IMC mínimo e máximo para faixa saudável
    imc_minimo = 18.5
    imc_maximo = 24.9

    # Calculando o peso mínimo e máximo com base na altura
    peso_minimo = imc_minimo * (altura ** 2)
    peso_maximo = imc_maximo * (altura ** 2)

    # Peso ideal é a média entre o peso mínimo e o peso máximo
    peso_ideal = (peso_minimo + peso_maximo) / 2

    return peso_minimo, peso_maximo, peso_ideal

def exibir_resultados(peso_minimo, peso_maximo, peso_ideal):
    """
    Exibe os resultados de peso mínimo, máximo e ideal formatados.
    
    Args:
        peso_minimo (float): O peso mínimo ideal.
        peso_maximo (float): O peso máximo ideal.
        peso_ideal (float): O peso ideal (média entre o mínimo e máximo).
    """
    print(f"Peso mínimo ideal: {peso_minimo:.2f} kg")
    print(f"Peso máximo ideal: {peso_maximo:.2f} kg")
    print(f"Peso ideal: {peso_ideal:.2f} kg")

def main():
    altura = float(input("Informe sua altura (em metros): "))
    
    peso_minimo, peso_maximo, peso_ideal = calcular_peso_ideal(altura)
    
    exibir_resultados(peso_minimo, peso_maximo, peso_ideal)

# Chama a função principal para executar o programa
if __name__ == "__main__":
    main()
