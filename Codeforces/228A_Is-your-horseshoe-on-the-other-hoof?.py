colors = list(map(int, input().split()))
checked = []
result = 0

for s in colors:
    if s not in checked and colors.count(s) > 1:
        result += colors.count(s) - 1
    checked.append(s)

print(result)
