stops = int(input())

min_capacity = 0
current = 0

while stops != 0:

    a, b = map(int, input().split())

    current = current - a + b

    min_capacity = max(min_capacity, current)

    stops -= 1

print(min_capacity)
