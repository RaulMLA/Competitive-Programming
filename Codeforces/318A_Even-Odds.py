n, k = map(int, input().split())
counter = 1

for i in range (1, n + 1, 2):
    if counter == k:
        print(i)
    counter += 1

if n > 1:
    for j in range (2, n + 1, 2):
        if counter == k:
            print(j)
        counter += 1
