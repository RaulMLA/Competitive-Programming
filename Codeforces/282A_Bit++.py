n = int(input())
x = 0

while n != 0:
    statement = input()
    if statement in ['X++', '++X']:
        x += 1
        n -= 1
    if statement in ['X--', '--X']:
        x -= 1
        n -= 1

print(x)
