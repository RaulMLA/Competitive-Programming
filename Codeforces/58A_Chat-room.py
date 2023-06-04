s = input()
word = 'hello'

for letter in s:
    if len(word) > 0:
        if letter == word[0]:
            word = word[1:]

print('YES') if word == '' else print('NO')
