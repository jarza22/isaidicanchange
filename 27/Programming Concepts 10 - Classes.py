"""
Programming Concepts 10 - Classes
This assignment is worth 60 points. Write your answers in the spaces provided.
"""

import random

#1: Creat a class called Patient. It should have instance member variables for name, age, and department. 
#Create a __str__ method to print Patient's contents. (20)

class Patient:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def __str__(self):
        message = self.name + "\n"
        message += "Age: " + str(self.age) + "\n"
        message += "Department: " + self.department + "\n"
        return message


newPatient = Patient("Angela McDonald", 35, "Endocrinology")
print(newPatient)

#2: Create a class called Case. It should have instance member variables for a case ID number,
#Patient, and summary of services being provided. Create a __str__ method to print the info. (20)

class Case:
    def __init__(self, caseIDNumber, patient, summaryOfServices):
        self.caseIDNumber = caseIDNumber
        self.patient = patient  
        self.summaryOfServices = summaryOfServices

    def __str__(self):
        message = "Case ID number is: " + self.caseIDNumber + "\n"
        message += str(self.patient) + "\n"  
        message += "Summary of service being provided is: " + self.summaryOfServices + "\n"
        return message

newCase = Case("1102", newPatient, "Hormone therapy")
print(newCase)

#3: Create a class called Die. This class has instance member variables for its number of sides and face-up value. Face-up value is always initially set to 1.
#Creat a method called roll that "rolls" the die, setting the face-up value to a random number from one to number of sides,
#and returns the new face-up value. Remember to add 1 to the upper bound of the randrange call. (20)

class Die:
    def __init__(self, sides):
        self.sides = sides
        self.faceUp = 1

    def roll(self):
        self.faceUp = random.randrange(1, self.sides + 1)
        return self.faceUp

newDie = Die(20)
print("New face-up value of die is: " + str(newDie.roll()))
