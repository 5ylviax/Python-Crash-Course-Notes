#Chapter 7 
#Exercise 7-5 Movie Tickets
# A movie theater charges different ticket prices depending on a person's age. 
# If a person is under the age of 3, the ticket is free; 
# if theya re between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
#Write a loop in which you ask users their age, and then tell them the cost of their moveie ticket. 


prompt = "How old are you?"
prompt = "Please enter your age to determine the price of the tickets: "
price = 0
while True:
    age = input(prompt)
    age = int(age)
    if age < 3:
        print("Ticket price is free.")
           
    elif (age >= 3) and (age <= 12):
        price = 10
        print(f"Ticket price is ${price}")

    elif age > 12:
        price = 15
        print(f"Ticket price is ${price}")
    break

        