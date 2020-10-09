import random

def printTeam(players):
    for i, player in enumerate(players):
        if i != len(players) - 1:
            print(player, end = ", ")
        else:
            print(player)

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


for i in range(len(players)):
    if players[i] not in teamOne:
        teamTwo.append(players[i])

print(f"Team One: ", end = "")
printTeam(teamOne)

print(f"Team Two: ", end = "")
printTeam(teamTwo)