#Chapter 6
#objective:
#- build dictionaries
#- loop through dictionaries
#- use dictionaries with combination with lists and if statements.
#- nesting 
#Dictionaries: is similar to a list, but it allows you to connect pieces of information. 
#Dictionaries can store an almost limitless amount of information. 
#-----------------------------------------------------A simple Dictionary------------------------------------------------------
#Simple  dictionary stores information about a particular alien:

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color']) #Prints 'green'
print(alien_0['points'])#Prints '5'
#-----------------------------------------------------Working with Dictionaries------------------------------------------------------
#A dictionary in Python is a collection of key-value pairs. 
#Each key is connected to a value, and you can use a key to access the value associated with that key. 
# A key's value can be a number, a string, a list, or even another dictionary. 
# In Python, a dictionary is wrapped in braces ({}) with a series of key-value paris inside the braces, as shown in the earlier example: 

alien_0 = {'color': 'green', 'points': 5}

#A key value pair is a set of values associated with each other.
# When you provide a key. Python returns the value associated with that key.
# Every key is connected to its value by a colon, and individual key-value pairs are separeated by commas. 

#simple dictionary has one key-value pair
alien_0 = {'color' : 'green'}
# The string 'color' is a key in the dictionary, and it is associated value is 'green'.

#-----------------------------------------------------Accessing Values in a Dictionary------------------------------------------------------
#To get the value associated with a key, give the name of the dictionary and then place the key inside a set of sqaure brackets.
#Return the value associated with the key 'color' from the dictionary.
print(alien_0['color'])

#Defined dictionary
alien_0 = {'color': 'green', 'points': 5}

#Pull the value associated with the key 'points' from the dictionary.
#The value is assigned to the variable new_points. 
new_points = alien_0['points']
#prints 
print(f"You just earned {new_points} points!")


#-----------------------------------------------------Adding New Key-Value Pairs------------------------------------------------------
#Dictionaries are dynamic structures. 
#It is called dynamic because:
#- You can add, remove, or update key-value pairs at runtime.
#- The size of the dictionary can grow or shrink dynamically as needed.
#- Internally, Python handles resizing the underlying hash table automatically.

#Python dictionaries are runtime, dynamic structures - they grow, shrink, and update while the program runs 
#Runtime = when the code is actually exectuing. Things can change dynamically. 

#Adding new key-value pairs to a dictionary 

#How would i add a new key value to my dictionary?
#1. you would give the name of the dictionary followed by the key value in square brackets, along with the new value.

#old
print(alien_0)

# adding two new key values
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

#Final dictionary contains four key-value pairs. 
#Dictionaries retina the order in which they were defined. 

#-----------------------------------------------------Starting with an Empty Dictionary------------------------------------------------------
#Define an empty dictionary with an empty set of braces
print("\nAn empty dictionary")
alien_0 = {}
#add each key-value pair on its own line.
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
#-----------------------------------------------------Modifying Values in a Dictionary------------------------------------------------------
# To modify a value in a dictionary, give the name of the dictionary wit hthe key in a square brackets and then
# the new value you want associated with that key
#For example: 
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

#Change the color to yellow 
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

#Another example of tracking the position of an alien that can move at different speed. 

# A define dictionary that stores values representing the alien's current speed and
# then use it to determine how far to the right the aline should move. 
alien_0 = {'x_position': 0, 'y_position': 25, 'speed' : 'medium'}
print(f"\nOriginal position: {alien_0['x_position']}")

#Move the alien to the right. 
#Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}\n")

#Update overall behavior of the alien speed 
alien_0['speed'] = 'fast'
# The if-elif-else block would then assign a larger value to x_increment the next time the code runs 

#-----------------------------------------------------Removing Key-Value Pairs ------------------------------------------------------
# When information stored in a dictionary is no longer needed, the 'del' statement can be used to remove a key-value pair.
# All 'del' needs is the name of the dictionary and the key that you want to remove.
#Example: 

alien_0 = {'color': 'green', 'points': 5}

del alien_0['points']
print(alien_0)
'''
Note: Be aware that the delted key-value pair is removed permanently.'''

#----------------------------------------------------- A Dictionary of Similar Object ------------------------------------------------------
# The previous dictionary example involved storing information about one object. However, dictionaries can also be used to store 
# one kind of information about many objects.
#Example:
#You want to poll a number of people and ask then what their favorite programming language is. 
# A dictionary is usefol for storing the results of a simple poll
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
#Broken a larger dictionary into several lines. 
#Each key is the name of the person who responded to the poll, and each key value is their language choice. 
 
'''
Most editors have some functionality that helps you format extended lists and dictionaries in a similar manner to this example.
Other acceptable ways to format long dictionaries are available as well, so you may see slightly different formatting in your editor,
or in other sources.
'''
#To use the dictionary, given the name of a person who took the poll, you can easily look up their favorite language
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

#----------------------------------------------------Using get() to Access Values ------------------------------------------------------
#using keys to retrieve the value of interest from a dictionary might cause one potential problem:
# if the key you ask for does not exist, you'll get an error 

alien_0 = {'color': 'green', 'speed': 'slow'}

# print(alien_0['points']) 
#results in a traceback, showing a keyError 
# For dictionaries specifically, you can use 'get()' method to set a default value that will be returned if
# the requested key does not exist
#1. 'get()' method requires a key as a first argument. 
#2. As second optional argument, you can pass the value to be returned if they key value does not exist

point_value = alien_0.get('points','No value assigned.')

print(point_value)

'''
Note: 
if you leave out the second argument in the call to get() and the key does not exist, Python will return the value 'None'. The special 
value 'None' means "no value exists." This is not an error: it's a special value meant to indicate the absence of a value.
'''