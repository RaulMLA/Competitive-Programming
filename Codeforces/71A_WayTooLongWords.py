N = int(input())
results = []

while N != 0:

    string = input()

    if len(string) <= 10:
        results.append(string)
    else:
        count = 0
        for i in range(1, len(string) - 1):
            count += 1
        results.append('%s%i%s' %(string[0], count, string[-1]))

    N -= 1

for r in results:
    print(r)
