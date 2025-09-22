#Chapter 8
#Exercise 8-5 Cities 
#Write a function called describe_city() that accepts the name of a city and its country. 
#The function should print a simple sentece, such as "Reykjavik is in Iceland". 
# give the parameter for the country a default value
#Call your function for three different cities, at least one of which is not in the default country.  


def describe_city(city, country='U.S.A'):
    print(f"{city.title()} is in {country.title()}.")
    
describe_city('chicago')

describe_city(city='north carolina')

describe_city(country='japan', city='tokyo')
    