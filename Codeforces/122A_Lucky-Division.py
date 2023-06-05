n = int(input())
lucky_digits = ['4', '7']

def checkLucky(n: int):
    for digit in str(n):
        if digit not in lucky_digits:
            return False
    
    return True

if checkLucky(n):
   print('YES')
else:
    count = 4
    divisible = False
    while count <= n:
        if checkLucky(count) and n % count == 0:
            divisible = True
            print('YES')
            break
        
        count += 1

    if not divisible:
        print('NO')
