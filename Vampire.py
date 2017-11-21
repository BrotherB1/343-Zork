from Monster import Monster
import random

"""Vampire class to help keep track of their cavities as they fight"Created by Luke Bassett Fall 2017"""
class Vampire(Monster):
	
	def __init__(self):
		self.hp = random.randint(100,200)
		self.atk = random.randint(10,20)
		self.name = "Vampire"
		self.dead = False
		self.observers = []

	"""Handles exception of chocolate since they prefer red food"""
	def attacked(self, hit, item):
		if item == "Chocolate Bar" or item == "chocolate bar":
			pass
		else:
			self.hp = self.hp - hit
		if self.hp <= 0:
			self.die()

