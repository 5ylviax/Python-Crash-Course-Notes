#Chapter 6 
#Exercise 6-5 Rivers 
#Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
#Use a loop to print a sentence about each river, such as "The Nile runs through Egypt"
rivers = {'nile': 'egypt',
          'mississippi river': 'USA',
          'River Severn': 'Uk',
          }
for river, country in rivers.items():
    print(f"The {river.title()} runs throuh {country.title()}.")
    
#Use a loop to print the name of each river included in the dictionary
for river in rivers.keys():
    print(f"{river.title()}")
    
#Use a loop to print the name of each country included in the dictionary 
for country in rivers.values():
    print(f"{country.title()}")

