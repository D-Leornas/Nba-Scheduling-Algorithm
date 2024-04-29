class Team:
    def __init__(self, name, index, conference, division):
        self.name = name
        self.index = index
        self.conference = conference
        self.division = division
        self.teamPlayCount = []
        for i in range(0, 30):
            self.teamPlayCount.append(0)
        
    def gamesScheduled(self):
        sum = 0
        for i in self.teamPlayCount:
            sum += i
        return sum