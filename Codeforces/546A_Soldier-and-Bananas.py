k, n, w = map(int, input().split())
total = 0

i = 1
while w != 0:
    total += i * k
    i += 1
    w -= 1

print(total - n) if total - n >= 0 else print(0)
