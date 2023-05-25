numbers = [int(x) for x in input().split()]

n = numbers[0]
m = numbers[1]
a = numbers[2]

print((-n // a) * (-m // a))
