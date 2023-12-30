"""
Programming Concepts 9 - Functions
This assignment is worth 60 points. Write your answers in the spaces provided.
"""

#1: Write a line of code that imports the "random" module and assigns it the name rand. (2)
import random as rand 

#2: Write a function called printBackwards that accepts a string and prints it backwards. (4)

def printBackwards(inputString):
    reversedString = inputString[::-1]
    print(reversedString)

printBackwards("Hello")

#3: Write a function called fourFunctionCalc that accepts two integers and returns their sum, difference, product, and quotient as a dictionary. (4)

def fourFunctionCalc(number1, number2):
    result = {
        "sum": number1 + number2,
        "difference": number1 - number2,
        "product": number1 * number2,
        "quotient": number1 / number2
    }
    return result

print(fourFunctionCalc(5,3))

#4: Write a function called roll100 that returns a random number between 1 and 100. (4)
def roll100():
    return rand.randint(1, 100)

print(roll100())

#5: Write a function called tetration that accepts a number and returns it raised to the power of itself.
#That is, if x=5, the function should return 3125. (4)

def tetration(a):
    result = a ** a 
    return result

print(tetration(10))

#6: Write a function called wheelSpin that accepts a list of options and returns a random selection. (4)

def wheelSpin(options):
    return rand.choice(options)

options = ["Vanilla", "Chocolate", "Strawberry", "Cookies and Cream", "Mint"]
print(wheelSpin(["Vanilla", "Chocolate", "Strawberry", "Cookies and Cream", "Mint"]))

#7: Write a function called isPalindrome that accepts a string and returns True if the string is a palindrome, False if it isn't. (6)
#Tip: You should cast the input to lowercase before checking it.

def isPalindrome(a):
    a = a.lower()
    return a == a[::-1]

print(isPalindrome("appa"))
print(isPalindrome("Pepperoni"))

#8: Write a function called countWords that accepts a string containing a large block of text.
#Remove any punctuation from the string using the provided string of punctuation marks.
#Use the split and lower functions to break the string into a list of individual words.
#Create an empty dictionary called repeats.
#For each word in our block of text, if it exists as a key in repeats, increase its value by 1. If not, add the key with a value of 1. (32)
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def countWords(sentence):

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    sentence = ''.join(char for char in sentence if char not in punctuations) 

    words = sentence.lower().split()

    repeats = {}

    for word in words:
        if word in repeats:
            repeats[word] += 1
        else:
            repeats[word] = 1

    return repeats       

print(countWords("We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defense, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America."))

