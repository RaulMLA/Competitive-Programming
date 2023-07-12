n = int(input())

while(n > 0):

    word = input()

    for i in range(0, len(word), 2):
        if i != len(word) - 1:
            print(word[i], end='')
    print(word[-1])
    n -= 1
