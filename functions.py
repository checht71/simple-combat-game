from random import randint
from classes import EnemyEntity
#Enemy1 = EnemyEntity("Enemy 1", 100, 100, 10, 1.05, 10, 5, 0, 0)
#from matplotlib import pyplot as plt
global enemyNumber
enemyNumber = 0
#array=[]

def newEnemy(self): #Uses the same object, enters new values
   global enemyNumber
   enemyNumber += 1
   difficulty = round(randint(1, 5) * enemyNumber/10) + 1 + round(enemyNumber/10)
   self.name = "Enemy " + str(enemyNumber)
   self.hp = round(60 * difficulty)
   self.maxhp = self.hp
   self.attack = 10 * difficulty
   self.defense = 1 + (0.1 * difficulty)
   self.shield = 5 * difficulty
   self.shieldincrease = 5 + 2 * difficulty
   self.lootdrop = 5 * difficulty
   self.hpdrop = round(0.1 * difficulty)
   self.shielddrop = round(0.3 * difficulty)
   self.xp = difficulty * 10
   return self.hp



"""
for i in range(30):
    back = newEnemy(Enemy1)
    array.append(back)

plt.plot(array)
"""
