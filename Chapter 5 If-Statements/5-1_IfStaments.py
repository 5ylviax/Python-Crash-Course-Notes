#Chapter 5 If Statements 
#Programming often involves examining a set of conditions and deciding which aciton to take based on  those conditions. 
#Python's if statement allows you to examine the current state of a program and resond appropriately to that state 

#Objective: 
# write conditional statements
# create complex series of if statements 

#-----------------------------------------------------A simple Example ------------------------------------------------------
cars = ['audi', 'bmw','subaru','toyota']
for car in cars: 
    if car == 'bmw': # checks if the current value is true to the conditional statement
        print(car.upper())
    else:
        print(car.title()) #if the value is not the 'bmw' it well printed int title case 

#-----------------------------------------------------Conditional Tests ------------------------------------------------------- 
# If statement is an expression that can be evaluated as true or false and is called a conditional test. 
#Python uses the value of 'True'  and 'Fasle' to decide whether the code in an if statemnt should be executed.
#If conditional test evaluates 'True', the following code is executed. 
#if false, the following code is ignored.
#-----------------------------------------------------Checking for Equality ------------------------------------------------------- 
# most conditional statement compare the current value of a variable to a specific value of interest. 
#returns true 
car = 'bmw' #define the variable 
car == 'bmw' #checks whether the value of car is equal to specific value of interest by using '=='. 
#The equality operator returns 'True' if the values on the left and right side of the operations match. 
#if false, returns 'False'.

#returns fasle
car = 'audi'
car == 'bmw'
#-----------------------------------------------------Ignoring Case When Checking for Equality  ------------------------------------------------------- 
# Testing equality is case sensitive

#Return false
car = 'Audi'
car == 'audi'

#Return True
car = 'Audi'
car.lower() == 'audi'

#-----------------------------------------------------Checking for Inequality  ------------------------------------------------------- 
#When you want ot determine whether two values are not equal, you can use the inequality operator '!='

requested_topping = 'muchrooms'
if requested_topping != 'anchovies':
    print("Hold the anchioves!")
# The code above compares the value of requested_topping to the value 'anchovies. 
#if these two values does not match, Python returns 'True' and executes the code. 
#if the two values does match, Python returns 'False' and does not execute the code 

#-----------------------------------------------------Numerical Comparisons ------------------------------------------------------- 
#Return true
age = 18
age == 18 

#also can test if two values are not equal 

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

#Mathematicla comparison operators 

age = 19
# greater than '>'
if age > 21:
    print(age, "is greater than 21")
# great than or equal ' >='
if age >= 21:
    print(age, "is greater than or equal to 21.")
# less than '<'
if age < 21:
    print(age, "is less than 21")

# less than or equal '<=' 
if age <= 21:
    print(age, "is less than or equal to 21")
#-----------------------------------------------------Checking Multiple Conditions ------------------------------------------------------- 
#Logical Operator 
print("\nLogical Operators")
#AND Returns True if both statements are true
age_0 = 22
age_1 = 18

if (age_0 >= 21) and (age_1 >= 21): 
    print("True")
else:
    print("False")

#Update variable 
age_1 = 22

if (age_0 >= 21) and (age_1 >= 21):
    print("True")
else:
    print("False")

#To improve readability you can use parentheses around the individual tests, but they are not required.

#OR Returns True if one of the statements is true
age_0 = 22 
age_1 = 18
if age_0 >= 21 or age_1 >= 21: # if(22 >= 21) or (18 >= 21) --> if(True) or (False) --> True 
    print("True")
else:
    print("False")
    
#Update
age_0 = 18
if age_0 >= 21 or age_1 >= 21: #if (18 >= 21) or (18 >= 21) --> if(false) or (false) --> False 
    print("True")
else: 
    print("False")
#overall expression evaluates to 'False'

#-----------------------------------------------------Checking Whether a Value Is in a List ------------------------------------------------------- 
# To check whether an existing value exist in the list is to use the keyword 'in'

requested_topping = ['muchrooms','onions','pineapple']
#Return True
if 'muchrooms' in requested_topping:
    print("Topping Available")
else:
    print("False")
    
#Return false 

if 'pepperoni' in requested_topping: 
    print("Topping Available")
else:
    print("Topping not available")
#-----------------------------------------------------Checking Whether a value is not in a list------------------------------------------------------- 
#There are time when it is important to know if a value does not exist in a list.
#Keyword 'not'
banned_users = ['andrew','carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
#-----------------------------------------------------Boolean Expressions------------------------------------------------------- 
#Boolean Expression: is an exprssion that evaluates to either TRUE or FALSE
#what are they used for ? 
#Used to keep track of certain conditions, such as whether a game is running or whether a user can edit certain content on a website 
game_active = True
can_edit = False 

#Boolean values provide an efficient way to track the state of a program or a particular condition that is important in your program 

