# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 21:06:22 2018

@author: marci
"""

import random

class Snake:
	def __init__(self, startPoint, parentDir=None):
		self.tip = True
		self.child = None
		if parentDir == None:
			self.head = True
			self.valid = True
			self.pos = [startPoint[0], startPoint[1]]
			self.dir = [1, 0]
			self.ch = '#'
			self.addSegment()
		else:
			self.head = False
			self.pos = [startPoint[0]-parentDir[0], startPoint[1]-parentDir[1]]
			self.dir = [parentDir[0], parentDir[1]]
			self.ch = 'o'
			
	def addSegment(self):
		if self.child != None:
			self.child.addSegment()
		else:
			self.child = Snake(self.pos, self.dir)
			self.tip = False
			
	def colision(self, pos):
		if self.head and not self.tip:
			return self.child.colision(self.pos)
		elif not self.tip:
			return self.child.colision(pos) or self.pos == pos
		elif self.tip:
			return self.pos == pos
		else:
			return False
			
	def show(self, screen):
		if self.head:
			screen.clear()
		if not self.tip:
			screen = self.child.show(screen)
		if self.head:
			self.valid = self.valid and screen.draw(self.ch, self.pos)
		else:
			screen.draw(self.ch, self.pos)
		return screen
	
	def setDir(self, drn):
		if drn[0] == 1: # gora
			self.dir = [-1,0]
		if drn[1] == 1: # dol
			self.dir = [1,0]
		if drn[2] == 1: # prawo
			self.dir = [0,1]
		if drn[3] == 1: # lewo
			self.dir = [0,-1]
	
	def update(self, screen):
		self.pos[0] += self.dir[0]
		self.pos[1] += self.dir[1]
		if not self.tip:
			screen = self.child.update(screen)
			self.child.dir = self.dir
		if self.head:
			self.valid = not self.colision(self.pos)
		return self.show(screen)
		
class Fruit:
	def __init__(self, ran1=1, ran2=1):
		self.pos = [random.randint(1, ran1),random.randint(1, ran2)];
		self.ch = '@'
		
	def show(self, screen):
		screen.draw(self.ch, self.pos)
		return screen
	
	def randomize(self, ran1, ran2):
		print self.pos
		self.pos[0] = random.randint(1, ran1)
		self.pos[1] = random.randint(1, ran2)
		print self.pos
