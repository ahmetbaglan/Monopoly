#!/usr/bin/python

from game import *
from player import *
from results import *
import sys
import time

# Init results class for saving results
r = Results("results.csv")

# Print start message
print "Starting simulation"

# Set simluation variables
count = 100000/2
start = time.time()

# Go through set amount of simulations
for i in range(0, count):
	# Start a new game, run it and save the results
	g = Game([Player()], 100)
	g.run()
	r.addHitResults(g.board.hits)

	# Calculate the amount of simulations per second
	now = time.time()
	speed = i / (now - start)

	# Display the progress every 1/1000 of the way to begin finished
	if (i + 1) % (count / 1000) == 0:
		sys.stdout.write("\rCurrently at %f percent done, %f games/second" % (i / float(count) * 100, speed))
		sys.stdout.flush()

# Print that the simulation is finished
print "\nDone!"

# Same the results to a csv
r.write()