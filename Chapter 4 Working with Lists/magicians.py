#Chapter 4: Working with Lists 
#Objective: Learn how to loop through an entire list
#Loop: allows you to take the same action, or set of actions, with every item in a list. 
#-----------------------------------------------------Looping through an entire list --------------------------------------------------------
#Example 1
#Print out each name in the list. How? using for-loop

magicians = ['alice', 'david', 'carolina'] #step 1: Define a list 
for magician in magicians: #step 2: Define a for-loop, the line tells us to pull a name from the list magicians, and associate it with the variable magician. 
    print(magician) #step 3: print the name that's just been assigned to magician
#output
#alice
#david
#carolina
#Read this code as "For every magician in the list of magicians, print the magician's name"
#-----------------------------------------------------A closer look at looping --------------------------------------------------------
#the set of steps is repeated once for each item in the list, no matter how many items are in the list 
#when writing your own for loops that you can choose any name you want for the temporary variable that will be associated with each value in the list. 
# for cat in cats: 
#for singular_Name in plural_Names:

#-----------------------------------------------------Doing more work within a for loop--------------------------------------------------------
#Example 2 
print("Example 2: Doing more work within a for-loop.\n")
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
#Every indented line following the line is considered inside the loop, and each indented line is executedd once for each value in the list
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
#-----------------------------------------------------Doing Something After a for loop -------------------------------------------------------
#What happens once a for loop has finished executing? 
#usually you'll want to summarize a block of output or move on to other work that your program must accomplish
#Any lines of code after the for loop that are not indented are executed once without repetition
print("Thank you, everyone. That was a great magic show!")

#----------------------------------------------------Avoiding Indentation Errors-------------------------------------------------------
#common errors: 
#-- people often ident lines of code that do not need to indented or forget to indent lines that need to be indented
#-- forgetting the colon 

#----------------------------------------------------Forgetting to Indent-------------------------------------------------------
#Must do:
#--always indent the line after the for statment in a loop. 
#----------------------------------------------------Forgetting to indent Additional lines-------------------------------------------------------
print("Forgetting to indent Additional Lines.\n")
animals = ['dog', 'cat','rabbit', 'groundhog']
for animal in animals:
    print(f"{animal.title()} are the best pet.\n")
print(f"I can wait to have a {animal.title()} as a pet!") # Logic Error 
#the second call to print is suppoed to be indented 
#python does not report an error, as a result, the second print() call is not indented, so it is executed only once after the loop has finished runnning
#because the final associated value with animal is 'groundhog'. The animal groundhog is the only value receives the print call
#----------------------------------------------------Forgettint the colon -------------------------------------------------------
#the colon at the end of a for statement tells python to interpret the next line as the start of a loop 
# If you accidentally forgot the colon, you'll get a syntax error because Python does not know exactly what you're trying to do: 
