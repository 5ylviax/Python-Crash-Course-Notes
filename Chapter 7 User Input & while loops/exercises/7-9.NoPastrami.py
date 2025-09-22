#Chapter 7 
#Exercise 7-9 No Pastrami 
#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list 
# three times.  Add code near the beginnig of your program to print a message saying the deli has run out 
#of pastrami, and the use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami
#sandwiches end up in finished_sandwiches. 

sandwich_orders = ['pastrami','pastrami','ham', 'turkey', 'pastrami', 'italian', 'chicken salad']
finished_sandwiches = []

print("Deli has run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
 
# Display final lists clearly
print("\nSandwich orders remaining:", sandwich_orders)
print("Finished sandwiches:", finished_sandwiches)
    