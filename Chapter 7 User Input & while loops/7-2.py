#Chapter 7 Section 2: Introducing while loops 
#For loops takes a collection of items and executes ablock of code once for each item in the collection. 
# In contrast, while loop runs as long as, or while, a certain condition is true. 

#----------------------------------------------------The while loop in action ---------------------------------------------------
#Counting from 1 to 5
current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1

#---------------------------------------------------Letting the User Choose When to Quit ---------------------------------------------------
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)


#---------------------------------------------------Using a Flag---------------------------------------------------
#For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active. 
#This variable is called flag, acts as a signal to the program.
#In the program, it can run whle the flag is set to True and stop running when any of several events set the value of the flag to False 
#As a result, the while statement needs to check only one condition: whether the flag is currently True. 
#Then, all our other tests can neatly oragnized in the rest of the program.
print("\nUsing a Flag")

active = True #variable set to true, so the while loop starts in an active state 

while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False #while loop stops if condition is met 
    else:
        print(message)
#---------------------------------------------------Using break to Exit a loop---------------------------------------------------
#Try to avoid this !!!!!!!!

#To exit a while loop immediately without running any remaining code in the loop, regardless of the result of any conditonal test,
#use the break statement.

#The break statement, directs the flow of your program; you can use it to control which lines of code are executed and which aren't,
#so the program only executes code that you want it to, when you want it to. 

#Example ------------
prompt = "\nPlease enter the name of the city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

'''
you can use th break statement in any of Python's loops. For example, you could use break to quit a for loop that's working through a list or a dictionary 

'''
#---------------------------------------------------Using continue in a loop ---------------------------------------------------
#Rather than breaking out of a loop entirely wihtout executing the rest of its code, you can use the continue statement
#to return to the beginning of the loop, based on the result of a conditional test.

#Example - 
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
#Prints odd numbers 

#---------------------------------------------------Avoiding infinite loops---------------------------------------------------
#Every while loop needs a way to stop running so it won't continue to run forever. 

#if program gets stuck in an infinite loop, press CTRL-C or just close the terminal window displaying your program's output. 


