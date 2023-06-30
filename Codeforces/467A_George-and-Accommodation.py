n = int(input())
total = 0

while (n > 0):
    
    p, q = map(int, input().split())
    if (q - p >= 2):
        total += 1
    
    n -= 1

print(total)
