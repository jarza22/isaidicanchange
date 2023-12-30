"""
Programming Concepts 5 – Conditional Statements
This assignment is worth 20 points. Write your answers in the spaces provided.
"""

#1: What is the output of the following code? (3)
x = (25**2)+140
if x > 1000:
    print(x*2)
else:
    print(x)
# Output is: 765

#2: What is the output of the following code? (3)
x = 2**4
y = 3**3
if x-y > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
# Output is: Zero

#What is the output of the following code? (4)
x = (13*4)+20
if x%2 == 0:
    print("x is even.")
if x%3 == 0:
    print("x is divisible by 3.")
if x%5 == 0:
    print("x is a multiple of 5.")
# Output is: x is even.
#            x is divisible by 3. (output has two rows.)

#4: Below is a list of numbers. Use the sum and len functions to find the average.
#Using conditional statements, print the following.
#If less than 60, print "F".
#If less than 70, print "D".
#If less than 80, print "C".
#If less than 90, print "B".
#If 90 or more, print "A".
#Hint: For readability, you might consider using compound conditionals. (10)
grades = [52, 98, 65, 77, 81, 32, 100, 61, 49, 92]
x = sum(grades)
y = len(grades)
average = x/y
if average < 60:
    print("F")
elif average < 70:
    print("D")
elif average < 80:  
    print("C")    
elif average < 90:  
    print("B")
else: 
    print("A")