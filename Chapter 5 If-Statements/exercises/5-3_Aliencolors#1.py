#Chapter 5
#Exercise 5-3 Alien Colors #1
#Imagine an alien was just shot down in a game. Create a variable called alien_color and assing it a value of 'green', 'yellow', or 'red'.
alien_color = 'green'

#write an if statement to test whether the alien's color is green. If it is, print a message that the player just earned 5 points.
if alien_color == 'green':
    print("You earned 5 points.")
#Write one verson of this program that passes the if test and another that fails. (The version that fails will have no outputs.)
alien_color = 'blue'
#Fails
if alien_color == 'red':
    print("You earned 5 points!")

#Pass
if alien_color == 'blue':
    print("You earned 5 points!")