class Results:

	def __init__(self, filename):
		self.filename = filename
		self.hits = [0] * 41

	def addHitResults(self, hits):
		for i in range(0, 41):
			self.hits[i] += hits[i]

	def write(self):
		file = open(self.filename, "w")
		file.write("Hit frequency;\"=SUM(b2:b42)\";\n")
		for i in range(0, len(self.hits)):
			file.write("%i;%i;\"=b%i/b$1\"\n" % (i, self.hits[i], i + 2))
		file.close()