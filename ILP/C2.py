def converter_segundos(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60

    return f"{horas} h {minutos} m {segundos_restantes} s"

C, O, L, X = map(int, input().split())

# Limitamo-nos pelo ingrediente que esgota primeiro:
pu_deans = min(C // 4, O // 8, L // 2, X // 1)

total_segundos = pu_deans * 1259

print(converter_segundos(total_segundos))
