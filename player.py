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
		newPosition = (self.position + diceResults[0]) % board.getSize()
		# Add one to position, if went past jail
		if (newPosition >= Board.TILES_JAIL[0] and newPosition < 35) and (
				self.position < Board.TILES_JAIL[0] or self.position > 35):
			newPosition += 1
		# Apply new position
		self.position = newPosition