"""
Programming Concepts 6 – Loops
This assignment is worth 20 points. Write your answers in the spaces provided.
"""

#1: What is the output of the following code? (3)
for i in range(1,10):
    print(i**2, end=" ")
# Output is: 1 4 9 16 25 36 49 64 81 
print()

#2: What is the output of the following code? (4)
x = 1
while x < 10:
    if x%2 == 0:
        print(x**3, end=" ")
    else:
        print(x*3, end=" ")
    x += 1
# Output is: 3 8 9 64 15 216 21 512 27
print()

#3: What is the output of the following code? (3)
grades = [89, 92, 34, 68]
for grade in grades:
    if grade >= 70:
        print("Pass", end=" ")
    else:
        print("Fail", end=" ")
# Output is: Pass Pass Fail Fail
print()

#4: Write a while loop to determine the factorial of a number entered by the user. (5)
number =int(input("Enter a number please "))
factorial = 1
while number > 0:
    factorial = factorial * number
    number -=1
print("Factorial is = ", factorial)
print()

#5: Write a for loop to iterate over a list of grades. Each grade should be rounded up to the next multiple of 10. (5)
#DO NOT use conditionals.
grades = [72, 68, 85, 92, 56]
for grade in range(len(grades)):
    grades[grade]= ((grades[grade] + 9)// 10) * 10
print(grades)
