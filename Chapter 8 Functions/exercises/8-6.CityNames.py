#Chapter 8 
#Exercise 8-6 City Names 
#Write a function called city_country() that takes in the name  of a city and its country. 
#The function shold return a string formatted like this: 
# "Santiago, Chile"
#Call your function with at least three city-country pairs, and print the values that are returned 

def city_country(city,country):
    formatted = f"{city}, {country}"
    
    return formatted.title()

formatted_pair = city_country('st. louis', 'U.S.A')
print(formatted_pair)

formatted_pair = city_country('tokyo', 'japan')
print(formatted_pair)

formatted_pair = city_country('madrid', 'spain')
print(formatted_pair)