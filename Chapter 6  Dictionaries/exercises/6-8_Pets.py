#Chapter 6
#Exercise 6-8 Pets 
#Make several dictionaries, where each dictionary represent a different pet. In each dictionary, include the kind of animal and the owner's 
# name.

pet_0 = { 'animal': 'dog', 'owner': 'robert'}
pet_1 = { 'animal': 'rabbit', 'owner': 'silvia'}
pet_2 = { 'animal': 'chicken', 'owner': 'jacob'}
#Store these dictionaries in a list called pets.
pets = [pet_0, pet_1, pet_2]
# Next, loop through your list and as you do, print everthing you know about each pet 

for pet in pets:
    print(f"{pet['owner'].title()} owns a {pet['animal']}.")