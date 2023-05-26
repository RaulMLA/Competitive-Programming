string_A = input()
string_B = input()

if string_A.lower() < string_B.lower():
    print("-1")
elif string_A.lower() > string_B.lower():
    print("1")
else:
    print("0")
