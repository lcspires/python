n = int(input())

for x in range(n):
    valor_gasto = 0.0
    m = int(input())
    for y in range(m):
        p, q = input().split()
        p = float(p)
        q = int(q)
        valor_gasto += (p*q)
    
    print(f"R$ {valor_gasto:.2f}")
