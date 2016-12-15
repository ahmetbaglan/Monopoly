from util import *
from board import *

class Game:

	def __init__(self, players, rounds):
		self.players = players
		self.board = Board()
		self.rounds = rounds

	def run(self):
		# Play the game for a given amount of rounds
		for i in range(0, self.rounds):
			self.round()

	def round(self):
		# Each round, every player should get its turn
		for player in self.players:
			self.turn(player)

	def turn(self, player):
		# Get number of eyes on dice
		diceResults = diceThrow()
		# Move the player to new position
		goingToJail = player.move(self.board, diceResults)

		# Get tile type
		tileType = self.board.getTileType(player.position)

		# Set to go to jail if on 'Go To Jail' tile
		if tileType == "gotojail":
			goingToJail = True

		# Override player's position if player should fo to prison
		if goingToJail:
			player.position = Board.TILES_JAIL[0]

		# Log the fact that a player has landed on a tile
		self.board.hit(player.position)

		# Go again if not on jail and has thrown double
		if tileType != "jail" and diceResults[1]:
			self.turn(player)