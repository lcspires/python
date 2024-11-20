# IMC ideal
altura = float(input("Informe sua altura (em metros): "))

peso_minimo = 18.5 * (altura ** 2)
peso_maximo = 24.9 * (altura ** 2)

peso_ideal = (peso_minimo + peso_maximo) / 2

print(f"Peso mínimo ideal: {peso_minimo:.2f} kg")
print(f"Peso máximo ideal: {peso_maximo:.2f} kg")
print(f"Peso ideal: {peso_ideal:.2f} kg")
