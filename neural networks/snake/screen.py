# -*- coding: utf-8 -*-

class Screen:
	def __init__(self, dim):
		self.arena = []
		self.dimx = dim[0]+2
		self.dimy = dim[1]+2
		for x in range(self.dimx):
			self.arena.append([])
			for y in range(self.dimy):
				if x == 0 or x == (self.dimx-1):
					self.arena[x].append('-')
				elif y == 0 or y == (self.dimy-1):
					self.arena[x].append('|')
				else:
					self.arena[x].append(' ')
					
	def draw(self, ch, pos):
		if self.inValidRange(pos):
			self.arena[pos[0]][pos[1]] = ch
			return True
		return False
			
	def clear(self):
		for x in range(self.dimx):
			for y in range(self.dimy):
				if x == 0 or x == (self.dimx-1):
					self.arena[x][y] = '-'
				elif y == 0 or y == (self.dimy-1):
					self.arena[x][y] = '|'
				else:
					self.arena[x][y] = ' '
			
	def inValidRange(self, pos):
		return pos[0] > 0 and pos[0] < (self.dimx-1) and pos[1] > 0 and pos[1] < (self.dimy-1)
					
	def __str__(self):
		tmp = ""
		for i in range(self.dimx):
			for j in self.arena[i]:
				tmp += j
			tmp += '\n'
		return tmp