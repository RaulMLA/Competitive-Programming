word = input()

lowercase, uppercase = 0, 0

for w in word:
    if w.lower() != w:
        uppercase += 1
    else:
        lowercase += 1

print(word.lower()) if lowercase >= uppercase else print(word.upper())
