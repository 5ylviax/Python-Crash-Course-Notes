#Chapter 7-3 Using a while loop with lists and dictionaries 

#----------------------------------------------------Moving Items from One List to Another----------------------------------------------------
#Consider a list of newly registered but unverified users of a website 

#Example --- 
#Start with users that need to be verified 

#and an empty list to hold confirmed users 

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#Verfiy each user until there are no more unconfirmed users
# Move each verified user into the list of confirmed users 

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    
#Display all confirmed users 
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(f"\t{confirmed_user.title()}")
    
#----------------------------------------------------Removing All Instances of Specific values from a list ----------------------------------------------------
#The remove() method removes the specified item
#If there are more than one item with the specified value, the remove() method removes the first occurrence:
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# In a while loop it removes all instances of a value in a list 

pets = ['dog', 'cat','dog', 'goldfish', 'cat', 'rabbit', 'cat']

print(pets)

while 'cat' in pets:
    pets.remove('cat')
    
print(pets)

#----------------------------------------------------Filling a Dictionary with User Input ----------------------------------------------------
#Store the data into a dictionary according to the user response

responses = {}
#Set a flag to indicate that polling is active 

polling_active = True 

while polling_active:
    #Prompt for the person's name and response
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday? ")
    
    #Store the response in the dictionary 

    responses[name] = response
    
    #Find out if anyone else is going to take the poll 
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
    
#Polling is complete. Show the results 
print("\n---Poll Results ---")
    
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response}.")