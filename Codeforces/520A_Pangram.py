n = int(input())
s = input().lower()

latin_alphabet = 'abcdefghijklmnopqrstuvwxyz'

result = 'YES'

for c in latin_alphabet:
    if c not in s:
        result = 'NO'
        break
        
print(result)
