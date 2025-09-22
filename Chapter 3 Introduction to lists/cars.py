#------------------------------------------------------Organizing a List -----------------------------------------------------
cars = ['bmw', 'audi','toyota','subaru']
cars.sort()
print(cars)

#sort() method changes the order of the list permanently, now alphabetical order 

#-------Reverse Oder----------
cars.sort(reverse=True)
print("\n")


#-------------------------------Sorting a list Temporarily with the sorted() funciton-----------------------------
# To maintain the original order of a list but present it in a sorted order, you can use the 'sorted()' fucntion 
#sorted() -- function lets  you display  your list in a particular order, but does not affect the acutal order of the list 
print("Here is the original list: ") #1 we first print the list in its original order
print(cars)

print("Here is the sorted list:") #2 print in alphabetical order 
print(sorted(cars))

print("Here is the orignal list again:") #3 After displaying in the new order, we show that the list is still stored in its original form 
print(cars) # OUTPUT ---> toyota, subaru, bmw , audi

#------------------------------------------------------Printing a List in Reverse Order --------------------------------------------------------
print(cars) # OUTPUT ---> toyota, subaru, bmw , audi
cars.reverse() #rearrange teh list into reverse-chronological order 
print(cars)
print("\n\n")

#------------------------------------------------------Finding a Length of a List -------------------------------------------------------
games = ['Deadlock','Apex Legends', 'Valorant','Assassin Creed Games']
num = len(games)
print(num)
#Python counts items in a list starting with one, so you wouldn't run into any off-by-one errors when determining the length of a list 
