"""
Programming Concepts 7 - Lists
This assignment is worth 40 points. Write your answers in the spaces provided.
"""

#1: What is the output of the following print statements given this list? (4)
names = ["Scarlet", "Jazmine", "Matthew", "Miles", "Savannah",
         "Tucker", "Jamie", "Alex", "Donovin", "Mariah"]

print(names[1]) # Output: Jazmine
print(names[-1]) # Output: Mariah
print(names[0:-1:2]) # Output: ['Scarlet', 'Matthew', 'Savannah', 'Jamie', 'Donovin']
print(len(names)) # Output: 10

#2: Write a line of code that adds your name to the end of the above list. (4)
names.append("Mert")
print(names)

#3: Write a line of code that removes your instructor's name from the list. (4)
names.pop(0)
print(names)

#4: Loop through the above list and print each name in all caps. (4)
for name in names:
    print(name.upper())

#5: Add up the number of letters in each name in the above list. Print the result. (4)
#This can be done with a single line of code, but a loop is acceptible.
totalLetterNumber = sum(len(name)for name in names)
print(totalLetterNumber)

#6: Write a Python script that repeatedly asks the user to input names, or enter "q" to finish.
#After they have finished, the script should print the names in a presentable fashion, followed by
#the length of the list total number of characters used excluding spaces, again in a presentable fashion. (20)
newNames = []
while True:
    newName = input("Write a name to print. If you want to finish this, please type 'q'. ")
    # if name == 'q': (actually at the first I typed this but it does not contain uppercase Q so I typed other one to contain both.)
    if newName.lower() == 'q':
        break

    newNames.append(newName)

print("Entered names are: ")
for newName in newNames:
        print(newName)

totalNumberOfCharacters = sum(len(newName.replace(" ", "")) for newName in newNames)
print (f"Total number of characters without spaces: {totalNumberOfCharacters}")


