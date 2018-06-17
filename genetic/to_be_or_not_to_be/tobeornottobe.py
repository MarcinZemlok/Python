# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 14:14:17 2018

@brief This script creates random population and evolves it to reach predefined sentense.

@author: MarcinZemlok
"""

import math as m
from string import letters
letters += " ,.;?!1234567890-_/*"
import random

def fit(_g):
	"""Computes fit value for given individual
		
		Parameters:
		_g - gen of individual for which fit value will be computed
		
		Returns:
		Function returns a fit value for given individual
	"""
	score = 0.0
	deltaLength = m.fabs(len(patern) - len(_g))
	iterations = len(_g) if len(patern)>len(_g) else len(patern)
	
	if debug:
		print "----------"
		print "Analizing: ", _g
		print "Will be made", iterations, "iterations"
		print "Individual length is:", len(_g)
	
	if deltaLength < len(patern):
		score = (len(patern) - deltaLength)
	
	for i in range(iterations):
		if _g[i] == patern[i]:
			score += 1
			if debug:
				print "Correct in", i, "pos:", _g[i], "==", patern[i]
		elif patern.lower()[i] == _g.lower()[i]:
			score += 0.5
			if debug:
				print "Allmost correct in", i, "pos:", _g[i], "==", patern[i]
	if debug:
		print "Score:", score
	return score

def fitPopulation(_pop):
	"""Computes fit values for given population
		
		Parameters:
		_pop - population for which fit values will be computed
		
		Returns:
		Function returns corresponding fit vaues for given population
	"""
	fitCounts = []
	for ind in _pop:
		fitCounts.append(fit(ind))
	return fitCounts

def sortRanking(_pop, _fit):
	"""Sorts population and fit values due to fit values
		
		Parameters:
		_pop - population to be sorted
		_fit - fit values related to population
		
		Returns:
		Function returns a tuple of sorted fit values and population
	"""
	return zip(*sorted(zip(_fit,_pop),reverse=True))

def compPropability(_poplen, _lr=0.0):
	"""Computes propability based on individuals ranking plase
		
		Parameters:
		_poplen - lenght of population
		_lr - propability of picking worst individual
		
		Returns:
		Function returns list of propability values
	"""
	ranksum = (1.0+_poplen)/2.0
	k = (1.0-_lr)/(_poplen-ranksum)
	sum = 0.0
	tmp = []
	for i in range(_poplen):
		tmp.append(_lr+k*(1.0-(float(i+1)/_poplen)))
		sum += tmp[-1]
	if debug:
		print "----------\nComputing propability\nk =", k
		print "Checksum =", sum
		print "Computed propability:"
		for i,p in enumerate(tmp):
			print i+1,"\t|",p
	return tmp

def pickPairs(_pop, _prop, _numpairs=None):
	"""Picks pairs of individuals from gicen population which will be crossover
	
		Selection is based on given propability values
		
		Parameters:
		_pop - population wrom which pick will be made, if length is not even then will be picked length-1 individuals
		_prop - propability values for population, should sum to 1
		
		Returns:
			Function returns selected individuals as a list
	"""
	if _numpairs == None:
		_numpairs = len(_pop)
	if _numpairs % 2 != 0:
		_numpairs -= 1
	tmp = []
	for i in range(_numpairs):
		trh = 0
		for j,p in enumerate(_prop):
			trh+=p
			if random.random() < trh:
				tmp.append(_pop[j])
				break
	if debug:
		print "----------\nResult of pairs rand:"
		for i,p in enumerate(tmp):
			print i+1,"\t|",p
	return tmp

def crosover(_pairs):
	"""Provides one point crossover over given list of idividuals
	
		Every odd individual is crossed with even one that comes after
		
		Parameters:
		_pairs - individuals to be cross (length must be even)
		
		Returns:
		Funcion returns new population based created from crosover
	"""
	if debug:
		print "----------\nChildren:"
	tmp = []
	i=0
	while i < len(_pairs):
		in1 = _pairs[i]
		in2 = _pairs[i+1]
		if (len(in2)-len(in1)/2) >= 0:
			tmp.append(in1[:len(in1)/2]+in2[len(in2)-len(in1)/2:])
		else:
			tmp.append(in1[:len(in1)/2]+in2[len(in2):])
		if (len(in1)-len(in2)/2) >= 0:
			tmp.append(in2[:len(in2)/2]+in1[len(in1)-len(in2)/2:])
		else:
			tmp.append(in2[:len(in2)/2]+in1[len(in1)/2:])
		i+=2
		if debug:
			print tmp[-2], len(tmp[-2]), "\t|\t", tmp[-1], len(tmp[-1])
	return tmp

def mutate(_pop, _mr=0.001):
	"""Mutates population with given mutation rate
		
		Parameters:
		_pop - population to be mutate vith given mutation rate
		_mr - mutation rate, default 0.1%
		
		Returns:
		Funcion returns mutated population as a list
	"""
	if debug:
		print "----------\nMutation:"
	tmp = []
	for i,p in enumerate(_pop):
		p=list(p)
		for j,l in enumerate(p):
			if random.random() < _mr:
				p[j] = random.choice(letters)
			if random.random() < _mr:
				p[j] = p[j].lower()
			if random.random() < _mr:
				p[j] = p[j].upper()
		p=''.join(p)
		if(random.random() < _mr):
			p=p[:-1]
		if(random.random() < _mr):
			p+=p[-1]
		tmp.append(p)
		if debug and _pop[i] != p:
			print _pop[i], "\t->\t", p
	return tmp

def generateStart(_count):
	"""This class generates random start population
	
		Parameters:
		_count - number of individuals in population
		
		Returns:
		Function returns generated population as a list
	"""
	pop = []
	for i in range(_count):
		tmp = ""
		for i in range(random.randint(1,41)):
			tmp += random.choice(letters)
		pop.append(tmp)
	return pop

"""You can change this parameters"""
## Sentence that is the target, should be between 5 and 40 characters
patern = "To be or not to be..."
## Length of population
poplen = 25
## Maximum number of iteration before loging out data
log = 10000
## True if all steps should be loged out
debug = False

"""Do not change anything under thi line if You dont know what You are doing"""
## Holds keyboard input
key = ""
## Iteration counter
it = 0
## Best individual and its fit value
best = False
## List of individuals in population
popul = generateStart(poplen)
## Propability values for population
prop = compPropability(poplen)
while key == "":

	fitVal = fitPopulation(popul)
	fitVal, popul = sortRanking(popul, fitVal)
	if best:
		list(fitVal).append(best[0])
		list(popul).append(best[1])
	fitVal, popul = sortRanking(popul, fitVal)
	best = [fitVal[0], popul[0]]
	
	if debug or (fitVal[0] == (len(patern)*2)) or ((it % log == 0)and(it>0)):
		print "----------\nFit value for iteration:", it
		for i,p in enumerate(popul):
			print i+1, fitVal[i],p
			if i >= 5:
				break
		if (fitVal[0] == (len(patern)*2)):
			print('\n\x1b[0;32;1m' + str(best[0]) + "\t" + str(best[1]) + '\x1b[0m')
			break
		key = raw_input("Enter - continue\nq->Enter - leave\n")
	
	pairs = pickPairs(popul, prop)
	popul = crosover(pairs)
	popul = mutate(popul, 0.01)
	it += 1
