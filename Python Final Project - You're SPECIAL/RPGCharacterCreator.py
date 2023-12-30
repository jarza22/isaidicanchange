"""
Python Final Project - You're SPECIAL
This Project is worth 240 points.
For this project, you are given a set of step-by-step instructions.
Write your code at the bottom of this file.
"""
from BagOfDice import Die, DiceBag
import random

"""
Let's built a character sheet generator for a Fallout-style role-playing game!
To get started, let's get all our files in the same place. You should have the following.
    1. A copy of this project file called RPGCharacterCreator.py.
    2. The main.py file that came with this project file.
    3. A copy of the completed Python Project 2 file called BagOfDice.py
IT IS ABSOLUTELY ESSENTIAL THAT THESE FILES BE IN THE SAME FOLDER AND HAVE THESE EXACT NAMES!

Above "import random", import Die and DiceBag from BagOfDice
Below these instruction, make a class called CharacterGenerator.
Copy and paste this dictionary into CharacterGenerator's __init__ method. It should be the first member listed.
self.governingSpecial = {
    "barter": "charisma",
    "energyweapons": "intelligence",
    "explosives": "perception",
    "guns": "agility",
    "lockpick": "perception",
    "medicine": "intelligence",
    "meleeweapons": "strength",
    "repair": "endurance",
    "science": "intelligence",
    "sneak": "agility",
    "speech": "charisma",
    "survival": "endurance",
    "unarmed": "strength",
}

This class must also contain the following instance member variables.
dice: A DiceBag object. This object is passed into __init__.
name: A string initialized to "Courier".
age: An integer initialized to 18.
gender: A string initialized as empty. For simplicity, this can only be M, F, or O. We'll handle that in buildCharacter below.
special: A dictionary with keys for strength, perception, endurance, charisma, intelligence, agaility, luck, all initialized to 1.
skills: A dictionary with keys that match the governingSpecial dictionary. All of their values are initialized to 5.
    Copy the keys from governingSpecial. Don't list them all again.
attributes: A dictionary with keys for hitpoints, actionpoints, carryweight, radiationresist, compassrange, and movespeed, all initialized to 1.

Next, we will create two methods as follows.

buildCharacter - This will modify our member variables as follows.
    1. Prompt the user to enter a name.
        If name is "Arnold", set strenght to 10.
        If name is "Lucky", set luck to 10.
    2. Characters are given 33 points to assign to their SPECIALs. Write code that assigns these points randomly.
        SPECIALs may NOT exceed a value of 10 at this stage.
    3. Set age to a random number from 18 to 65, inclusive at both bounds.
        If age is less than 25, increase agility by 2.
        If age is greater than or equal 25 and less than 40, increase perception and endurance by 1.
        If age is greater than or equal to 40, increase intelligence and charisma by 1.
    4. Prompt the user to enter gender as either "M", "F", or "O". Cast their input to uppercase before checking it.
        If male, increase strength and decrease agility by 1.
        If female, increase agility and decrease strength by 1.
        If other, do not change anything.
        If the user enters anything besides these three characters, they must re-enter their choice.
            Hint: Create a list of valid inputs to make error checking simpler.
    5. Increase each skill by 2 times their governing SPECIAL + half their luck rounded down.
    6. Set attributes as follows.
        hitpoints - One D100 roll for every point of endurance + one D20 for every point of luck.
        actionpoints - One D10 roll for every point of agility.
        carryweight - 100 + one D20 roll for every point of strength.
        radiationresist - One D2 roll for every point of endurance.
        compassrange - 100 + one D6 roll for every point of perception + one D4 roll for every point of intelligence.
        movespeed - Half of one D50 roll for every point of agility, rounded down to the nearest integer.

__str__ - Returns a string of the complete character build. Format it as you see fit, as long as it is readable.
    You will need for loops for this. DO NOT PRINT EVERYTHING EXPLICITLY BY NAME!

Now, open main.py and do the following.
    1. Import Die and DiceBag from BagOfDice and CharacterGenerator from RPGCharacterCreator.
    2. Create a DiceBag object with 2, 4, 6, 10, 20, 50, and 100 sided dice.
    3. Create a CharacterGenerator object; pass in your created DiceBag object.
    4. Call your CharacterGenerator's buildCharacter method.
    5. Print the object to the terminal.

Lastly, run main.py. Save a screenshot showing your code works. This step is worth the remaining 60 points not included in your class definition.
Compress this file, BagOfDice.py, main.py, and your screenshot into a ZiP folder and submit on Canvas.
"""

#CharacterGenerator class goes here!
#Each of the three required methods is worth 60 points for a total of 180.



class CharacterGenerator:
    def __init__(self, dice):
        self.governingSpecial = {
            "barter": "charisma",
            "energyweapons": "intelligence",
            "explosives": "perception",
            "guns": "agility",
            "lockpick": "perception",
            "medicine": "intelligence",
            "meleeweapons": "strength",
            "repair": "endurance",
            "science": "intelligence",
            "sneak": "agility",
            "speech": "charisma",
            "survival": "endurance",
            "unarmed": "strength",
        }
        self.dice = dice
        self.name = "Courier"
        self.age = 18
        self.gender = ""
        self.special = {
            "strength": 1,
            "perception": 1,
            "endurance": 1,
            "charisma": 1,
            "intelligence": 1,
            "agility": 1,
            "luck": 1,
        }
        self.skills = {key: 5 for key in self.governingSpecial.keys()}
        self.attributes = {
            "hitpoints": 1,
            "actionpoints": 1,
            "carryweight": 1,
            "radiationresist": 1,
            "compassrange": 1,
            "movespeed": 1,
        }

    def buildCharacter(self):
        self.name = input("Enter a name for your character: ")
        if self.name.lower() == "arnold":
            self.special['strength'] = 10
        elif self.name.lower() == "lucky":
            self.special['luck'] = 10
        
        assignablePoints = 33
        specials = list(self.special.keys())
        while assignablePoints > 0:
            stat = random.choice(specials)
            if self.special[stat] < 10 and assignablePoints > 0:
                self.special[stat] += 1
                assignablePoints -= 1
        
        
        self.age = random.randint(18, 65)
        if self.age < 25:
            self.special['agility'] += 2
        elif 25 <= self.age < 40:
            self.special['perception'] += 1
            self.special['endurance'] += 1
        elif self.age >= 40:
            self.special['intelligence'] += 1
            self.special['charisma'] += 1
        
        
        valid_genders = ['M', 'F', 'O']
        while True:
            gender_input = input("Enter your gender (M/F/O): ").upper()
            if gender_input in valid_genders:
                self.gender = gender_input
                if self.gender == 'M':
                    self.special['strength'] += 1
                    self.special['agility'] -= 1
                elif self.gender == 'F':
                    self.special['agility'] += 1
                    self.special['strength'] -= 1
                break
            else:
                print("Invalid input. Please enter M, F, or O.")

        for skill, stat in self.governingSpecial.items():
            self.skills[skill] += 2 * self.special[stat] + self.special['luck'] // 2
        
        self.attributes['hitpoints'] = sum(self.dice.multiRoll(100, self.special['endurance']) for _ in range(self.special['endurance'])) + sum(self.dice.multiRoll(20, self.special['luck']) for _ in range(self.special['luck']))
        self.attributes['actionpoints'] = self.dice.multiRoll(10, self.special['agility'])
        self.attributes['carryweight'] = 100 + sum(self.dice.multiRoll(20, self.special['strength']) for _ in range(self.special['strength']))
        self.attributes['radiationresist'] = self.dice.multiRoll(2, self.special['endurance'])
        self.attributes['compassrange'] = 100 + sum(self.dice.multiRoll(6, self.special['perception']) for _ in range(self.special['perception'])) + sum(self.dice.multiRoll(4, self.special['intelligence']) for _ in range(self.special['intelligence']))
        self.attributes['movespeed'] = sum(self.dice.multiRoll(50, self.special['agility']) for _ in range(self.special['agility'])) // 2

    def __str__(self):
        character_str = f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nSPECIAL:\n"
        for stat, value in self.special.items():
            character_str += f"{stat.capitalize()}: {value}\n"
        character_str += "SKILLS:\n"
        for skill, value in self.skills.items():
            character_str += f"{skill.capitalize()}: {value}\n"
        character_str += "ATTRIBUTES:\n"
        for attr, value in self.attributes.items():
            character_str += f"{attr.capitalize()}: {value}\n"
        return character_str
