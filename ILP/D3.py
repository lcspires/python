d, e = map(int, input().split())
dia_queda = 0

for i in range(1, d + 1):
    dano = int(input())
    e -= dano
    if e <= 0 and dia_queda == 0:
        dia_queda = i

if dia_queda > 0:
    print(dia_queda)
else:
    print("Resistiu")
