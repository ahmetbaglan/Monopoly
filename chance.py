import random
from chance import *

class ChanceCard:

	def __init__(self, kind, value):
		self.kind = kind
		self.value = value

class ChancePile:

	CARDS = [
		ChanceCard("advance", 0),
		ChanceCard("advance", 25),
		ChanceCard("advance", 12),
		ChanceCard("advance", "utility"),
		ChanceCard("advance", "railroad"),
		ChanceCard("cash", 50),
		ChanceCard("escapejail", None),
		ChanceCard("advance", -3),
		ChanceCard("tax", [25, 100]), # 25 for house, 100 for hotel
		ChanceCard("cash", -15),
		ChanceCard("advance", 5),
		ChanceCard("advance", 40),
		ChanceCard("pay", 50), # pay each player 50
		ChanceCard("cash", 150),
		ChanceCard("cash", 100),
	]

	def __init__(self):
		# Generate an order of chance cards
		self.pile = random.sample(range(0, len(self.CARDS)),
			len(self.CARDS))

	def pullCard(self):
		card = self.pile[0]
		
		return card