n, k = map(int, input().split())

while k != 0:
    if n % 10 == 0:
        n = int(str(n)[0:-1])
    else:
        n -= 1

    k -= 1

print(n)
