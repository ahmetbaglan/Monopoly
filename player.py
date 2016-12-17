from board import *

class Player:

	def __init__(self):
		self.position = 0
		self.consecutiveDoubles = 0

	def move(self, board, diceResults):
		# Determine whether to go to jail due to double throws
		goingToJail = False
		if diceResults[1]:
			# Add one to the number of consecutive doubles
			self.consecutiveDoubles += 1

			# Signal to go to jail if 3 doubles in a row
			if self.consecutiveDoubles >= 3:
				goingToJail = True
				# Reset consecutive throws
				self.consecutiveDoubles = 0
		else:
			# Reset consecutive doubles every time different numbers are roled
			self.consecutiveDoubles = 0

		# Calculate new position, overflow if necessary
		newPosition = self.getNewPosition(diceResults[0], board)
		# Add one to position, if went past jail
		if (newPosition >= Board.TILES_JAIL[0] and newPosition < 35) and (
				self.position < Board.TILES_JAIL[0] or self.position > 35):
			newPosition += 1
		# Apply new position
		self.position = newPosition

	def getNewPosition(self, offset, board):
		return (self.position + offset) % board.getSize()

	def doChanceCard(self, card, board):
		# Check the type of the chance card
		if card.kind == "advance":
			# Move to next utilities if necessary
			if card.value == "utility":
				# Keep track if suitable utilities is found
				moved = False
				# Go through possible utilities
				for pos in Board.TILES_UTILITIES:
					# If player is before current utility, go to that one
					if self.position < pos:
						self.position = pos;
						moved = True
						break

				# If not yet moved, go to first utilities in array
				if not moved:
					self.position = Board.TILES_UTILITIES[0]

			# Move to next railroad if necessary
			elif card.value == "railroad":
				# Keep track if suitable railroad is found
				moved = False
				# Go through possible railroad
				for pos in Board.TILES_TRANSPORT:
					# If player is before current railroad, go to that one
					if self.position < pos:
						self.position = pos;
						moved = True
						break

				# If not yet moved, go to first railroad in array
				if not moved:
					self.position = Board.TILES_TRANSPORT[0]

			# If negative, thus should move back, do that
			elif card.value <= 0:
				self.position = self.getNewPosition(-3, board)

			# Move player to given position otherwise
			else:
				self.position = card.value

	def doCommunityCard(self, card, board):
		# Go to given position if card is of the advance kind
		if card.kind == "advance":
			self.position = card.value