# Evitando o .reverse, mas não o list.

n = int(input())
items = list(map(int, input().split()))

reversed_items = []
for i in range(n - 1, -1, -1):
    reversed_items.append(items[i])

for item in reversed_items:
    print(item, end=" ")
