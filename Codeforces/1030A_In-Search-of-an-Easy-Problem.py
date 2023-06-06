n = int(input())
numbers = list(map(int, input().split()))

print('HARD') if numbers.count(1) > 0 else print('EASY')
