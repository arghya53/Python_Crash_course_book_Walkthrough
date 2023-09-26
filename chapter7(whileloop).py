# name = input("Please enter your name:")
# print(f"Hello, {name} ")

# prompt = "If you see this message please feel free to response"
# prompt += "\nWhat's your name?"

# message = input(prompt)
# print(f'Hello! {message}')

# age = input("What's your age?")
# message_1 = int(age)
# print(f'\n aMy age is {message_1}')

# height = input("What's your height in inches?")
# height = int(height)
# if height >= 55:
# 	print("You are eligible for the ride")
# else:
# 	print("You need to be older")


# number = input("Enter a number, I will tell you even or odd:")
# number =  int(number)
# if number%2 == 0:
#     print(f"The number {number} is even")
# else: 
#     print(f"The number {number} is odd") 


# prompt = "Tell me your name, I will repeat it with you." # prompt is written to instruct the user what to do
# prompt += "The program will quit if you type'quit'."

# message = " "            # message requires a value to enter into while loop
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
 
# active = True  
# while active:         """ the active variable is set as flag to indicate whether the whole program is in active mode
                                #    here no comparison is made in the while statement"""


 
#     message = input(prompt)
 
#     if message == 'quit': # comparison is handled in this if statement instead of while

 
 
#         active = False
#     else:
#         print(message)


# prompt = " Enter the name of city. "
# prompt += " The program will stop if you type 'quit'."

# while True:
#     message = input(prompt)
#     #print(message)
#     if message == 'quit':

#         break
#     else:
#         print(f"I would love to go to the city {message}")


# current_number = 0
# while True:
#     if current_number < 10:

#         current_number += 1
#         if current_number % 2 == 0:
#             continue     # it means restart the loop from the begining avoiding the rest part of the code.
#                          # here we cannot use break instead of continue. Break will exit the loop immediately it finds 2 and won't restart.
#         print(current_number)
        

# prompt = "Tell me which topping you want to add in the pizza?"
# prompt += "\nThe program stops as long as you enter 'quit'."

# while True:
#     message = input(prompt)
#     if message == 'quit':
#         break
#     else:
#         print(f"You will add {message} to the pizza.")
# age = input("Please enter your age.")
    
# age= int(age)
# while True:
#     age = input("Please enter your age.")
    
#     age= int(age)
    
    
#     if age <= 3:
       
#         print("Your ticket is free.")
    
#     elif age>= 3 and age<= 12:
        
#         print("The ticket is $10")
    
#     else:
#         print("Your ticket is $15")
    
#     break
    

# unverified_users = ['dany', 'balde', 'sergio']
# verified_users= []

# print(f"Verifying users")
# while unverified_users:
#     current_user = unverified_users.pop()
#     print(current_user)
#     verified_users.append(current_user)
# print("\nThe following users are verified:")
# for users in verified_users:
#     print(users)



# pets = ['cats', 'dogs', 'pig', 'cow', 'goat', 'cats']
# pets.remove('cats') 
# print(pets)

""" Here the remove method will only eliminate the first instance but not all similar instances named 'cats'

 In order to remove all the instances, we should use remove method inside while loop."""
# while 'cats' in pets:
#     pets.remove('cats')
# print(pets)

"""while loop will loop through the list again and again till there is any instance 'cat'.

we can also use for loop to remove repeated instances in a list. But using while loop is wise to modify a list."""

# for pet in pets:
#     if pet == 'cats':
#         pets.remove(pet)
# print(pets)



# responses = {}
# polling_active = True
# while polling_active:
#     name = input("Please enter your name:")
#     response = input("What's your favorite place?")
#     responses[name] = response
#     message_1 = input("Do you want to nominate anyone. (yes/no)")
#     """print(message_1)"""
#     if message_1 == 'no':
#         print("\n The program is terminated")
#         polling_active = False
        
# print(" ---- Polling Result------")
# for name, response in responses.items():
#     print(f"\n {name.title()} would like to visit {response.title()}. ")
# print(responses)



















































