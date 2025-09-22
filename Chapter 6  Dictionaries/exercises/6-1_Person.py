#Chapter 6
#Exercise 6-1 Person
# Use a dictionary to store information about a person you know.
#Store their first name, last anme, age, and the city in which they live. 
#You should have keys such as first_name, last_name, age, and city.

person  = {'first_name': 'silvia', 
           'last_name': 'saavedra',
           'age': 26,
           'city': 'FH',
           }

#Print Each piece of information stored in our dictionary
print(f"{person['first_name'].title()} {person['last_name'].title()} is {person['age']} years old and lives in {person['city'].title()}")