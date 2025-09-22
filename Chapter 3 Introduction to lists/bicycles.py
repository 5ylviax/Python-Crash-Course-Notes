bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles)
#------------------------------------------------------------Accessing Elements in a List --------------------------------------------------------------------------------
#you can access any elements in a list by telling Python the position, or index, of the item desired

print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[3].title())
print(bicycles[-1].title()) #Python has a special syntax for accessing the last element in a list. if you ask for the item at index -1. Python
#well always returns the last item in the list
#------------------------------------------------------------Using Individuals Values from a List --------------------------------------------------------------------------------
message = f"My first bicycle was a {bicycles[0].title()}."
print(message + "\n")

#------------------------------------------------------------Modifying Elements in a List --------------------------------------------------------------------------------

carsBrand = ['testla', 'ford','nissan','toyota','kia','gmc','ram','porsche']
#lets modify the last one since it is a luxury brand 
print(carsBrand[-1])
carsBrand[-1] = 'Hyundai'
print(carsBrand[-1])
#------------------------------------------------------------Appending Elements to the End of a List --------------------------------------------------------------------------------

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

#start of an empty list 
print("Empty list, test on append")
emptyList = []
emptyList.append('honda')
print(emptyList)
emptyList.append('yamaha')
print(emptyList)
emptyList.append('suzuki')
print(emptyList)
#------------------------------------------------------------Inserting Elements into a list  --------------------------------------------------------------------------------
#you can add a new element at any position in your list by using the insert() method
#do this by specifying the index of the new element and the value of the new item 
# insert(index, new value)
 
motorcycles.insert(0,'unknown')
print(motorcycles)
#In this example, we insert the value 'unknown' at the beginning of the list. insert() method opens a space at a position 0 and stores the value 'unknown' at that location
#operation shifts every other value in the list one position to the right 
#------------------------------------------------------------Removing an Item Using the del Statement--------------------------------------------------------------------------------
del motorcycles[0]
print(motorcycles)

del motorcycles[-1]
print(motorcycles)
# you can remove any item in the list using the 'del' statement if you know its index  
#-----------------------------------------------------------Removing an Item Using the pop() method --------------------------------------------------------------------------------
#pop() method removes the last item in a list, but it lets you work with that item after removing it

gamesName = ['Helldivers', 'Apex Legends', 'Deadlock'] #1 defining and printing the list of games 
print(gamesName)

popGames = gamesName.pop() #2 Pop a value form the list, and assign that value to the variable popGames
print(gamesName)#3 print the list
print(popGames) #4 to prove that we still have access to the value that was removed from the list 

print(f"Last game played was {popGames.title()}")

#----------------------------------Removing an Item by Value ------------------------------------------------------
print(gamesName)
gamesName.remove('Apex Legends')
print(gamesName)
#remove() method tells Python to figure out where 'Apex Legends' appears in the list and remove that element 
to_easy = 'Helldivers'
gamesName.remove(to_easy)
print(f"\n{to_easy.title()} is too easy and it is recommended for everyone to play with friends.")