from Monster import Monster
import random

"""Being a Bassett, I can identify with dogs! Werewolf class to keep their powerful stats"""
class Werewolf(Monster):
	
	def __init__(self):
		self.hp = 200 
		self.atk = random.randint(0,40)
		self.name = "Werewolf"
		self.dead = False
		self.observers = []

	"""handles exeption of Chocolate and Sour items which they are strangely immune to."""
	def attacked(self, hit, item):
		if item == "Chocolate Bar" or item == "chocolate bar" or item =="sour straw" or item == "Sour Straw":
			pass
		
		else:
			self.hp = self.hp - hit
		if self.hp <= 0:
			self.die()

