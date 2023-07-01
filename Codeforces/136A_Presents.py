n = int(input())
gifts = list(map(int, input().split()))
result = []

for i in range(len(gifts)):
    result.append(0)

for j in range (len(gifts)):
    result[gifts[j] - 1] = j + 1

for r in result:
    print(r, end=' ')

print()
