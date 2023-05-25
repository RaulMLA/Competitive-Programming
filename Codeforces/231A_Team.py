N = int(input())
friends = 0

while N != 0:

    numbers = [int(x) for x in input().split()]

    count = 0
    
    for n in numbers:
        if n == 1:
            count += 1

    if count >= 2:
        friends += 1
        
    N -= 1

print(friends)
