year = str(int(input()) + 1)

while True:
    nums = []
    
    for n in year:
        if n not in nums:
            nums.append(n)
    
    if len(nums) == len(year):
        break
    
    year = str(int(year) + 1)

print(year)
