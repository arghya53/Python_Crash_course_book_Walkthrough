def build_profile(first, last, **user_info): # here we have introduced an empty dictionary named 'user_info' which can take arbitrary no of keys and values

    user_info['first name'] = first #In the body of build_profile(), we add the first and last names to the user_info dictionary because we’ll always receive these two pieces of information from the user u, and they haven’t been placed into the dictionary 
                                     #yet. Then we return the user_info dictionary to the function call line.
    user_info['last name'] = last
    return user_info

# profile = build_profile('Karim', 'Benzema', location = 'Madrid', team = 'real madrid')
# print(profile)

# def build_phone(brand, model, **mobile_info):

#     mobile_info['brand name'] = brand
#     mobile_info['model name'] = model
#     return mobile_info

# my_phone = build_phone('google', 'pixel 7', ram = '8/128', camera = '10 MP')
# print(my_phone)