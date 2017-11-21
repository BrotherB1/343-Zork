from Ghoul import Ghoul
from Vampire import Vampire
from Werewolf import Werewolf
from Zombie import Zombie
from Monster import Monster
from Person import Person
from Observer import Observer
from Observable import Observable
import random

"""Class for our beloved houses. Created by Luke Bassett with help from Brendan Cronan and Python Documenation at https://docs.python.org/3/ Fall 2017"""
class House(Observer, Observable):
	def __init__(self):
		#List of monsters in the house
		self.mon = [] 
		self.p = Person()
		#random number of monsters in house
		self.ran = random.randint(1,10)
		self.observers = []
		#instantiates monster list
		for x in range (0,self.ran):
			self.mon = self.mon + random.sample([Ghoul(), Vampire(), Werewolf(), Zombie(), self.p], 1)
			
	
	def getNumMonsters(self):
		return self.ran
	
	#prints current monsters
	def getMonsters(self):
		names = ""
		for x in range (0,self.ran):
			
			names = names + " " + self.mon[x].getName()
		print("There are these monsters still in the room:")
		print(names + "\n")

	#if the house is attacked by an item
	def attacked(self, hit, item):
		for x in range (0 , self.ran):
			if self.mon[x] == self.p:
				pass
			else:
				self.mon[x].attacked(hit, item)
				if self.mon[x].getDead():
					self.mon[x] = Person()

	#each monster attacks
	def attack(self):
		self.total = 0
		for x in range (0 , self.ran):
			if self.mon[x] == 0:
				pass
			else:
				self.total = self.total + self.mon[x].getAttack()
		return self.total

	#returns boolean if the house is only full of people or not
	def clear(self):
		for x in range(0,self.ran):
			if not isinstance(self.mon[x], Person):
				return False
		return True

	#adds observers for the monsters in the house
	def setObservers(self):
		for x in range (0,self.ran):
			self.mon[x].add_observer(self)
	
	#update method for the monsters to communicate to the house
	def update(self, monster):
		if isinstance(monster, Monster):
			self.mon.remove(monster)
			self.mon.append(Person())
		self.update_observer(self)
