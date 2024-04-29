from datetime import date
from team import Team
from fourPlaysGraph2 import maxGraphs
import random as rd

# date in year, month, day

# This will generate a random correct schedule

# All of these hard-coded data points will be entered by the user
startDate = date(2022, 10, 18)
endDate = date(2023, 4, 9)
maxGames = 82

# West = 1, East = 2
# Northwest = 1, Pacific = 2, Southwest = 3, Atlantic = 4, Central = 5, Southeast = 6
teamInfo = {
"Atlanta Hawks": [2, 6, 0],
"Boston Celtics": [2, 4, 1],
"Brooklyn Nets": [2, 4, 2],
"Charlotte Hornets": [2, 6, 3],
"Chicago Bulls": [2, 5, 4],
"Cleveland Cavaliers": [2, 5, 5],
"Dallas Mavericks": [1, 3, 6],
"Denver Nuggets": [1, 1, 7],
"Detroit Pistons": [2, 5, 8],
"Golden State Warriors": [1, 2, 9],
"Houston Rockets": [1, 3, 10],
"Indiana Pacers": [2, 5, 11],
"Los Angeles Clippers": [1, 2, 12],
"Los Angeles Lakers": [1, 2, 13],
"Memphis Grizzlies": [1, 3, 14],
"Miami Heat": [2, 6, 15],
"Milwaukee Bucks": [2, 5, 16],
"Minnesota Timberwolves": [1, 1, 17],
"New Orleans Pelicans": [1, 3, 18],
"New York Knicks": [2, 4, 19],
"Oklahoma City Thunder": [1, 1, 20],
"Orlando Magic": [2, 6, 21],
"Philadelphia 76ers": [2, 4, 22],
"Phoenix Suns": [1, 2, 23],
"Portland Trail Blazers": [1, 1, 24],
"Sacramento Kings": [1, 2, 25],
"San Antonio Spurs": [1, 3, 26],
"Toronto Raptors": [2, 4, 27],
"Utah Jazz": [1, 1, 28],
"Washington Wizards": [2, 6, 29],
}

# This array will keep track of which conference teams will play each other 4 times
# It will be an array of arrays
conference4Plays = []
for i in range(0, len(teamInfo)):
    tempArray = []
    conference4Plays.append(tempArray)

teams = []

for i in teamInfo:
    t = Team(i, list(teamInfo.keys()).index(i),teamInfo[i][0], teamInfo[i][1])
    teams.append(t)

#for i in range(0, len(teams)-1):
#print(teams[i].name + " | " + str(teams[i].conference) + " | " + str(teams[i].division))
# This produces some teams with less than 82 games
#for i in teams:
#   for j in teamInfo:
#       if i.name == j:
#           i.teamPlayCount.append(0)
#       else:
#           if i.conference == teamInfo[j][0]:
#               if i.division == teamInfo[j][1]:
#                   i.teamPlayCount.append(4)
#               # If i is not filled, j is not filled, i is not already on j, and j is not already in i
#               elif len(conference4Plays[i.index]) < 6 and not conference4Plays[i.index].count(j) and not conference4Plays[list(teamInfo.keys()).index(j)].count(i) and len(conference4Plays[list(teamInfo.keys()).index(j)]) < 6:
#                   i.teamPlayCount.append(4)
#                   conference4Plays[i.index].append(j)
#                   conference4Plays[list(teamInfo.keys()).index(j)].append(i.name)
#               else:
#                   i.teamPlayCount.append(3)
#           else:
#               i.teamPlayCount.append(2)

# This produces some (less than before) teams with less than 82 games
#for i in teams:
#    for j in teams:
#        if i.teamPlayCount[j.index] == 0:
#            if i.name == j.name:
#                i.teamPlayCount[j.index] = 0
#            else:
#                if i.conference == j.conference:
#                    if i.division == j.division:
#                        i.teamPlayCount[j.index] = 4
#                else:
#                    i.teamPlayCount[j.index] = 2

# This is to verify each team play each other and the conference4plays are filled
#for i in teams:
#    if len(conference4Plays[i.index]) > 6 or len(conference4Plays[i.index]) < 6:
#        print(i.name + " are playing "  + str(len(conference4Plays[i.index])) + " teams")
#    for j in conference4Plays[i.index]:
#       if(not conference4Plays[list(teamInfo.keys()).index(j)].count(i.name)):
#            print(i.name + " are playing " + j + " but " + j + " are not playing " + i.name)

# This is to verify each team has 82 games
#for i in teams:
#    if i.gamesScheduled() != 82:
#        print(i.name + " are playing " + str(i.gamesScheduled()) + " games")

# This is to check individual teams' same conference 4 plays
#cont = 1
#while cont:
#    choice = input('Team number or e for exit ')
#    if choice == "e":
#        cont =  0
#    else:
#        for i in teamInfo:
#            print(i + " are played " + str(teams[list(teamInfo.keys()).index(choice)].teamPlayCount[list(teamInfo.keys()).index(i)]) + " times")
#        print(str(teams[list(teamInfo.keys()).index(choice)].teamPlayCount.count(4)) + " teams are played 4 times")
#        print(str(teams[list(teamInfo.keys()).index(choice)].teamPlayCount.count(3)) + " teams are played 3 times")
#        print(str(teams[list(teamInfo.keys()).index(choice)].teamPlayCount.count(2)) + " teams are played 2 times")

# maxGraphs requires a given graph to generate which same-conference teams play each other four times

# This generates the index of the teams that are in the same division
#temp = []
#for i in teamInfo:
#    temp.append([])
#    for j in teamInfo:
#        if teamInfo[j][1] == teamInfo[i][1] and i != j:
#            temp[teamInfo[i][2]].append(teamInfo[j][2])
#
#print(temp)

west = []
east = []
for i in teamInfo:
    if teamInfo[i][0] == 1:
            west.append(i)
for i in teamInfo:
    if teamInfo[i][0] == 1:
        east.append(i)

#print(west)

westSD = []
wcount = 0
for i in west:
    westSD.append([])
    for j in west:
        if teamInfo[i][1] == teamInfo[j][1] and not j == i:
            westSD[wcount].append(west.index(j))
    wcount += 1

eastSD = []
ecount = 0
for i in east:
    eastSD.append([])
    for j in west:
        if teamInfo[i][1] == teamInfo[j][1] and not j == i:
            eastSD[ecount].append(east.index(j))
    wcount += 1

givenGraph = [[1, 12, 5, 9], [0, 7, 2, 9], [1, 6, 4, 13], [14, 7, 8, 5], [2, 5, 13, 9], [0, 3, 4, 8], [2, 10, 11, 12], [1, 3, 12, 11], [3, 5, 11, 13], [0, 1, 4, 10], [6, 9, 14, 13], [6, 7, 8, 14], [0, 6, 7, 12], [2, 4, 8, 10], [3, 10, 11, 12]]

maxGraphs(15, 6, givenGraph, westSD)