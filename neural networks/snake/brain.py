# -*- coding: utf-8 -*-
import numpy as np

class Brain:
	def __init__(self, dim):
		self.alfa = 1.0
		self.gamma = 1.0
		self.w1 = np.array(np.random.rand(dim,50), np.float64)
		self.w2 = np.array(np.random.rand(50,1), np.float64)
		
	def __str__(self):
		return "W1:\n"+str(self.w1.shape)+"\nW2\n"+str(self.w2.shape)
	
	def predict(self, _indata, act):
		indata = np.array(np.zeros(148))
		for i,d in enumerate(np.array(_indata).flatten()):
			if d == '-':
				indata[i] = 0.0
			elif d == '|':
				indata[i] = 0.2
			elif d == ' ':
				indata[i] = 0.4
			elif d == 'o':
				indata[i] = 0.6
			elif d == '#':
				indata[i] = 0.8
			elif d == '@':
				indata[i] = 1.0
		indata[-4:] = act
		hidden = np.matmul(indata, self.w1)
		hidden = np.tanh(hidden)
		out = np.matmul(hidden, self.w2)
		out = np.tanh(out)
		return out
	
	def processActions(self, arena, actions):
		scores = []
		for action in actions:
			scores.append(self.predict(arena, action))
		scores = np.array(scores)
		move = [0,0,0,0]
		move[scores.argmax()] = 1
		return move, scores.max()
	
	def computeCorrected(self, arena, predicted, real):
		move, maks = self.processActions(arena, [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]])
		return self.alfa*(real + self.gamma*maks - predicted)
		