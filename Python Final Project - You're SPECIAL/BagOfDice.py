#I won't make you do this twice. Here ya go!
#No need to make any changes. Just put this in your project folder.

import random

class Die:
    def __init__(self, sides):
        self.sides = sides
        self.value = 1
    def roll(self):
        self.value = random.randrange(1,self.sides+1)
        return self.value
    
class DiceBag:
    def __init__(self, dice):
        self.dice = dice
    def singleRoll(self, selectedDie):
        for die in self.dice:
            if die.sides == selectedDie:
                return die.roll()
        return -1
    def multiRoll(self, selectedDie, numberOfRolls):
        for die in self.dice:
            if die.sides == selectedDie:
                total = 0
                for i in range(0,numberOfRolls):
                    total += die.roll()
                return total
        return -1
    
#Create some dice
d4 = Die(4)
d6 = Die(6)
d10 = Die(10)
d20 = Die(20)
d50 = Die(50)
d100 = Die(100)

#Make a list of dice.
diceList = [d4, d6, d10, d20, d50, d100]

#Make the bag.
bag1 = DiceBag(diceList)

#Alternatively, you can do all of this on one line as follows.
bag2 = DiceBag([Die(4), Die(6), Die(10), Die(20), Die(50), Die(100)])

#Roll a die once.
print(bag1.singleRoll(10))
print(bag1.singleRoll(20))
print(bag1.singleRoll(15)) #Doesn't find a matching die, returns -1.

#Roll a die multiple times.
print(bag2.multiRoll(20, 3)) #Rolls a d20 three times.
print(bag2.multiRoll(100, 35)) #Rolls a d100 35 times.
print(bag2.multiRoll(25, 6)) #Doesn't find a matching die, returns -1.