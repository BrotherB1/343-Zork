#!/usr/bin/env python
from Neighborhood import Neighborhood
from Player import Player

"""The Game class that controls all movement and actions taken. Created by Luke Bassett with help from Brendan Cronan and Python Documentation https://docs.python.org/3/ Fall 2017"""
class Game():

	player = Player()
	Hood = Neighborhood()
	def __init__(self):
		first = 1
		self.player = Player()
		self.xPos = 1
		self.yPos = 0
		self.Hood = Neighborhood()
		self.won = False
		
	"""Method that controls all movement as well as miscellaneous commands while in the neighborhood"""
	def move(self):
		loop = 4
		while loop == 4:
			first = raw_input("Where would you like to go?\n")
	
			if first == "north" or first == "North":
				if self.yPos == 14:
					print("You can't go any farther North!")
				else:
					self.yPos +=1
			elif first == "east" or first == "East":
				if self.xPos == 9:
					print("You can't go any farther East!")
				else:
					self.xPos +=1
			elif first == "south" or first == "South":
				if self.yPos == 0:
					print("You can't go any further South!")
				else:
					self.yPos -=1
			elif first == "west" or first == "West":
				if self.xPos == 0:
					print("You can't go any further West!")
				else:
					self.xPos -=1

			elif first == "help":
				print("1. Type north, south, east or west to move (first letters can be either case) and the game will tell you what position you are (on a house, in a yard, or on the stree(look both ways before you take a step!))")
				print("2. If you decide you would like to start a new game (becasue we all know you want to always play this) then type 'quit' to exit the current game (to hop right back in after!)")
				print("3. Type 'info' if you want to know your current health/attack, inventory, and number of monsters left")

			elif first == "quit":
				self.end()

			elif first == "info":
				self.player.status()
				self.player.Inventory()
				print("Total number of Monsters still in the Neighborhood: ")
				i =self.Hood.getMonsterNumber()
				print(i)
			else:
				print("Please enter a valid direction")
			pos = self.Hood.getPos(self.xPos, self.yPos)

			if pos == "s" or pos == "y" or pos == "H":
				pass

			else: 
				second = raw_input("Would you like to enter?\n")
				if second == "yes" or second == "Yes":
					self.attackPhase(self.xPos, self.yPos)
				else:
					print("\n")
				
	"""Method that ends the game, win or lose"""
	def end(self):
		if self.won == True:
			print("Congradulations! You've won the game!")
		else:
			print("Too bad, you lost. Come back and try again!")
		import os
		quit(1)

	"""Method that controls the attack phase inside of a house. Parameters xPos and yPos are the positions to grab the house object ffrom the neighborhood"""
	def attackPhase(self, xPos, yPos):
		print("You've entered the house! Your current stats are:")
		#self.player.status()
		#self.player.Inventory()
		self.loop = 5
		#self.Hood.getHouse(xPos,yPos).getMonsters()

		while self.loop == 5:
			self.player.status()
			self.player.Inventory()
			self.loop = 5
			self.Hood.getHouse(xPos,yPos).getMonsters()	
			 
			atk = 1
			self.item = raw_input("What would you like to attack with?\n")

			if self.item == "Hershey Kiss" or self.item == "hershey kiss":
				if self.player.checkInventory("Hershey Kiss"):
					atk = self.player.atkKiss()
					self.loop = 6
				else:
					print("None of that item are in your bag!")
			elif self.item == "Chocolate Bar" or self.item == "chocolate bar":
				if self.player.checkInventory("Chocolate Bar"):
					atk = self.player.atkBar()
					self.loop = 6
				else:
					print("None of that item are in your bag!")

			elif self.item == "sour straw" or self.item == "Sour Straw":
				if self.player.checkInventory("Sour Straw"):
					atk = self.player.atkStraw()
					self.loop = 6
				else:
					print("None of that item are in your bag!")

			elif self.item == "Nerd Bomb" or self.item == "nerd bomb":
				if self.player.checkInventory("Nerd Bomb"):	
					atk = self.player.atkBomb()
					self.loop = 6
				else:
					print("None of that item are in your bag!")

			elif self.item == "info":
				print("\n")
				self.Hood.getHouse(xPos,yPos).getMonsters()
				self.player.status()
				self.player.Inventory()

			elif self.item == "run":
				print("You ran out of the house!")
				self.loop = 4

			elif self.item == "help":
				print("1. Type Chocolate Bar, Hershey Kiss, Nerd Bomb, or Sour Straw to attack (first letters can be either case)")
				print("2. If you feel you can't take on this house currently, type 'run' and you will be able to escape back into the neighborhood")
				print("3. Type 'info' if you want to know your current health/attack, inventory, and monsters types left in the house")
			else:
				print("please input a valid item")
			print("\n")
			while self.loop == 6:
				
				self.Hood.getHouse(xPos,yPos).attacked(atk, self.item)
				self.mAtk = self.Hood.getHouse(xPos,yPos).attack()	
				
				self.player.attacked(self.mAtk)
				self.loop = 5
				if self.player.getHealth() <= 0:
					self.won = False
					self.end()
				if self.Hood.getHouse(xPos,yPos).clear():
					print("You cleared the house! The people are thankful and have given you more items!")
					i = self.Hood.getHouse(xPos,yPos).getNumMonsters()
					if(self.Hood.getMonsterNumber() <= 0):
						self.won = True
						self.end()
					self.player.generateItems(i)
					self.Hood.setLocation(xPos, yPos)
					self.loop = 7
				
print("Welcome to your hometown of Zork! You've woken up this morning only to discover the neighborhood has been overrun with monsters! You still have a mix of Hershey Kisses, Chocolate Bars, Sour Straws and Nerd Bombs to help you defend your home town. You currently stand in front of a house. Type 'west' to approach the house! If you ever feel lost, type 'help' and a list of instructions will appear to help guide you!")

g = Game()
g.move()
