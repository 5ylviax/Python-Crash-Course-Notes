#Chapter 8 Return Values 
#---------------------------------------------------- Return Values ----------------------------------------------------
#A return statement is used to end the execution of the function call and it "returns" the value of the expression following the return keyword to the caller.
# The statements after the return statements are not executed. If the return statement is without any expression, then the special value None is returned.
# A return statement is overall used to invoke a function so that the passed statements can be executed.

#---------------------------------------------------- Return a Simple Value ----------------------------------------------------

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')

print(musician)
#---------------------------------------------------- Making an Argument Optional----------------------------------------------------
#You can make an argument optional in Python by assigning it a default value in the function definition.

def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    
    return full_name.title()
musician = get_formatted_name('john','lee','hooker')

print(musician)

#However middle names are not always needed. This function would not work when calling the function with only first and last name 
#To make middle name optional. we can do this by making the middle_name argument an empty default value. 

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#Optional values allows function to handle a wide range of use cases 
#while letting function calls remain as simple as possible 

#----------------------------------------------------Returning a Dictionary----------------------------------------------------
# A function can return any kind of value you need it to, including more complicated data structures like lists and dictionaries.

#For example, the following function takes in part of a name and returns a dictionary representing a person

def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first': first_name,
              'last': last_name, 
              }
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

#This function takes in simple text information n puts it into a more meaningful data structure that lets y ou work with the information
#beyond just printing it 

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person"""
    person = {'first': first_name,
              'last': last_name, 
              }
    if age:
        person['age'] = age
    return person

#Adding a new optional parameter 
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

#----------------------------------------------------Using a Function witha while loop----------------------------------------------------
#You can use functions with all the Python structures you've learned about so far. 
def get_formatted(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    
    return full_name.title()

#Infinite Loop 
while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    
    print(f"\nHello, {formatted_name}!")
    
    