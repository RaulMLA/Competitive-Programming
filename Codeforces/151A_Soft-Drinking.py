n, k, l, c, d, p, nl, np = [int(x) for x in input().split()]

toasts = (k * l) // nl
lime_toasts = c * d
salt_toasts = p * np

print(min(toasts, lime_toasts, salt_toasts) // n)
