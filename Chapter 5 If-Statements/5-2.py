#Chapter 5-2 If else statements
#-----------------------------------------------------Simple if statements------------------------------------------------------ 
#if conditional_test: 
    #do something 

#Example 1: Test whether the person is old enough to vote 

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
# Indentation determines the scope of code blocks

#If the value of age is less than 18, this program would produce no output

#-----------------------------------------------------if-else statements------------------------------------------------------ 
# if-else statement is similar to a simple if statement, but the else statement allows you to define an action or set of actions that are executed 
# when the conditoin test fails

#Example 2: person old enough to vote? 

age = 17
if age >= 18: #If condition is true, the next condition block is ignored
    print("You are old enought to vote")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are to young to vote.")
    print("Please register to vote as soon you turn 18!")

#Only two possible solutions to evaluate
#-----------------------------------------------------The if-elif-else Chain----------------------------------------------------- 
# Often you'll need to test more than two possible situations and to evaluate by using the if-elif-else syntax.
#In this chain, Python only executes one block if it is true. Therefore, text is executed and Python skips the rest of the code

#Real world example 
#Amusement park that charges different reate for different age groups 

age = 26
#The first two test fails causing the else block to be executed.
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admisson cost is $25.")
else:
    print("Your admissoin cost is $40.")

#In each condition block sets a price value. 
#The indented lines set the value of price according to the person's age
#Simply determines the admission price rather outputing a message. 
if age < 4:
    price = 0
elif age < 18:
    price = 25
else: 
    price = 40
print(f"Your admission cost is ${price}.")
#-----------------------------------------------------Using Multiple elif Blocks-----------------------------------------------------
#You can use as many elif blocks in your code as you like. 
age = 12 
if age < 4: 
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else: #This code block is any else thats greater than 65 or equal admission cost is 20 
    price = 20
print(f"Your admisson cost is ${price}\n")

#-----------------------------------------------------Omitting the else Block -----------------------------------------------------
#Omitting: to leave out or leave unmentioned
#else block is not requried at the end of an if else chain 
age = 12
if age < 4: 
    price = 0
elif age < 18: 
    price = 25
elif age < 65:
    price = 40
#It is clearer to use an additional elif statement that catches the specific condition of interest
elif age >= 65:
    price = 20
    
#-----------------------------------------------------Testing Multiple Conditions -----------------------------------------------------
#sometimes it is important to check all conditions of interest. 
#Therefore, use a series of if statements with no elif or else blocks 
#This technique makes senxe when more than one condition could be 'True' and you want to act on every coniditon that is 'True'

#Example ---- If someone requests a two-topping pizza, you'll need to be sure to include both topping on their pizza
requested_toppings = ['muchrooms','extra cheese']
if 'muchrooms' in requested_toppings:
    print("Adding muchrooms.")
if 'pepperoni' in requested_toppings:
    print("Addnig pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!\n")

#This code would not work properly if we used an if-elif-else block becuase the code will only execute one block and stop running. 
if 'muchrooms' in requested_toppings: #first to pass 
    print("Adding muchrooms.")
elif 'pepperoni' in requested_toppings: #Not checked
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings: #Not checked
    print("Adding extra cheese.")
print("\nFinished making your pziza!")
