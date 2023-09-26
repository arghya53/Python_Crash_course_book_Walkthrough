profile = {'father': 'businessman', 'age': 55, 'disease': 'diabetes'}
profile_f = profile['father']
print(f'My father is a {profile_f}')
profile['shop'] ='2S Service'
profile['dob'] = '2/7/1966'
del profile['disease']

data = profile.get('disease', '\nNo disease found')  # using get method to search any key in the dictionary and show a message if not found

data_1 = profile.get("father", "\n No father's job in the list")

print(data)
print(data_1)
print(profile)

profile_1 = {}
profile_1['mother'] = 'homemaker'
profile_1['age'] = 45
profile_1['disease'] = 'none'
print(profile_1)

alien_phase = {'x_position': 0, 'y_position': 10, 'speed': 'medium'}
print(f"\nOriginal position {alien_phase['x_position']}")
if alien_phase['speed'] == 'slow':
	x_increment = 1

elif alien_phase['speed'] == 'medium':
	x_increment = 2

else:
	x_increment = 3

alien_phase['x_position'] = alien_phase['x_position'] + x_increment
print(f"New position {alien_phase['x_position']}")


favorite_languages = {'rahim': 'c', 'karim': 'python', 'adam': 'java', 'smith': 'javascript'}

language = favorite_languages['smith']
print(f"\nSmith's favorite language is {language.title()}")


mother = {'first name' : 'snigdha', 'last name' : 'biswas', 'age' : 45, 'city' : 'chittagong'}

name_1 = mother['first name']
name_2 = mother['last name']
age = mother['age']
city = mother['city']

print(name_1.title(), name_2.title())
print(age)
print(city.title())


glossary = {'list' : 'It stores data', 'tuple' : "It stores data which can't be changed", 'method' : "It works on a variale to change it's shape"}
item_1 = glossary['list']
item_2 = glossary['tuple']
item_3 = glossary['method']

print(f'List: {item_1}. \nTuple: {item_2}. \nMethod: {item_3}. ')


users = { 
		'abiswas' : {'first': 'arghya',
					 'last': 'biswas',
					 'location': 'nalapara'},
		'aroy' :    {'first': 'aishwariya',
		             'last': 'roy',
		             'location': 'askar dighi'}
		}

for username, userinfo in users.items():

    print("\nUsername: " +  username)
    print("\t Full Name : " + userinfo['first'].title() + " " + userinfo['last'].title()) 
    print("\t Location : " + userinfo['location'].title())
    



user_0 = {'user_1' : {'username' : 'abiswas',
		  'first' : 'arghya',
		  'last' :  'biswas'},
		  'user_2' : {'username' : 'aroy',
		  'first' : 'aishi',
		  'last' : 'roy'}
		   }


for keys, values in user_0.items():
	print(keys)  # user_1 and user_2 are the keys of the dictionary user_0
	print('\tUsername :' + " " + values['username']) #
	print('\tFull name :' + values['first'].title() + " " + values['last'].title() ) # values['last'] indicates value of the key username in the dictionary user_0

# Looping through all key-value pairs

favorite_language = {'sarah' : 'c', 'reynold' : 'python', 'ryan' : 'java', 'aston' : 'javascript'}
	
for name, language in favorite_language.items():
	print(f"\n{name.title()}'s favorite language is {language.title()}.")



# Looping Through All the Keys in a Dictionary

for name in favorite_language.keys():
	print('\n' + name.title()) 


for name in favorite_language: # same as the above
	print('\n' + name.title()) 


# Looping Through All the values in a Dictionary

for language in favorite_language.values():
	print('\n' + language.title())


favorite_languages = { 'phil' : 'c', 
	                   'sarah' : 'java',
                       'foden' : 'python',
                       'adam' : 'javascript',
                       'phil' : 'java' }

for name, language in favorite_languages.items():
	print(name.title())

	friends = ['sarah', 'adam', 'smith']

	if name in friends:
		print(f'\tHi {name.title()} I see you love  {language.title()}')
   
#nested dictionaries

alien_0 = {'color': 'green', 'speed' : 'slow', 'points' : 5}
alien_1 = {'color' : 'red' , 'speed' : 'medium', 'points' : 1}
alien_2 = {'color' : 'blue', 'speed' : 'fast', 'points' : 3}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)

# DICTIONARIES inside a list

aliens = []

for alien_number in range (30): 
	new_alien = {'color': 'green', 'speed' : 'slow', 'points' : 5}
	aliens.append(new_alien)
#print(aliens[:5]) # here the command is showing a list(alien) with first five dictionaries or elements of it.

for alien in aliens[0:5]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15
for alien in aliens[0:10]:
	print(f'{alien}') # here the command is showing first five dictionaries/elements separately from the list

print(f"Total number of aliens: {len(aliens)}")



# storing list in a dictionary

relatives_location = {'askar dighi': 'aishi', 'north nalapara' : ['didi', 'mashi', 'pishi'] }


print(f"I want to visit {relatives_location['askar dighi']}")

print(f"In north nalapara I want to visit the following places:") 
for relatives in relatives_location['north nalapara']:

	print(relatives.title())



# aishi_favs = ['bali', 'california', 'singapore']
# akshay_favs = ['bankok', 'ibiza', 'kashi']

favorite_places = {'arghya' : {'place_1':'pataya', 'place_2': 'madrid', 'place_3': 'kedarnath'},
                   'aishi'  : ['bali', 'california', 'singapore'],
                   'akshay' : ['bankok', 'ibiza', 'kashi']}
print('The favorite places of the following people are:')

for name, places in favorite_places.items():
	if name == 'arghya':
		
		print(f"I am {name.title()} and I want to visit {places['place_1']} first.")
	else:
		print(f" I am {name.title()} and I want to visit ")

		for places in favorite_places[name]:
			print('\t' + places.title() )




































































































