n = int(input())
numbers = list(map(int, input().split()))

index_odd = 0
index_even = 0
count_odd = 0
count_even = 0

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        index_even = i + 1
        count_even += 1
    else:
        index_odd = i + 1
        count_odd += 1

print(index_odd) if count_odd == 1 else print(index_even)
