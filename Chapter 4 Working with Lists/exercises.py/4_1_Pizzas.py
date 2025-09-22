#chatper 4 Exercise 4-1 Pizzas 
#Think of at least threekinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of the pizza
pizzas = ['pepperoni','sausage', 'pineapple','supreme']
print("These are my favorite type of pizzas: ")
for pizzaType in pizzas:
    print(f"{pizzaType.title()}")
print("\n")
#Modify your for loop to print a sentece using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should
# have one line of output containing a simple statement like "I like pepperoni pizza."
for pizzaType in pizzas:
    print(f"I like {pizzaType} pizza")
print("\n")

#Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consit of three or more lines about the kinds
#of pizza you like and then an additional sentence, such as "I really love pizza"!
print("I really like pizza, that I eat pizza weekly on Fridays")
    
    