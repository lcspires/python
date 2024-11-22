# Evitando o list(), mas não o if-in.

n = int(input())

esmeraldas = []

for _ in range(n):
    esmeraldas.append(int(input()))

chaos_esmeraldas = int(input())

if chaos_esmeraldas in esmeraldas:
    print(chaos_esmeraldas)
else:
    print(-1)
