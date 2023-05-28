N = int(input())
stones_array = input()
stones = []

for stone in stones_array:
    stones.append(stone)


def calculateStones(N, stones):
    result = 0
    while (result != N):
        counter = 0
        for i in range(len(stones)):
            if i != len(stones) - 1:
                if stones[i] == stones[i + 1]:
                    stones.pop(i)
                    counter += 1
                    break

        if counter == 0:
            return result
        
        result += 1
    
    return result

        
print(calculateStones(N, stones))

# 10
# GGBRBRGGRB