#Chapter 6 
#Exercise 6-7 People:
#Start with the program you wrote for Exercise 6-1 (pg. 98). Make two new dictionaries representing different peple, and store all
#three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person 

person_0 = {
    'first_name': 'silvia', 
    'last_name': 'saavedra',
    'age': 26,
    'city': 'FH',
    }
person_1 = {
    'first_name': 'ares',
    'last_name': 'santiago',
    'age': 8,
    'city': 'FH',
    }
person_2 = {
    'first_name': 'robert',
    'last_name': 'patterson',
    'age': 30,
    'city': 'unkown',
}

people= [person_0, person_1, person_2]


for person in people:
    print(f"Firstname: {person['first_name'].title()}")
    print(f"LastName: {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")
    