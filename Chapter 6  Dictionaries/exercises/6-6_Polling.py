#Chapter 6 
#Exercise 6-6 Polling: 
#Use the code in favorite_language.py (pg. 96)
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
#Make a list of people who should take the favorite language poll. Include some names that are already in the dictionary and some that are not.
newList = { 'silvia', 'kate', 'robert', 'david'}
#Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. 
#If they have not yet taken the poll, print a message inviting them to take the poll. 

for name in newList:
    if name in favorite_languages: # loop automatically by default by keys 
        print(f"{name.title()}, thank you for taking the poll!")
    else:
        print(f"{name.title()}, you are invited to take the poll.")

