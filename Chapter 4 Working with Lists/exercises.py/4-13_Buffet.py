#Chapter 4 
#Exercise 4-13
#Buffet
#A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store then in a tuple 

foods = ('oatmeal','omelette', 'burrito','pancakes','waffles')
#Use a for loop to print each food the restuarant offesr 

for food in foods: 
    print(food.title())
#Try to modify one of the items, and make sure that Python rejects, the change

# error ---> foods[0] = 'scramble eggs'

#The restuarant changes it menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the line 
#on the revised menu.


foods = ('french toast','omelette', 'breakfast burrito','pancakes','waffles')
for food in foods:
    print(food)
