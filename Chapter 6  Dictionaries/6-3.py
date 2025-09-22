#Chapter 6
#----------------------------------------------------Nesting------------------------------------------------------
# a Nested dictionary is a dictionary that contains other dictionaries as values. 
# This creates a hierarchical or multi-level data structure, allowing for the organization of complex and related data. 

#----------------------------------------------------A List of Dictionaries ------------------------------------------------------
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# A list of in which contains a dictionary of information
aliens_ = [alien_0, alien_1, alien_2]

for alien in aliens_:
    print(alien)
    
# Generating more than 3 aliens automatically by using range() to create a fleet of 30 aliens

#Define an empty list
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#Use slice to show the first 5 aliens 
for alien in aliens[:5]:
    print(alien)
print("...")

#Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")

#These alien stored in aliens have the same characteristic. However, in Python considers each one a separate object, which allows us to modify each alien individually

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] ='yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 5

#Print the first three objects 
for alien in aliens[:5]:
    print(alien)
print("...")
#----------------------------------------------------A List in a Dictionary ------------------------------------------------------
# A list inside a dictionary. 
#Example: two kind of information is stored for each pizza: 
# a type of crust and a list of topping
#The list of topping is a value associated with the key 'toppings'. 

#Store infromation about a pizza being stored 
pizza = {
    #Key: crust, associated with the value 'thick'
    'crust': 'thick',
    #Key = 'toppings', has a list as its value that stores all requested toppings
    'toppings': ['muchrooms', 'extra cheese'],
}

#Summarize the order 

print(f"You ordered a {pizza['crust']}-crust pizza"
      " with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
    
#-------------------------------------Example 
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}
# Inside the dictionarys's for loop, we use another for loop to run through the list of languages associated with each person

for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print(f"\n{name.title()}'s favorite language is {languages[0].title()}")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")

'''
Note: You should not nest lists and dictionaries too deeply. If you're nesting items much deeper than what y ou see in the preceding examples,
or if you're working with someone else's code with significant levels of nesting, there's most likely a simpler way to solve the problem.
'''
#----------------------------------------------------A Dictionary in a Dictionary ------------------------------------------------------
#Nesting a dictionary inside another dictionary is possible,but code gets complicated. 
#Example: serveral users for a website, each with a unique username, you can use the usernames as the keys in a dictionary. 
#Store information about each user by using a dictionary as the value associated with their usernames. 

#Define users with two keys
users = {
    #a value associated with each key is a dictionary
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"Username: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location =  user_info['location']
    
    print(f"\tFullname: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    
#if each user's dictionary had different keys, the code inside the for loop would be more complicated 

