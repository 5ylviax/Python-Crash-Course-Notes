#Chapter 6 Section 2 Looping through a Dictionary
#----------------------------------------------------Looping through a Dictionary ------------------------------------------------------
# A dictionary can contain large amouts of data, Python lets you loop through a dictionary. 
#Dictionarys can be used to store information in a variety of ways; therefore, several different ways exist to loop through them. 
# -- can loop through all of a dictionary's key-value pairs, through its keys, or through its values.

#----------------------------------------------------Looping through All Key-Value Pairs ------------------------------------------------------
user_0 = {
    'username': 'efermi',
    'first': 'enrico', 
    'last': 'fermi',
}

# Use a for loop to go through the dictionary and access every piece of information stored in it.

#To write a for loop for a dictionary, you create names for the two variable that will hold the key and value in each key-value pair. 
for key, value in user_0.items(): # items() method which returns a sequence of key-value pairs.
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print("\n")  

#another example
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust', 
    'phil': 'python', 
    'silvia': 'c++',
    }


for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
    
#----------------------------------------------------Looping through All the Keys in a Dictionary ------------------------------------------------------
#keys() method is useful when you dont need to work with all of the values in a dictionary. 
#Loop through the favorite_language dictionary and print the name of everyone who took the poll

for name in favorite_language.keys():
    print(name.title())
print("\n")
#Looping through the keys is actually the default behavior whne looping through a dictionary
# for name in favorite_ language:
#              same as 
# for name in favorite_language.key():

friends = ['phil', 'sarah']

for name in favorite_language.keys():
    print(f"Hi {name.title()}.")
    
    if name in friends:
        language = favorite_language[name].title()
        print(f"\t {name.title()}, I see you love {language}!")
        
#You can also use the keys() method to find out if a particular person was polled. 
#Lets find out if Erin took the poll

if 'erin' not in favorite_language.keys():
    print("Erin, please take the poll!")

#keys() method is not just for looping: it actully returns a sequence of all the keys and the if statement simply checks if 'erin' is in this sequence. 

#----------------------------------------------------Looping Through a Dicitonary's Keys in a Particular Order ------------------------------------------------------
#Looping through a dictionary returns the items in the same order they were inserted. 
#sorted() function to get a copy of the keys in order
print("\nPrinting a dictionary's keys in particular oder\n")
for name in sorted(favorite_language.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
    
#----------------------------------------------------Looping Through All Values in a Dictionary ------------------------------------------------------
# If you are primarily interested in the values that a dictionary contains, you can use the values() method to return a sequence of values without any keys. 
#Example: List of languages chosen in the programming language poll
print("\nThe following languages have been mentioned: ")
for language in favorite_language.values():
    print(language.title())
#This approach pulls all the values form the dictionary without checking for repeats.

#To see each language chosen without repetition, we can use a set. 
# A set is a collection in which each item must be unique. 
for language in set(favorite_language.values()): #when you wrap set() around a collection of values that contains duplicate items
    #python indentifies the unique items in the collection and builds a set from those items.
    print(language.title())
    
#the result is a nonrepetitive list of languages that have been mentioned

'''
Note: you can build a set directly using braces and separating the elements with commas:
'''

languages = {'python', 'rust', 'python', 'c'}
print(languages)

'''
It is easy to mistake sets for dictionaries because they're both wrapped in braces. 
When you see braces but no key-value pairs, you're probably looking at a set. 
Unlike lists and dictionaries, sets do not retain items in any specific order.
'''