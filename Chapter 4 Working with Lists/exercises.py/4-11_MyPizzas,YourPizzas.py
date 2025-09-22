#Chapter 4 
#Exercise 4-11
#My Pizzas, Your Pizzas 
# Start with you program form Exercise 4-1 (pg 56).
my_pizzas = ['pepperoni', 'sausage','cheese']
#Make a copy of th list of pizzas, call it friend_pizzas. Then, do the following:
friend_pizzas = my_pizzas[:]

# Add a new pizza to the original list
my_pizzas.append('supreme')
# Add a different pizza to the list friend_pizzas
friend_pizzas.append('meat lovers')

#Prove that you have two separate lists. Print the message "My favorite pizza are :, and then use a for loop to print the first list. Print the message "My 
#friend's favorite pizzas are :, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
print("\nMy favorite pizzas are: ")
for pizza in my_pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
    
