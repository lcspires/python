n = int(input())
balls = input().split()

balls_total = 0
for i in range(n):
    if balls[i] == '*':
        balls_total += 1

if balls_total != 7:
    print("Pedido negado")
else:
    print("Pedido realizado")
    ball_number = 1
    for i in range(n):
        if balls[i] == '*':
            print(ball_number, end=" ")
            ball_number += 1
        else:
            print('$', end=" ")
