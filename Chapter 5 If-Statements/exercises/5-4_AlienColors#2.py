#Chapter 5
#Exercise 5-4 Alien Colors #2
#Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain. 
alien_color = 'red'
#if the alien's color is green, print a statement that the player just earned 5 points for shooting the alien
if alien_color == 'green':
    print("You earned 5 points.")
#if the alien's color isn't green, print a statement that the player just earned 10 points.
if alien_color != 'green':
    print("You earned 10 points.")
#Write one version of this program that runs the if block and another that runs the else block.

alien_color = 'blue'
if alien_color == 'blue':
    print("You earned 2 point.")
else:
    print("No Points")
    
if alien_color == 'red':
    print("You earned 3 points.")
else:
    print("You earned 15 points.")