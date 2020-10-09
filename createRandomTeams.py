import random

players = []
teamOne = []
teamTwo = []

print("Please enter all player names, seperated by a comma and a space (i.e: Joe, Chris, Bob)")
names = input("> ")
players = names.split(', ')

while len(teamOne) != int(len(players)/2):
    rand = random.randint(0, len(players) - 1)
    if players[rand] not in teamOne:
        teamOne.append(players[rand])


for i in range(6):
    if players[i] not in teamOne:
        teamTwo.append(players[i])

print(f"Team One: {teamOne[0]}, {teamOne[1]}, {teamOne[2]}")
print(f"Team Two: {teamTwo[0]}, {teamTwo[1]}, {teamTwo[2]}")