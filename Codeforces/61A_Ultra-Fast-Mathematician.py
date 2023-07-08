first = input()
second = input()
result = ''

for i in range(len(first)):
    if int(first[i]) ^ int(second[i]):
        result += '1'
    else:
        result += '0'

print(result)
