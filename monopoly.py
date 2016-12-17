#!/usr/bin/python

from game import *
from player import *
from results import *
import sys
import time

# Init results class for saving results
r = Results("results")

# Print start message
print "Starting simulation"

# Set simluation variables
count = 50000
players = 1
rounds = 100
start = time.time()

# Go through set amount of simulations
for i in range(0, count):
	# Start a new game, run it and save the results
	g = Game([Player()] * players, rounds)
	g.run()
	r.addHitResults(g.board.hits)

	# Calculate the amount of simulations per second
	now = time.time()
	speed = i / (now - start)

	# Display the progress every 1/1000 of the way to begin finished
	if (i + 1) % (count / 1000) == 0:
		sys.stdout.write("\rCurrently at %s%% done, %s games/second" %
			(str(round((i + 1) / float(count) * 100, 1)), str(round(speed, 1))))
		sys.stdout.flush()

# Print that the simulation is finished
print "\nDone!"

# Same the results to a csv
r.writeHTML(count, players, rounds)