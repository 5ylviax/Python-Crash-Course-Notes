#Chapter 5
#---------Version #1
#Exercise 5-5 Alien Colors #3
# Turn your if-else chain from Exercise 5-4 into an if-elif-else chain
alien_color = 'red'

#If the alien is green, print a message that the player earned 5 points.
if alien_color == 'green':
    print("You earned 5 points.")

#If the aline is yellow, print a message that the player earned 10 points.
elif alien_color == 'yellow':
    print("You earned 10 points. ")
#If the alien is red, print a message that the player earned 15 points.
elif alien_color == 'red':
    print("You earned 15 points.")
#Write three versions of this program, making sure each message is printed for the appropriate color alien. 

#----------Version #2 

topping = 'muchrooms'

if topping == 'pepperoni':
    price = 4
elif topping == 'muchrooms':
    price = 5
elif topping == 'extra cheese':
    price = 6
print(f"This topping ({topping}) adds an extra ${price} on your order.")

#------------Version #3


mouse_brand = 'finalmouse'

if mouse_brand == 'logitech':
    price = 140
elif mouse_brand == 'finalmouse':
    price = 180 
elif mouse_brand == 'zowie':
    price = 140
print(f"My {mouse_brand.title()} costs ${price}.")