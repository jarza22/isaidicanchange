"""
Programming Concepts 10 - Classes
This assignment is worth 60 points. Write your answers in the spaces provided.
"""

import random

#1: Creat a class called Patient. It should have instance member variables for name, age, and department. 
#Create a __str__ method to print Patient's contents. (20)

newPatient = Patient("Angela McDonald", 35, "Endocrinology")
print(newPatient)

#2: Create a class called Case. It should have instance member variables for a case ID number,
#Patient, and summary of services being provided. Create a __str__ method to print the info. (20)

newCase = Case("1102", newPatient, "Hormone therapy")
print(newCase)

#3: Create a class called Die. This class has instance member variables for its number of sides and face-up value. Face-up value is always initially set to 1.
#Creat a method called roll that "rolls" the die, setting the face-up value to a random number from one to number of sides,
#and returns the new face-up value. Remember to add 1 to the upper bound of the randrange call. (20)

newDie = Die(20)
print(newDie.roll())