n = int(input())
coins = list(map(int, input().split()))
taken = []

while True:
    taken.append(max(coins))
    coins.remove(max(coins))
    
    if sum(taken) > sum(coins):
        break

print(len(taken))
