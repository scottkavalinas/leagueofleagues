from player import Player

#team can be 1 of 4 types
#teams have players
class Team:

	def __init__(self,name):
		self.name = name
		self.roster = []

	def getName(self):
		return self.name
	def addPlayer(self,player):
		
		self.roster.append(Player(player))


new = Team("NFL")