class Board:

	def __init__(self):
		# Define types of tiles on board
		self.tilesRealestate = [
				1,3,6,8,9,12,14,15,17,19,20,22,24,25,27,28,30,32,33,35,38,40]
		self.tilesChance = [7,23,37]
		self.tilesCommunity = [2,18,34]
		self.tilesUtilities = [13,29]
		self.tilesTransport = [5,16,26,36]
		self.tilesTax = [4,39]
		self.tilesNone = [10,21]
		self.tilesJail = [11]
		self.tilesGoToJail = [31]
		self.tilesGo = [0]

		# Check if total amount of tiles is correct
		tilesCount = self.getSize()
		if tilesCount != 41:
			print "Game board consists of %i tiles, instead of 41!" % tilesCount

		# Setup array to keep track of times a player had landed on a tile
		self.hits = [0] * 41

	def getTileType(self, tile):
		# Return a string of the type of tile corresponding with the index given
		if tile in self.tilesRealestate:
			return "realestate"
		elif tile in self.tilesChance:
			return "chance"
		elif tile in self.tilesCommunity:
			return "community"
		elif tile in self.tilesUtilities:
			return "utitlities"
		elif tile in self.tilesTransport:
			return "transport"
		elif tile in self.tilesTax:
			return "tax"
		elif tile in self.tilesJail:
			return "jail"
		elif tile in self.tilesGoToJail:
			return "gotojail"
		elif tile in self.tilesGo:
			return "go"
		else:
			return "none"


	def hit(self, tile):
		# Increment tile hit count in array
		self.hits[tile] += 1

	def getSize(self):
		return (len(self.tilesRealestate) + len(self.tilesChance) +
				len(self.tilesCommunity) + len(self.tilesUtilities) +
				len(self.tilesTransport) + len(self.tilesTax) +
				len(self.tilesNone) + len(self.tilesJail) +
				len(self.tilesGoToJail) + len(self.tilesGo))