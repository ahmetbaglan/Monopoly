from board import *

class Results:

	def __init__(self, filename):
		self.filename = filename
		# Generate an empty array to save the times a player has passed a tile
		self.hits = [0] * 41

	def addHitResults(self, hits):
		# Add hits given to the local hits array
		for i in range(0, 41):
			self.hits[i] += hits[i]

	def write(self):
		# Open the file
		file = open(self.filename, "w")
		
		# Write a title and the sum of all the tile hits
		file.write("Hit frequency;\"=SUM(b2:b42)\";\n")
		
		# Write the tile index, the hit count and the chance
		for i in range(0, len(self.hits)):
			file.write("\"%s\";%i;\"=b%i/b$1\"\n" % (Board.TILE_NAME[i], self.hits[i], i + 2))

		# Close and write the file
		file.close()