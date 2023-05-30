N = int(input())
x, y, z = 0, 0, 0

while N != 0:
    numbers = [int(x) for x in input().split()]
    x += numbers[0]
    y += numbers[1]
    z += numbers[2]
    N -= 1

print('YES') if x == 0 and y == 0 and z == 0 else print('NO')
