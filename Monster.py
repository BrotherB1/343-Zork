from Observable import Observable

"""Monster class to control the monserts and people alike! Created by Luke Bassett with help from Brendan Cronan Fall 2017"""
class Monster(Observable):

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
