from team import Team

#owner has 4 teams


class Owner:

	def __init__(self,name):
		self.name = name

	def getName(self):
		return self.name

	def setTeam(self,team):
		self.nhl=team[0]
		self.nfl=team[1]
		self.mlb=team[2]
		self.nba=team[3]

	def addNHL(self,player):
		self.nhl.addPlayer(player)

nhl = Team("nhl")
nfl = Team("nfl")
mlb = Team("mlb")
nba = Team("nba")

owner = Owner("Scott")
teamList = [nhl,nfl,mlb,nba]
owner.setTeam(teamList)

owner.addNHL("McDavid")

print(owner.nhl.roster)