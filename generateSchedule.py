from datetime import date
from team import Team
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
"Atlanta Hawks": [2, 5],
"Boston Celtics": [2, 4],
"Brooklyn Nets": [2, 4],
"Charlotte Hornets": [2, 6],
"Chicago Bulls": [2, 5],
"Cleveland Cavaliers": [2, 5],
"Dallas Mavericks": [1, 3],
"Denver Nuggets": [1, 1],
"Detroit Pistons": [2, 5],
"Golden State Warriors": [1, 2],
"Houston Rockets": [1, 3],
"Indiana Pacers": [2, 5],
"Los Angeles Clippers": [1, 2],
"Los Angeles Lakers": [1, 2],
"Memphis Grizzlies": [1, 3],
"Miami Heat": [2, 6],
"Milwaukee Bucks": [2, 5],
"Minnesota Timberwolves": [1, 1],
"New Orleans Pelicans": [1, 3],
"New York Knicks": [2, 4],
"Oklahoma City Thunder": [1, 1],
"Orlando Magic": [2, 6],
"Philadelphia 76ers": [2, 4],
"Phoenix Suns": [1, 2],
"Portland Trail Blazers": [1, 1],
"Sacramento Kings": [1, 2],
"San Antonio Spurs": [1, 3],
"Toronto Raptors": [2, 4],
"Utah Jazz": [1, 1],
"Washington Wizards": [2, 6],
}

teams = []

for i in teamInfo:
    t = Team(i, teamInfo[i][0], teamInfo[i][1])
    teams.append(t)

#for i in range(0, len(teams)-1):
#    print(teams[i].name + " | " + str(teams[i].conference) + " | " + str(teams[i].division))

for i in teams:
    for j in teamInfo:
        if i.name == j:
            i.teamPlayCount.append(0)
        if i.conference == teamInfo[j][0]:
            #schedule