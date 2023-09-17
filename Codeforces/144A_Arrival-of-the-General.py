n = int(input())
soldiers = [int(x) for x in input().split()]

seconds = 0

counter = 1

while True:
    
    print(counter, end = ' - ')
    print(soldiers)
    counter += 1

    condition = False
    for i in range(n):
        if soldiers[0] == max(soldiers) and soldiers[-1] == min(soldiers):
            condition = True
            break

        if soldiers[i] == max(soldiers) and soldiers[i] != soldiers[0]:
            keep = soldiers[i]
            soldiers[i] = soldiers[i - 1]
            soldiers[i - 1] = keep
            seconds += 1
            break

        if soldiers[i] == min(soldiers) and soldiers[i] != soldiers[-1]:
            keep = soldiers[i]
            soldiers[i] = soldiers[i + 1]
            soldiers[i + 1] = keep
            seconds += 1
            break
    
    if condition:
        print(soldiers)
        break

print(seconds)
