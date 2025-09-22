#Chapter 7 
#Exercise 7-6 Three Exists
#Write different version of either Exercise 7-4 or 7-5 that do each of the following at least once:

#Use a conditional test in the while statement to stop the loop 

#Use an active variable to control how long the loop runs 

#Use a break statement to exit the loop when the user enters a 'quit' value 


prompt = "Please enter your age to determine the price of the tickets: "
price = 0
flag = True
while flag:
    age = input(prompt)
    
    if age == 'quit':
        break 
  
    age = int(age)
        
    if age < 3:
        print("Ticket price is free.")
        flag = False
           
    elif (age >= 3) and (age <= 12):
        price = 10
        print(f"Ticket price is ${price}")
        flag = False
    elif age > 12:
        price = 15
        print(f"Ticket price is ${price}")
        flag = False
