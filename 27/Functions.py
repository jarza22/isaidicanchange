#Factorial
#Inputs - x (an integer)
#Output - result (an integer)
#Iterative
def factorial(x):
    result = 1
    while x > 1:
        result *= x
        x -= 1
    return result

#Recursive
def recursiveFactorial(x):
    if x == 1:
        return x
    else:
        return x*recursiveFactorial(x-1)

#Integer Sum
#Inputs - numbers (a list)
#Output - result (an integer)
#Constraints - Break if a non-integer is found.
def integerSum(numbers):
    result = 0
    for number in numbers:
        if type(number) is not int:
            break
        else:
            result += number
    return result

#Mean and Range
#Inputs - numbers (a list)
#Output - data (a dictionary)
#Constraints - Eliminate non-integer values from numbers.
def meanAndRange(numbers):
    onlyIntegers = [number for number in numbers if type(number) is int]
    data = {}
    highest = max(onlyIntegers)
    lowest = min(onlyIntegers)
    integerRange = highest-lowest
    mean = sum(onlyIntegers)/len(onlyIntegers)
    data["mean"] = mean
    data["range"] = integerRange
    return data

#Pythagorean Theorem
#Inputs - a (a number), b (a number)
#Output - c (a number)
#Constraints - Print an error if a non-number is given.
def pythagorean(a, b):
    sumOfSquares = (a**2)+(b**2)
    c = sumOfSquares**(1/2)
    return c

#Testing
print(factorial(5))
print(recursiveFactorial(5))
print(factorial(10))
print(recursiveFactorial(10))

list1 = [1,3,8,22,35,68]
list2 = [5,3,17,True,"R",100]
print(integerSum(list1))
print(integerSum(list2))

print(meanAndRange(list1))
print(meanAndRange(list2))

print(pythagorean(3,4))
print(pythagorean(6,12))