counter = 0
row1 = [int(x) for x in input().split()]
row2 = [int(x) for x in input().split()]
row3 = [int(x) for x in input().split()]
row4 = [int(x) for x in input().split()]
row5 = [int(x) for x in input().split()]

while (1 not in row3) or (1 != row3[2]):
    
    if 1 in row1:
        counter += 1
        row = row2
        row2 = row1
        row1 = row
    
    elif 1 in row2:
        counter += 1
        row = row3
        row3 = row2
        row2 = row
    
    elif 1 in row4:
        counter += 1
        row = row4
        row4 = row3
        row3 = row
    
    elif 1 in row5:
        counter += 1
        row = row5
        row5 = row4
        row4 = row

    elif 1 == row3[0]:
        counter += 1
        row = row3[1]
        row3[1] = row3[0]
        row3[0] = row
    
    elif 1 == row3[1]:
        counter += 1
        row = row3[2]
        row3[2] = row3[1]
        row3[1] = row
    
    elif 1 == row3[3]:
        counter += 1
        row = row3[3]
        row3[3] = row3[2]
        row3[2] = row
    
    elif 1 == row3[4]:
        counter += 1
        row = row3[4]
        row3[4] = row3[3]
        row3[3] = row

print(counter)
