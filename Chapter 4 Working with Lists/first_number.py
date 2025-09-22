#Chapter 4-3: Making Numerical Lists
#-----------------------------------------------------Using Range Funciton--------------------------------------------------------
#Python range() function makes it easy to generate a series of numbers. 

for value in range(1,5):
    print(value)
#output: 
    #1
    #2
    #3
    #4
#Althought the code looks like it should print the numbers from 1 to 5, it does not print 5
#In this example, range() print only the numbers 1 through 4.  
#This is another result of hte off by one behavior you'll see often in programming languages. 
print("Prints the value in range 1 through 5")
for value in range(1,6):
    print(value)
#range() -> pass only one argument and it well start the sequence of numbers at 0.
#for example, range(6) would return the numbers from 0 through 5
print("Range with only one argument passed")
for value in range(6):
    print(value)
#-----------------------------------------------------Using range() to make a list of numbers--------------------------------------------------------
numbers = list(range(1,6))
print(numbers)
#-----------------------------------------------------Printing Even numbers--------------------------------------------------------
#Use range() function to tell Python to skip numbers in a given range. If you pass a third argument to range(start, end, step size), Python uses 
#that value as a step size when generating numbers
even_numbers = list(range(2,11,2))
print(even_numbers)
#With range() funciton, you can create any set of numbers.
#for example: creating a list of the first 10 square numbers (that is the square of each integer from 1 through 10)
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)
# To write the code more concisely
squares = []
for value in range (1,11):
    squares.append(value**2)
print(squares)
#-----------------------------------------------------Simple Statistics with a list of numbers-------------------------------------------------------
#Python funcitons that are helpful with lists of numbers. 
digits = []
for value in range(1,10):
    digits.append(value)
digits.append(0)
print(digits)
#finding the minimum
print(f"The minimum value in the list digts is", min(digits))
#Fidning the maximum
print(f"The maximum value in the list digits is", max(digits))
#Finding the sum of a list
print(f"The sum of the list is", sum(digits))
#-----------------------------------------------------List Comprehensions-------------------------------------------------------
#List comprehensions: allows you to generate this smae lis in just one lines of code rather than using thre or four lines of code. 
# A list comprehensions combines the for loop and the creation of new elements into one line, and automatically appends each new element. 
squares = [value ** 2 for value in range(1,11)]
print(squares)
# to use this syntax, begin with a descriptive name for the list. 
#next, open a set of square brackets and define the expression for the value you wnat to store in the new list
#then, write a for loop to generate the numbers you want to feed into the expression, and close the square bracket
