#Chapter 6 User input and while loops 
#----------------------------------------------------User Inputs and While Loops-----------------------------------------------------
# Most programs are written to solve an end user's problem, relying on their inputs to complete a task.
#Objective: 
#- accept user inputs
#- prompt
# input() function to request the end user input. 
# while loops to keep programs running as long as certain conditions remain true 
#----------------------------------------------------How the input() function works----------------------------------------------------
#input() function puases the program and waits for the user to enter their input. 
#Once python receives the user's input, it assigns that input to a variable to make it convenient for you to work with. 

#Example 
#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)

#input() function takes one argument: the prompt that we want to display to the user, so they know what kind information to enter. 
'''
Some text editors won't run programs that prompt the user for input. You can use these editors to write programs that prompt for input,
but you'll need to run these programs from a terminal. See "Running Pythons Programs from a Terminal" on page 11. 
'''

#----------------------------------------------------Writing Clear Prompts----------------------------------------------------
#Rules
#Each time you use the input() function, you should include a clear, easy-to-follow prompt that tells the user exactly what kind of information
#you're requesting.

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

#Example 

prompt = "If you share your name, we can personalize the message you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")
#----------------------------------------------------Using int() to Accept Numerical Input---------------------------------------------------
#input() function, Python interprets everthing the user enters as a string. 

age = input("How old are you? ")
print(age) #Python returns a string
#Python interpreted the input as a string because the number is now enclosed in qoutes. If you try to use the input as a number, it leads to an error. 

#Numerical comparison

age = int(age)  #value is converted to a numerical representation by int()
if age >= 18:
    print("You are older than 18!")
    
#Python produces an error due to comapring a string to an integer
#this solution is resolved by using the int() function, which converts input string to a numerical value.

#Example ----------

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall engough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

#----------------------------------------------------The Modulo Operator ---------------------------------------------------
#modulo operator (%) which divides one number by another number and returns the remainder 
#using the modulo operator is significant to determine if one number is either odd or even

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0: 
    print(f"\nThe number {number} is even. ")
else:
    print(f"\nThe number {number} is odd. ")