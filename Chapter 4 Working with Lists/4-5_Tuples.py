#Chapter 4-5: Tuples 
#Tuples allows you to create a list of items that cannot be changed. 
#Python refers to values that canot change as immutable, and an immutable list is called tuple.
#Tuple uses parentheses instead of square brackets.
#1. Define a tuple 
#2. access indivdiual elements by using each item's index. 

#Example: if we have a rectangle that should always be a certain size,  we can ensure that its size does not change by putting the dimensions into a tuple 
dimensions = (20,50) #Define using parentheses
print(dimensions[0])
print(dimensions[1])

#What happens if we attempt to change one of the elements in the list? 
#---> dimensions[0] = 250

#This code atttempts to change the value of the first dimensions, but Python returns a type error. 
#Because the code is trying to alter a tuple, which can not be done to that type of object. 

#Note: To use a tuple it is required to use more than one element. However, using one element in a tuple is allowed if tuples are techinically defined by the precence of a comma 
#Therefore, to define a tuple with one element, need to include a trailing comma 
#my_t = (3,) <------- Tuple with one element 
#-----------------------------------------------------Looping through all values in a tuple -------------------------------------------------------
#Looping through a tuple is excatly the same thing done with a regular list. 


#-----------------------------------------------------Writing over a tuple  -------------------------------------------------------
#Can not modify a tuple, but you can assing a new value to a variable that represents a tuple. 
#For example, if we wanted to change the dimensions of this rectangle, we could define the entire tuple. 

print("Original dimensions: ")

for dimension in dimensions: 
    print(dimension)
   
#Python  does not raise any errors because reassigning a variable is valid 
dimensions = (400,100) # associate a new tuple with new variable dimensions and print the new values. 


print("\nModified dimensions: ")
for dimension in dimensions: 
    print(dimension)
    
#When to use tuple? 
#Tuples are simple data strucutres. Use them when you want to store a set of values that should not be changed throughout the life of a program. 

    
    



