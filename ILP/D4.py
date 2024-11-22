operation, dimension = map(int, input().split())

if operation == 1:
    vector1 = list(map(int, input().split()))
    vector2 = list(map(int, input().split()))

    for i in range(dimension):
        vector1[i] += vector2[i]
    
    print(*vector1)

elif operation == 2:
    vector1 = list(map(int, input().split()))
    vector2 = list(map(int, input().split()))

    # list comprehensions
    scalar_product = sum(vector1[i] * vector2[i] for i in range(dimension))

"""
for i in range(dimension):
    # Multiplica os elementos correspondentes dos dois vetores
    scalar_product += vector1[i] * vector2[i]
"""

    print(scalar_product)

else:
    vector = list(map(int, input().split()))
    scalar = int(input())

    # list comprehensions
    vector = [x * scalar for x in vector]

    print(*vector)
