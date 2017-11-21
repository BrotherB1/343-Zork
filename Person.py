from Monster import Monster

"""Yay Humans! Person class to help the player"""
class Person(Monster):
	
	def __init__(self):
		self.hp = 1
		#wanted to make the health a bit more resonable and interesting
		self.atk = -5
		self.name = "Person"
		self.dead = False
		self.observers = []
	
	"""Doesn't do anything, but allows for a clean for loop without additionalif statements"""
	def attacked(self, hit, item):
		pass
	

