import random

"""Class for Sour Straw. Uses basic getters."""
class Straw:
	
	def __init__(self):
		self.use = 2
		self.mult = 0

	def used(self):
		self.use = self.use - 1
		
	def getMult(self):
		self.mult = random.uniform(1.0, 1.75)
		return self.mult

	def getUse(self):
		return self.use

	def getString(self):
		return "Sour Straw"
