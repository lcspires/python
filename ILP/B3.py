while True:
    entrada = input()
    if entrada == "#":
        break
    inicial, saturacao = entrada.split()
    saturacao = int(saturacao)
    if saturacao < 90:
        print(f"{inicial} Internação")
    else:
        print(f"{inicial} Alta")
