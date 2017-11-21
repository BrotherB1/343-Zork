import random

"""Class for Chocolate Bar. Uses basic getters. Created by Luke Bassett Fall 2017"""
class Bar:
	
	def __init__(self):
		self.use = 4
		self.mult = 0

	def used(self):
		self.use = self.use - 1
		
	def getMult(self):
		self.mult = random.uniform(2.0, 2.4)
		return self.mult

	def getUse(self):
		return self.use

	def getString(self):
		return "Chocolate Bar"
