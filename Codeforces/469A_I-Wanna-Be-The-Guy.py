n = int(input())
p = list(map(int, input().split()))[1:]
q = list(map(int, input().split()))[1:]
condition = True

while n > 0:
    
    if n not in p and n not in q:
        condition = False

    n -= 1

print('I become the guy.') if condition else print('Oh, my keyboard!')
