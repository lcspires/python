S = float(input())

if S <= 3000:
    taxa = 0.15
    imposto = S * taxa
elif S > 3000 and S <= 6000:
    imposto = (3000 * 0.15) + ((S - 3000) * 0.20)
else:
    imposto = (3000 * 0.15) + (3000 * 0.20) + ((S - 6000) * 0.30)

salario_liquido = S - imposto

# Exibição dos valores com 2 casas decimais com f-string:
print(f"Imposto: R$ {imposto:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
