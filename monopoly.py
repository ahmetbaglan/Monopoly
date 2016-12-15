#!/usr/bin/python

from game import *
from player import *
from results import *
import sys
import time

r = Results("results.csv")
print "Starting simulation"
count = 100000/2
start = time.time()

for i in range(0, count):
	g = Game([Player()], 100)
	g.run()
	r.addHitResults(g.board.hits)

	now = time.time()
	speed = i / (now - start)

	if (i + 1) % (count / 1000) == 0:
		sys.stdout.write("\rCurrently at %f percent done, %f games/second" % (i / float(count) * 100, speed))
		sys.stdout.flush()

print "\nDone!"

r.write()