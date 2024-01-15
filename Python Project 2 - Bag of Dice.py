"""
Python Project 1 - Bag of Dice
This Project is worth 100 points.
For this project, you are given a general description of what to do.
Write your code at the bottom of this file.
"""

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