n_k = [int(x) for x in input().split()]
k = n_k[1] - 1
scores = [int(x) for x in input().split()]

counter = 0

for score in scores:
    if score >= scores[k] and score != 0:
        counter += 1
    if score < scores[k]:
        break

print(counter)
