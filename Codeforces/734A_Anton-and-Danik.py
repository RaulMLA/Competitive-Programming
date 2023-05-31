N = int(input())
games = input()
a, d = 0, 0

for g in games:
    if g == 'A':
        a+= 1
    else:
        d += 1

if a > d:
    print('Anton')
elif a < d:
    print('Danik')
else:
    print('Friendship')
    