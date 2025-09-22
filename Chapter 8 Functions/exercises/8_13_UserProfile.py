#Chapter 8 
# Exercise 8-13 User Profiles
#Start with a copy of user_profiles.py from page 148. Build a profile of yourself by calling build_profile().
# Using your first and last names and three other key-value pairs that describe you. 

def build_profile(first, last, **description):
    description['first name'] = first
    description['last name'] = last
    
    return description

user_profile = build_profile('silvia', 'saavedra', height="5'2", eye_color='brown', hair_color='black')

for key, value in user_profile.items():
    print(f"{key.title()}: {value}")