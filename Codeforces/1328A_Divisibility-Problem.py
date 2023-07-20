t = int(input())

while t > 0:
    a, b = map(int, input().split())
    counter = 0

    while True:
        if (a % b == 0):
            break
        else:
            counter += 1
            a += 1
    
    print(counter)

    t -= 1
