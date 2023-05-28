word = input()
no_vowels, new_word = "", ""
vowels = ['A', 'O', 'Y', 'E', 'U', 'I',
          'a', 'o', 'y', 'e', 'u', 'i']

for letter in word:
    if letter not in vowels:
        no_vowels += letter.lower()

for letter in no_vowels:
    new_word = new_word + '.'
    new_word += letter

print(new_word)
