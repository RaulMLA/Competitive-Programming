n, t = map(int, input().split())
s = list(input())
i = 0

while t != 0:
    i = 0
    while (i < n - 1):
        if i != n - 1:
            if s[i] == 'B' and s[i + 1] == 'G':
                s[i], s[i + 1] = s[i + 1], s[i]
                i += 1
            i += 1
    t -= 1

for letter in s:
    print(letter, end="")
print()
