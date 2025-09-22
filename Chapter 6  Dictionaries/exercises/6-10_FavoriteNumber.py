#Chapter 6
#Exercise 6-10 Favorite Number 
#Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
# Then print each person's name along with their favorite numbers.

favorite_numbers = {'silvia': [3,2,1],
                    'eustorgio': [3,77,88],
                    'gustavo': [10,30,23],
                    'diego': [24,1,79],
                    'alejandro': [0,22,4],
                    'ares': [6,5,8],
                    }


for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for user_number in numbers:
        print(f"\t{user_number}")
        
