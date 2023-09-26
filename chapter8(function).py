""" Calling a function """
# def person(name, complexion, height):
#     print(f"I know a person named {name}, whose complexion is {complexion} and of height {height} inches.")

# person('Mike', 'black', 36.5) # here the order of values for the the keywords matter
# person(complexion='white', name= 'Harry', height= 55) # here the order of keyword arguments doesn't matter

# def person_name(first_name, last_name):
#     full_name = (f"{first_name} {last_name}")
#     return full_name

# formatted_name = person_name('arghya', 'biswas')
# print(formatted_name)



# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = (f"{first_name} {middle_name} {last_name}")
#     else:
#         full_name = (f"{first_name} {last_name}")
    
#     return full_name.title()    # return statement returns the value to the function when it is called. Here in the next two lines
# formatted_name = get_formatted_name('Arghya', 'biswas')
# print(formatted_name)

# formatted_name = get_formatted_name('Jim', 'Carter', 'Lee')
# print(formatted_name)


# def person(first_name, last_name):
#     """ Returning a dictionary of information about the person """
#     person_1 = {'first' : first_name, 'last': last_name}
#     return person_1

# me = person('Arghya', 'Biswas')
# print(me)


# def person_info(first_name, last_name, age= None):
#     """ returning a dicionary of info about the person """
#     person= {'first':first_name, 'last':last_name}

#     if age:                         # it means if age has a value then include a key named age with a value 'age' in the dictionary 'person'. 
#         person['age'] = age
#     return person

# singer = person_info('Arghya', 'Biswas', 27)
# print(singer)


# def get_formatted_name(first_name, last_name, middle_name= None):
#     """returning a dictionary of info about the person"""
    
#     person = {'first': first_name, 'last': last_name}

#     if middle_name:
#         person['middle']= m_name
#     return person

# while True:
#     print("Please enter 'q' anytime to quit.")
#     f_name = input("What's your first name?")
#     if f_name == 'q':
#         break
    
#     l_name = input("What's your last name?")
#     if l_name == 'q':
#         break
    
#     m_name = input("What's your middle name?")
    
#     full_name = (f"{f_name} {m_name} {l_name}")
    
#     singer = get_formatted_name(f_name, l_name, m_name)
    
#     print(singer)
#     print(full_name)



#passing a list in a function

# def invited_persons(names):

#     for name in names:
#         print(f"Hello {name.title()} you are invited in my party")

# usernames = ['jason', 'hannah', 'mary', 'sean']
# invited_persons(usernames)


# Modifying a list in a Function

""" We have a  list of undone activities and we are making a list of the activities which we have already done from the undone activities  """

""" We can do it in the following two ways """

""" First: Using While Loop """
# incomplete_activities = ['hiking', 'skiing', 'mountain biking', 'photography', 'freelancing', 'coding', 'mailing', 'hacking']
# completed_activities = []

# while incomplete_activities:
#     current_activity = incomplete_activities.pop()
#     print(f"The activities currently I am doing are {current_activity}")
#     completed_activities.append(current_activity)
# print(completed_activities)

# print("---The following activites are done finally----")

# for activity in completed_activities:
#     print(activity)


# """ Next: We can do the same task using function """

# def all_tasks(incomplete_activities, completed_activities):

#     while incomplete_activities:
#         current_activities = incomplete_activities.pop()
#         print(f" Currently I am doing these {current_activities}.")
#         completed_activities.append(current_activities)

# def finished_tasks(completed_activities):
#     print("----The following activities are completed----")
#     for activity in completed_activities:
#         print(activity)

# incomplete_activities = ['hiking', 'skiing', 'mountain biking', 'photography', 'freelancing', 'coding', 'mailing', 'hacking']
# completed_activities = []

# all_tasks(incomplete_activities[:], completed_activities); """ The [:] sign will prevent emptying the original list and it will print a copy of orginal list 'incomplete_activities' """
# print(incomplete_activities)
# print(completed_activities)



# def pizza(size, *toppings):

#     print(f"I want the pizza of {size} inches with")
#     for topping in toppings:
#         print(topping)

# pizza(12, 'mushroom', 'coconut', 'sausage', 'chutney' )

def build_profile(first, last, **user_info): # here we have introduced an empty dictionary named 'user_info' which can take arbitrary no of keys and values

    user_info['first name'] = first # In the body of build_profile(), we add the first and last names to the 
                                    # user_info dictionary because we’ll always receive these two pieces of 
                                    # information from the user u, and they haven’t been placed into the 
                                    # dictionary yet. Then we return the user_info dictionary to the function call line.
    user_info['last name'] = last
    return user_info

profile = build_profile('Karim', 'Benzema', location = 'Madrid', team = 'real madrid')
print(profile)

def build_phone(brand, model, **mobile_info):

    mobile_info['brand name'] = brand
    mobile_info['model name'] = model
    return mobile_info

my_phone = build_phone('google', 'pixel 7', ram = '8/128', camera = '10 MP')
print(my_phone)


































    


























