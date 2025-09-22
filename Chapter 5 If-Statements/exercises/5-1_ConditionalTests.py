#Chapter 5
#Exercise 5-1 Conditional Tests
#Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code sh ould look something like this:
#--------Example 1
cars = ['subaru','mitsubishi','toyota','honda','porshe']
my_car = 'bmw'
#False
if my_car in cars:
    print(f"{my_car.title()} found in the list.")
else: 
    print("Not found")

#True
dream_car = 'porshe'
if dream_car in cars:
    print(f"{dream_car.title()} is in the list.")
else:
    print("Not found")
    
#----------Example 2 
mouse_brands = ['logitech', 'razer','finalmouse','steel serires']
old_mouse = 'finalmouse'
new_mouse = 'zowie'

#True
if old_mouse in mouse_brands:
    print(f"{old_mouse.title()} is in the list.")
else: 
    print("Not found")
#False 
if new_mouse in mouse_brands:
    print(f"{new_mouse} is in the list")
else:
    print("Not found")
#----------Example 3 
keyboard_sizes = [60,65,75,80,100]

my_favorite = 65
keypad = 13
#True
if my_favorite in keyboard_sizes:
    print(f"My favorite keyboard size in the list is {my_favorite}% keyboard")
else:
    print(f"My favoirte keyboard size is not in the list.")

if keypad in keyboard_sizes:
    print("The keyboard pad size is found int the list")
else:
    print("Not found ")



