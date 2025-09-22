#Chapter 5 Section 3 

#-----------------------------------------------------Using if statements with lists ------------------------------------------------------
#Objective: Combine lists and if statements

#--------Checking for special items 

#simple For-Loop
requested_toppings = ['pepperoni','muchrooms', 'green peppers', 'extra cheese']
for topping in requested_toppings:
    print(f"Adding {topping}.")
print("\nFinished mkaing your pizza!")

#However what happens if the pizzeria runs out of ingredientes?
#An if statement inside the for-loop can handle this situation


requested_toppings = ['pepperoni','muchrooms', 'green peppers', 'extra cheese']
# A nested if statement inside a for loop 
for topping in requested_toppings:
    if topping == 'green peppers':
        print("\nSorry, we are out of green peppers right now.")
    else:
        print(f"Adding {topping}")
print("\nFinished making your pizza!")

#-----------------------------------------------------Checking that a list is not empty ------------------------------------------------------

#in the previous exercise, we assumed that a list so far has at least one item in it. 
#However, we would be requesting the user information to add to the list and we wont be able to assume that a list has any items 
#in it each time a loop is run.
#To solve this problem is to check whether a list is empty before running a for loop

#Empty list
requested_toppings = []
#When the name of a list is used in an if statement, Python returns 'True if the list contains at least one item;
#an empty list evaluates to 'False'
if requested_toppings: #conditional statement--> True --> continue the first conditional block
    for topping in requested_toppings:
        print(f"Adding {topping}.")
    print("\nFinished making your pizza!")
else: # If false, we ask the customer a question.
    print("Are you sure you want a plain pizza?")
#-----------------------------------------------------Using Multiple Lists------------------------------------------------------
print("\nUsing Multiple List\n")
#Define a list of available toppings at this pizzaria.
available_toppings = ['muchrooms', 'olives', 'green peppers', 'pepperoni',
                      'pineapple', 'extra cheese']
#The topping the customer has requested
requested_toppings = ['muchrooms', 'french fries', 'extra cheese']

#Loop throught the list of request toppings. 
for requested_topping in requested_toppings:
    #Inside the loop, we check to see if each requested topping is actually in the list of available toppings.
    if requested_topping in available_toppings: #If true, we add it to the pizza
        print(f"Adding {requested_topping}.")
    else: #if false, we leave a message to the customer stating we dont have the ingredient of requeted topping.
        print(f"Sorry, we don't ahve {requested_topping}.")
print("\nFinished making your pizza!")