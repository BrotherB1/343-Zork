from Monster import Monster
import random

"""These are so overrated... Zombie class to hold the information of the undead! Created by Luke Bassett Fall 2017"""
class Zombie(Monster):
	
	def __init__(self):
		self.hp = random.randint(50,100)
		self.atk = random.randint(0, 10)
		self.name = "Zombie"
		self.dead = False
		self.observers = []	

	"""handles exception of sour straw which causes extra damage"""
	def attacked(self, hit, item):
		if item == "Sour Straw" or item == "sour straw":
			self.hp = self.hp - 2*hit
		else:
			self.hp = self.hp - hit
		if self.hp <= 0:
			self.die()

