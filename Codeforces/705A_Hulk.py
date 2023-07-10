n = int(input())

for i in range(n):
    print ('I hate', end=' ') if (i % 2) == 0 else print ('I love', end=' ')
    print ('it', end=' ') if i == n - 1 else print ('that', end=' ')

print()
