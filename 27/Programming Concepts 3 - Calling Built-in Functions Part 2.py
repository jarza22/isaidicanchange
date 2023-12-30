"""
Programming Concepts 3 – Calling Built-in Functions (2 of 2)
This assignment is worth 20 points. Write your answers in the spaces provided.
"""

#1: Write code that will cast an integer to a string, then print it. (4)
number = 5
print("#" + str(number))

#2: Write code that will prompt the user to enter their age, then echo it back to them. (4)
#Hint: There is no need to cast to a string. 
age = input("How old are you? ")
print("Your age is" , age)

#3: Write code that prompts the user for their first name. Append to this an input for their last name. (4)
firstname = input("What is your name? ")
surname= input("What is your surname? ")
fullname = firstname + " " + surname
print(fullname)

#4: Write code that prints string1 in all uppercase letters and string2 in all lowercase letters. (4)
string1 = "jsu"
string2 = "Python"
print(string1.upper())
print(string2.lower())


#5: WRite code that replaces the underscores in a string with spaces. (4)
textToModify = "All_these_squares_make_a_circle."
newText = textToModify.replace("_"," ")
print(newText)

