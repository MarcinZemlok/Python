# -*- coding: utf-8 -*-

from screen import Screen
from snake import (Snake, Fruit)
from brain import Brain
import time
#import numpy as np

sc = Screen([10,10])
sn = Snake([5,5])
sn.setDir([0,0,0,1])
fruit = Fruit(10,10)
b = Brain(12*12+4)

while sn.valid:
	reward = 0.0
	move, maks = b.processActions(sc.arena, [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]])
	sn.setDir(move)
	sc = sn.update(sc)
	sc = fruit.show(sc)
	print sc
	print "Predicted reward:",maks
	if not sn.valid:
		reward = -1.0
	if sn.pos == fruit.pos:
		sn.addSegment()
		fruit.randomize(10,20)
		reward = 1.0
	err = b.computeCorrected(sc.arena, maks, reward)
	print "Reward error:",err
	time.sleep(0.25)