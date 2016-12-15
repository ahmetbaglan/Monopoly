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
		if newPosition >= board.tilesJail[0] and self.position < board.tilesJail[0]:
			newPosition += 1
		# Apply new position
		self.position = newPosition