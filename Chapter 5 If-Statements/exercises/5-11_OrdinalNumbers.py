#Chapter 5 
#Exercise 5-11 Ordinal Numbers
#Ordinal: like "first", "second", and "third", indicate position or order within a sequence .
#Ordinal Numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in t, except 1, 2, and 3 

#Store the numbers 1 through 9 in a list 
num_List = list(range(1,10))

#Loop through the list
#Use an if-elif-else chain inside the loop to print the paper ordinal ending for each number. Your output should read
# "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line .
for num in num_List:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")

