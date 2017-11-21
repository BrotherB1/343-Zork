from Observable import Observable

"""Monster class to control the monserts and people alike!"""
class Monster(Observable):
	def __init__ (self):
		self.health = 50
		self.atk = 10
		self.name = "Monster"
		self.dead = False

	"""Getters that all of the Monsters are able to use"""
	def getHealth(self):
		return self.health

	def getAttack(self):
		return self.atk

	def getName(self):
		return self.name

	def getDead(self):
		return self.dead

	def die(self):
		self.update_observers(self)
