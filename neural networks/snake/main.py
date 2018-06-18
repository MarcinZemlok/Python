# -*- coding: utf-8 -*-

from screen import Screen
from snake import (Snake, Fruit)
import time

sc = Screen([10,20])
sn = Snake([5,20])
sn.setDir([0,0,0,1])
fruit = Fruit(10,20)
print fruit.pos

while sn.valid:
	sc = sn.update(sc)
	sc = fruit.show(sc)
	print sc
	print sn.valid
	if sn.pos == fruit.pos:
		sn.addSegment()
		fruit.randomize(10,20)
	time.sleep(0.25)