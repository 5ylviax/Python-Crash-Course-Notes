#Chapter 5
#Exercise 5-1 Conditional Tests
#You do not have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests and add them to conditional_test.py. 
#Have at least one True and one False result for each of the following: 

#test for equality and inequality with strings 
car = 'porshe'
#False
if car == 'Porshe': 
    print("True")
else:
    print("False")

#True
if car.title() == "Porshe":
    print("True")
else:
    print("False")
    
#------------------------------------------------------Inequality------------------------------------------------
#False
mouse_brand = 'Finalmouse'
#test using the lower() method
if mouse_brand.lower() != 'finalmouse':
    print("True")
else:
    print("False")
#True
if mouse_brand != 'razer':
    print("True")
else: 
    print("False")
    
#Numerical tests involving equality and inequality, greater than and less than, greather than or equal to, and less than or equal to

my_age = 26 
age = 10
if my_age > 20 and my_age < 30:
    print("You are in your twentys")

if age != 15:
    print("It is not your quincenera!")
if age >= 21: 
    print("You're an adult")
if age <= 21:
    print("You are still not old enough")
    
#Test whether an item is in a list 

keyboard_brands = ['ducky','razer','high ground','logitech']
keyboard = 'ducky'
if keyboard in keyboard_brands:
    print(f"{keyboard.title()} keyboard is in the list.")
    
#Test whether an item is in a list
banned_users = ['carolina','david','josh','mary']
user = 'silvia'

if user not in banned_users:
    print("You are allowed. ")
else:
    print("You are not allowed.")
    