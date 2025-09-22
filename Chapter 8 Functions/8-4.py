#Chapter 8 Passing a List
#----------------------------------------------------Passing a List----------------------------------------------------
#You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
def greet_users(names):
    """Print a simple greeting to each user in the list. """
    for name in names: 
        msg = f"Hello, {name.title()}!"
        print(msg)
        
usernames = ['hannah', 'ty', 'margot']

greet_users(usernames)

#----------------------------------------------------Modifying a list in a Function----------------------------------------------------
print("\n----------Modifying a list in a Function----------------\n")
#When  you pass a list to a function, the function can modify the list. 
#Any changes made to the list inside the function's body are permanent. 

#Start with some desgins that need to printed 

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#Stimulate printing each design, until non are left
#Move each design to completed models after printing. 

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
    
#Display all completed models 
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    
#-------------------------------Reorganize the code by writing two functions, each of which does one specific job----------------------------
print("\n--------Reorganize the code by writing two functions----------------\n")
#Handles printing the designs 
def print_models(unprinted_Designs, completed_Models):
    """
    Stimulate printing each design, until non are left.
    Move each desgin to completed_models after printing.
    """
    while unprinted_Designs:
        current_design = unprinted_Designs.pop()
        print(f"Printing model: {current_design}")
        completed_Models.append(current_design)
        
#summarize the prints that have been made

def show_completed_models(completed_Models):
    """Show all the models that were printed """
    print("\nThe following models have been printed: ")
    for completed_model in completed_Models:
        print(completed_model)
        
#Code is more readable
unprinted_Designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_Models = []

print_models(unprinted_Designs,completed_Models)
show_completed_models(completed_Models)

#This program demonstrates the idea that every functions should have one specific job! 

#----------------------------------------------------Preventing a Function from Modifying a List ----------------------------------------------------
print("\n--------Preventing a Function from Modifying a List----------------\n")
# To prevent a function frmo modifying a list is by passing the function a copy of the list.
# function(name(list_name[:]))

#the slice notation [:] makes a copy of hte list to send to the function. 
print_models(unprinted_Designs[:], completed_Models)

#Its more efficient for a function to work with an existing list, because this avoids using thtime and memory neded to make a separate copy. 
