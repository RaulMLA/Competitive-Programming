n, h = map(int, input().split())
heights = list(map(int, input().split()))
count = 0

for height in heights:
    if height > h:
        count += 2
    else:
        count += 1

print(count)
