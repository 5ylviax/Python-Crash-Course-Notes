#Chatper 7
#Exercise 7-3 Multiple of Ten
#Ask the user for a number, and then report whether the number is a multiple of 10 or not
number = input("Enter a number, and I'll tell you if it is a multiple of 10 or not ")
number = int(number)

if number % 10 == 0: 
    print(f"Yes, the number {number} is a multiple of 10.")
else:
    print(f"No, the number {number} is not a multiple of 10. ")