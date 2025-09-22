#Chapter 5 
#Exercise 5-9 No users 
usernames = ['silviaxp','XxPaper','jaden__','paperclipxX', 'admin','finalmouseXp']
#Add an if test to hello_admin.py to make sure the list of users is not empty 

if usernames:
    for username in usernames: 
        print(f"Hello {username}, thank you for loggin in again!")
else:
    print("We need to find some users!")
#if the list is empty, print the message "We need to find some users!"
print(usernames)

#------------------------------------- IMPORTANT----------------------------------------------------------------
#Remove all of the usernames from your list, and make sure the correct message is printed 
#When removing elements from a list during iteration using a for loop in Python, modifying the list directly 
# can lead to unexpected behavior due to index shifting. 
#To avoid this, it's recommended to iterate over a copy of the list or use alternative approaches like list 
#comprehension or the filter function

#Iterate over a copy 
#One safe approach is to iterate over a copy of the list, allowing modifications to the original list without 
#afecting the loop's behavior. This can be achieved using slicing to create a copy. 

for element in usernames[:]:
    if element in usernames:
        usernames.remove(element)
print(usernames)

#PRINT OUT THE EMPTY LIST CONDITION
if usernames:
    for username in usernames: 
        print(f"Hello {username}, thank you for loggin in again!")
else:
    print("We need to find some users!")