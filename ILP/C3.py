n = int(input())

if n < 2:
    print(f"{n} não é primo")
else:
    eh_primo = True
    for i in range(2, int(n**0.5) + 1):
        print(i)
        if n % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print(f"{n} he primo")
    else:
        print(f"{n} nao he primo")
