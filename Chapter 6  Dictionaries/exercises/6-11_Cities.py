#Chapter 6 
#Exercise 6-10 Cities 
#Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and 
# include the country that the city is in, its approximately population, and one fact about that city. The keys for each city's dictionary
#should be something like 'country', 'population', and 'fact'. Print the name of each city and all of the information you have stored about it.

cities = {
    'chicago': {
    'country': 'usa',
    'info1' : 'noisey',
    'info2': 'crime rate is high',
    'info3': 'it gets very cold in the winter',
    'population': '2.664 million',
    },
    
    'los angeles': {
        'country': 'usa',
        'info1': 'expensive',
        'info2': 'traffic is bad',
        'info3': 'near the ocean',
        'population': '9.663 million'
    },
    'st. louis': {
        'country': 'usa',
        'info1': 'tax is alot',
        'info2': 'next to a river',
        'info3': 'The Gateway Arch is the monument of St. Louis.',
        'population': '281,754'
    }
}

for city_name, city_info in cities.items():
    print(f"Five facts about {city_name.title()} are: ")
    print(f"\t{city_name.title()} is in the {city_info['country'].upper()}")
    print(f"\t{city_info['info1'].capitalize()}")
    print(f"\t{city_info['info2'].capitalize()}")
    print(f"\t{city_info['info3']}")
    print(f"The population is approximately: {city_info['population']}\n")