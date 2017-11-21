from Monster import Monster

"""Yay Humans! Person class to help the player. Created by Luke Bassett Fall 2017"""
class Person(Monster):
	
	def __init__(self):
		self.hp = 1
		#wanted to make the health gain a bit more reasonable and interesting
		self.atk = -5
		self.name = "Person"
		self.dead = False
		self.observers = []
	
	"""Doesn't do anything, but allows for a clean for loop without additional if statements"""
	def attacked(self, hit, item):
		pass
	

