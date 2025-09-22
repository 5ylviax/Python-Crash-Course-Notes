#Chapter 4-4: Working with part of a list 
#work with a specific group of items in a list, called a slice in Python 
#-----------------------------------------------------Slicing in a list -------------------------------------------------------
# to make a slice, you specify the index of the first index and last elements you want to work with. 
players = ['charles', 'martina', 'michael', 'florence', 'eli']
#To output the first three elements in a list, you wuld request indices 0 through, which would return elements 0,1, and 2.
# This code prints slice of the list. 
print(players[0:3])


# Can generate any subset of a list. 
print(players[1:4])

#Omit the first index in a slice 
print(players[:4]) #withou a starting index, Python starts at the beginning of the list 

#This syntax allows you to output all of the elements from any point in the list to the end, regardless of the length of the list. 
print(players[2:])

#Recall that a negative index returns an element a certain distance from the ned of a list
print(players[-3:])
''' 
Note: You can include a third value in the brakets indicating a slice. If a third value is included, this tells Python how many items to skip ebtween items in the specified
range
'''
#-----------------------------------------------------Looping through a slice-------------------------------------------------------

#You can use a slice in a for loop if you want to loop through a subset of the elements in a list. 
print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())
#What are slices useful?
#when creating a game, you could add a player's final score to a list every time that player finishes playing. Then you could 
#then get a player's top three scores by sortint the list in decreasing order and taknig a slice that includes just hte first three scores. 
#-----------------------------------------------------Copying a list -------------------------------------------------------
#often you start with an existing list and make a new list based on the first list. 
#to copy a list:
#you can make a slice that includes the entire original list by omitting the first index and the second index ([:]).
#this tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list. 

my_foods = ['pizza','hotdog', 'carrot cake', 'alfredo']
friend_foods = my_foods[:]
print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)
print("\nAfter the update:")

#steps:
#1. Create a list
#2. create a new list by requesting a slice of the original list without specifying any indices by using ([:])
#3. Assign the copy to the new list
#4. print both list to see if they match.If they match, it is correct. 

#To prove these two list are different, well append a new food on both list of different food type. 
my_foods.append('cheese cake')

friend_foods.append('cereal')
friend_foods.append('oranges')

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

#What happends if i copy a code and assin it without slicing?
#example my_foods = ['pizza','hotdog', 'carrot cake', 'alfredo']
#friend_foods = my_foods 
#this does not work !!!!!!!!!!!
#Does not work because adding a new element to a list would add to both list. 
#Therefore, copying a list of elements requires slicing 
