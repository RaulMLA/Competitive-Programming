x = int(input())
steps = [1, 2, 3, 4, 5]
count = 0

while True:
    for step in reversed(steps):
        if x - step >= 0:
            x -= step
            count += 1
            break
    
    if x == 0:
        break


print(count)
