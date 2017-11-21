from House import House
from Observer import Observer

"""Class for the Neighborhood that will create the same object each time"""
class Neighborhood(Observer):
	hood = [[0 for y in range(14)] for x in range(10)]


	#This method constructs the neighborhood in a specific way, that way the game will be the same each time.
	def __init__(self):
		self.hood = [[0 for y in range(15)] for x in range(10)]
		for a in range(0, 10):
			
			for b in range(0,15):
				
				if a == 3 or a == 6:
					if b == 11 or b == 12 or b == 13:
						self.hood[a][b] = "s"
						continue
						
					if b % 2 == 1:
						self.hood[a][b] = "y"
						continue
					else:
						self.hood[a][b] = House()
					self.hood[3][14] = "y"
				elif a == 0 or a == 9:
					if b % 2 == 1:
						self.hood[a][b] = "y"
					else:
						self.hood[a][b] = House()
				elif a== 1 or a == 2 or a == 7 or a == 8:
					self.hood[a][b] = "s"
					if b == 14 and (a == 1 or a == 8):
						self.hood[a][b] = "y"
					elif (a == 2 or a == 7) and b == 14:
				
						self.hood[a][b] = House()
				else:
				
					self.hood[a][b] = "y"
					self.hood[a][11] = "s" 
					self.hood[a][12] = "s" 
					self.hood[a][13] = "s"
					self.hood[4][14] = House()
				if isinstance(self.hood[a][b], House):
					self.hood[a][b].setObservers() 
		 
	

	#gets the current position
	def getPos(self, x, y):
		if self.hood[x][y] == "s":
			print("You're standing in a street\n")
			return "s"
		elif self.hood[x][y] == "y":
			print("You're standing in someone's yard!\n")
			return "y"
		elif self.hood[x][y] == "H":
			print("You've already cleared this house!\n")
			return "H"
		else:
			print("You're by a house.\n")
		
	#sets the cleared house to house you can no longer go into
	def setLocation(self, xPos, yPos):
		self.hood[xPos][yPos] = "H"

	#gets the house object for the Game class
	def getHouse(self, xPos, yPos):
		return self.hood[xPos][yPos]

	#updates the number of monsters
	def update(self, monster):
		self.monsterNum = self.monsterNum - 1
		if (self.monsterNum == 0):
			pass

