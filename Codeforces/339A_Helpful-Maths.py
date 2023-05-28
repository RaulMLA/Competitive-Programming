operation = input()
numbers = []

for i in range(1, 4):
    for o in operation:
        if o == str(i):
            numbers.append(i)

for i in range(0, len(numbers)):
    if i != len(numbers) - 1:
        print('{}+' .format(numbers[i]), end = "")
    else:
        print('{}' .format(numbers[i]))
