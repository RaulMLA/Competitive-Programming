n = int(input())
magnets = []
groups = 1

while n > 0:
    magnets.append(input())
    n -= 1

for i in range(len(magnets)):
    if i != len(magnets) - 1:
        if magnets[i][1] == magnets[i+1][0]:
            groups += 1

print(groups)
