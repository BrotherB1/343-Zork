from Bar import Bar
from Straw import Straw
from Bomb import Bomb
from Kiss import Kiss
import random

"""This is the class for the player. Keeps track of our youth and vitality!"""
class Player:
	
	"""Starts by making starting stats as well as a beginning random inventory"""
	def __init__(self):
		self.health = random.randint(200, 300)
		self.attack = random.randint(10,20)
		self.inventory = []
		for x in range(0,10):
			self.bar = Bar()
			self.straw = Straw()
			self.bomb = Bomb()
			self.kiss = Kiss()
			self.inventory = self.inventory + random.sample([self.bomb,self.kiss, self.straw,self.bar], 1)
		
	#prints current stats
	def status(self):
		print("[HP:{} ATK:{}]".format(self.health, self.attack))

	#prints our warrioresque inventory
	def Inventory(self):
		self.sInventory = []
		for x in range(0,10):
			self.sInventory.append(self.inventory[x].getString())
		print("Your Inventory is: ")
		print(self.sInventory)
		print( " ")

	#checks if an item is present during attack phase
	def checkInventory(self, item):
		for x in range(0,10):
			if item == self.inventory[x].getString():
				return True
		return False

	#retrieves attack multiplier for weapons and decreases uses left
	def getMult(self, item):
		for x in range(0,10):
			if item == self.inventory[x].getString():
				self.inventory[x].used()
				y = self.inventory[x].getMult()
				if self.inventory[x].getUse() <= 0:
					self.inventory[x] = self.kiss
				return y

	#getters for player attack as well as total attack with weapon multiplier
	def getAttack(self):
		return self.attack

	def getHealth(self):
		return self.health
			
	def atkBomb(self):
		return self.attack * self.getMult("Nerd Bomb")
	def atkBar(self):
		return self.attack * self.getMult("Chocolate Bar")
	 
	def atkStraw(self):
		return self.attack * self.getMult("Sour Straw")
	
	def atkKiss(self):
		return self.attack 

	def attacked(self, hit):
		self.health -= hit
	
	#After a battle, will generate items based on how many people were saved
	def generateItems(self, num):
		for x in range (0, 10):
			if self.inventory[x] == self.kiss:
				self.inventory.remove(self.kiss)
				self.inventory = self.inventory + random.sample([self.bomb,self.kiss, self.straw], 1)
