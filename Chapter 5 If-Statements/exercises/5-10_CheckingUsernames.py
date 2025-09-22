#Chapter 5 
#Exercise 5-10 Checking Usernames

#Do the following to create a program that stimulates how websites ensure that everyone has a unique username. 

#make a list of five or more usernames called current_users 
current_users = ['john','smith','patterson','walker','saavedra']

#make another list of five usernames called new_users. Make sure one or two of the new names are also in the current_users list 
new_users = ['walker','saavedra','bolton','hughes','white']
# Loop through the new_users list to see if each new username has already been used.
for user in new_users:
    if user.lower() in current_users[:]:
        print(f"Enter a new username {user}:")
    else:
        print(f"Username available: {user}.")
#If it has, print a message that the person will need to enter a new username.
#if a username has not been used, print a message saying "that the username is available"

#Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. 
#(To do this, you'll need to make a copy of current_users containing the lowercase version of all existing users.)