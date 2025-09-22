#Chapter 7 
#Exercise 7-4 Pizza Topping 
#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
#As they enter each  topping, print a message saying you'll add that topping to their pizza. 

toppings = []

prompt = "Please enter the name of the pizza topping:"
prompt += "\nEnter 'quit' when you are finished.\n"

while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(f"\t{message.title()} will be added to your pizza.")
        toppings.append(message)

print("\nYour toppings are:")
for topping in toppings:
    print(f"\t{topping.title()}")