#Chapter 7 
#Exercise 7-10 Dream Vacation
#Write a program that polls users about their dream vacation. 
#Write a prompt similar to "If you could visit one place in the world, where would you go? "
#Include a block of code that prints the results of the poll. 
dream_vacations = {}

active = True
while active:
    name = input("\nWhat is your name? ").strip()
    location = input("If you could visit one place in the world, where would you go? ").strip()
    
    dream_vacations[name] = location
    
    repeat = input("Would you like to let another person respond? (yes/no) ").strip()
    
    if repeat.lower() == 'no':
        active = False
        
print("\n---Poll Results ---")

for name, location in dream_vacations.items():
    print(f"{name.title()} would like to vist {location.title()}.")
    