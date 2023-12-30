"""
In this project, you will be creating a bag of dice that will be used in your final project.
First things first, you need to import random into your file.
Use the Die class from Programming Concepts 10. There's no need to code this again.
Normally we would import this, but for simplicity, just copy/paste the Die class here.
Your DiceBag class should contain the following members and methods.
A list of Die objects.
A singleRoll method that selects a die by its number of sides via input. If the die exists, roll it and return the result. If not, return -1.
A multiRoll method that takes a number of sides to select and number of times to roll and returns the sum of the rolls. If the selected die doesn't exist, return -1.
Once you've got both your classes present and accounted for, write some test code. Create a list of Die objects.
You should have a 4, 6, 10, 20, 50, and 100 sided die. Creat a DiceBag object containing this list of dice.
Call the singleRoll and multiRoll functions a few times and print the results to verify that it works.
Take a screenshot of the terminal to show your code works.
Delete your test code, leaving only the import command and your two classes.
Compress your Python file and screenshot into a ZIP folder and submit it on Canvas.
"""

import random

class Die:
    def __init__(self, sides):
        self.sides = sides
        self.faceUp = 1

    def roll(self):
        self.faceUp = random.randrange(1, self.sides + 1)
        return self.faceUp

class DiceBag:
    def __init__(self, diceList):
        self.diceList = diceList

    def singleRoll(self, sides):
        for die in self.diceList:
            if die.sides == sides:
                return die.roll()    
        return -1
    
    def multiRoll(self, sides, numberOfRolls):
        total = 0
        for die in self.diceList:
            if die.sides == sides:
                for _ in range(numberOfRolls):
                    total += die.roll()
                return total    
        return -1    


diceList = [Die(4), Die(6), Die(10), Die(20), Die(50), Die(100)]

dice_bag = DiceBag(diceList)

result_single = dice_bag.singleRoll(6)
print(f"Single roll of 6-sided die: {result_single}")

resultante_single = dice_bag.singleRoll(12)
print(f"Single roll of 12-sided die: {resultante_single}")

result_multi = dice_bag.multiRoll(10, 3)
print(f"Sum of 3 rolls of 10-sided die: {result_multi}")

resultante_multi = dice_bag.multiRoll(7,4)
print(f"Sum of 4 rolls of 7-sided die: {resultante_multi}")






