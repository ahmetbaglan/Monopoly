from random import randint

def diceThrow():
	dice1 = randint(1, 6)
	dice2 = randint(1, 6)

	# Return total num of eyes, and whether or not the dices were equal
	return [dice1 + dice2, dice1 == dice2]