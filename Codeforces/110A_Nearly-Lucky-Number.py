numbers = input()
lucky_digits = ['4', '7']

count = 0
for n in numbers:
    if n in lucky_digits:
        count += 1

condition = False
if str(count) in lucky_digits:
    condition = True

print('NO') if not condition else print('YES')
