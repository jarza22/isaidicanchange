"""
Programming Concepts 8 - Dictionaries
This assignment is worth 40 points. Write your answers in the spaces provided.
This assignment will touch on elements of our final project.
"""

#1: Given the following dictionary, write the output of the following print calls? (10)
attributes = {"strength": 8,
              "perception": 5,
              "endurance": 7,
              "charisma": 1,
              "intelligence": 9,
              "agility": 8,
              "luck": 2}

print(attributes["intelligence"])
for key in attributes:
    print(key, end=" ")
print("\n" + str(sum(attributes.values())))

#2: Use the += operator to add one point to any of the listed attributes. (5)

#3: The character with the above attributes is suffering from radiation poisoning.
#Because of this, they take a -2 endurance debuff. Adjust the dictionary accordingly. (5)

#4: Create some new attributes as follows. (20)
#name - Prompt the user to input this.
#hitpoints - Base value of 100, 15 additional points per point of endurance.
#actionpoints - Base value of 45, 5 additional points per point of agility.
#carryweight - Base value of 150, 10 additional points per point of strength.
#critchance - One point per point of luck.
#Print the dictionary in a presentable fashion to verify the changes made.