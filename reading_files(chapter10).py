# file_path = 'E:/Mastering Python/Python_projects/read_file.txt'
# with open(file_path) as my_file:
#     contents = my_file.read()
#     print(contents)  #rstrip method cuts the extra blank line in the output 


# file_path = 'E:/Mastering Python/Python_projects/read_file.txt'
# with open(file_path) as my_file:

    # for line in my_file:
    #     #print(line)
    #     print(line.rstrip()) #rstrip is used to remove unncesessary spaces between lines
    
    # alternative way
    
#     lines = my_file.readlines()

# for line in lines:
#     print(line.rstrip())

# all_text = ''
# for line in lines:
#     all_text += line.rstrip()
# print(all_text)


###### value of pi


# file_path  = 'E:/Mastering Python/Python_projects/pi.txt'

# with open(file_path) as my_file:
#     lines= my_file.readlines() # readlines method take each line from the file and stores it in a list. The list is then assigned to 'lines'

### if we want to print the list:

# for line in lines:
#     print(line.strip())

### if we want to build a single string containing all the digits in the file

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()  # += operator adds each line in lines to the variable pi_string and assigns the new variable with the same name pi_string
# print(pi_string) 
# print(len(pi_string))
# print(f"{pi_string[:30]}")

# ''' Is your birthday contained in pi?  '''

# birthday = input("Enter your birthday in mmddyy :")
# if birthday in pi_string:
#     print("Your birthday is in pi")
# else:
#     print("Your birthday is not in pi")


#### Writing to a text file

# file_path = 'E:/Mastering Python/Python_projects/read_file.txt'
# with open(file_path, 'a') as file_object:
#     file_object.write('I love programming \n')
#     file_object.write('I also love maths')
#     file_object.write('3221')

# my_guest = input("Please enter your name :")

# print(my_guest)

# file_path = 'E:/Mastering Python/Python_projects/guest.txt'
# active = True

# while active:
#     my_guest = input("Please enter your name :")
#     if my_guest == 'exit':
#         break

#     else:
#         print(my_guest)


#     with open(file_path, 'a') as file_object:
#         file_object.write( f'{my_guest}\n')




######### ZERODIVISIONERROR

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero")



# print('Give me two numbers I will divide them')
# print("Type 'q' to quit.")

# while True:
#     first_number = input("The first number is: \n")
#     if first_number == 'q':
#         break
    
#     second_number = input("The second number is: \n")
#     if second_number == 'q':
#         break
#     try:

#         answer = int(first_number)/int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by zero!")
    
#     else:
#         print(f"The answer is: {answer}")


# file_name = 'alice.txt'

# try:


#     with open(file_name, encoding='utf-8') as f:
#         contents= f.read()
# except FileNotFoundError:
#     print("This file is not found")


#### JSON

import json

numbers = [1, 2, 3, 4]

file_name = 'numbers.json'

with open (file_name, 'w') as f:
    json.dump(numbers, f)







































































































































































































































































































    