players_array = input()
players = []
for player in players_array:
    players.append(player)

count = 0

for i in range(len(players)):
    if i != (len(players) - 1):
        if players[i] == players[i + 1]:
            count += 1
        else:
            if count < 6:
                count = 0

print('YES') if count >= 6 else print('NO')
