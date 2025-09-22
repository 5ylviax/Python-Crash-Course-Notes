#Chapter 6
#Exercise 6-9 Favorite Places 
#Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for 
#each person. To makes this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
favorite_places = {
    'silvia': ['romania', 'japan','korea'],
    'clara': ['japan','germany', 'usa'],
    'turner': ['florida', 'california', 'new york'],
}
#Loop through the dictionary, and print each person's name and their favorite places

for name, places in favorite_places.items():
    print(f"{name.title()} favorite places are: ")
    for place in places:
        print(f"\t{place.title()}")
