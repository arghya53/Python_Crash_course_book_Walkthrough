# class Dog:

#     """ Defining a class called Dog """
#     def __init__(self, name, age):  ### here, (name and age) are attributes
#         self.name = name
#         self.age = age

#     def sit(self):                     ### it is a method
#         print(f"{self.name} is sitting")
#     def roll(self):
#         print(f"{self.name} is rolling")
# my_dog = Dog('husky', 5)                    # here, my_dog is an instance of the class Dog
# print(f"My dog's name is {my_dog.name} and it is {my_dog.age} years old")
# my_dog.sit()
# my_dog.roll()
# my_dog = Dog('Shepherd', 6)
# print(f"My dog's name is {my_dog.name} and it is {my_dog.age} years old")
# my_dog.sit()
# my_dog.roll()

 

# class Restaurant():
#     """ Initiating a class restaurant """
#     def __init__(self, name, cuisine):
#         self.name = name
#         self.cuisine = cuisine
#         self.number_served = 0
    
#     def describe_restaurant(self):
#         print(f"The name of our restaurant is {self.name}.")
#         print(f"{self.cuisine} is our signature cuisine. ")
    
#     def open_restaurant(self):
#         print(f"Our {self.name} is open now.")
    
#     def customer_numbers(self):
#         print(f"The number of customers served is {self.number_served}")
    
#     def number_served(self, number):
#         self.customer_numbers = number
    
#     def incerment_number_served(self, incremented):
#         self.number_served += incremented 
    

# restaurant = Restaurant("Sultan's Dine", 'Kacchi')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# restaurant.number_served = 20
# restaurant.customer_numbers()
# # restaurant.number_served = 50
# restaurant.incerment_number_served(100)
# restaurant.customer_numbers()


# class IceCreamStand(Restaurant):

#     ''' Initiating a subclass IceCreamStand '''
#     def __init__(self, name, cuisine):
#         super().__init__(name, cuisine)
#         self.flavor = ['vanilla', 'mango', 'chocolate', 'mixed fruit' ]

#     def flavors(self):
#         print(f"Among all the flavors I prefer {self.flavor[:]} the most.")

# fav_flavor = IceCreamStand('Icecream Parlour', 'icecreams')
# fav_flavor.describe_restaurant() 
# fav_flavor.flavors()




# class Sushi:
#     """ Defining the aspects of sushi """
    
#     def __init__(self, price= 55):
#         self.price = price
    
#     def describe_sushi(self):
#         print(f"The price of sushi is {self.price}")

#     def get_range(self):
#         if self.price <= 55:
#             print("The sushi is small")

#         else:
#             print('The sushi is large')

        
# class Chinese_restaurant(Restaurant):
#     """ Represents aspects of car specific to electric vehicles """
#     def __init__(self, name, cuisine):
#         super().__init__(name, cuisine) # super means the parent is denoted as superclass and daughter as subclass
#         self.chinese_people = 5  # adding new attribute to the child class
#         self.sushi = Sushi()
    
#     def people(self):
#         """ Print a statement describing amount of people ."""
#         print(f"The amount of chinese people in the restaurant is {self.chinese_people} ")


# my_dish = Chinese_restaurant('Zouk', 'Sushi')
# print(my_dish.describe_restaurant())
# my_dish.people()
# my_dish.sushi.describe_sushi()   # in order to call the method "describe_sushi", at first I need to call the attribute "sushi"
# my_dish.sushi.get_range()         # in order to call the method "get_range", at first I need to call the attribute "sushi"


# class Mobile:
#     """ Initializing class Car """
#     def __init__(self, maker, model, year):
#         self.maker = maker       # this attribute 'maker' takes a value from instance at line 56 and assigns it to self.maker
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def car_description(self):
#         full_description = f"{self.maker} {self.model} {self.year}"
#         return full_description.title()
    
#     def read_odometer(self):
#         print(f"The odometer reading is {self.odometer_reading} miles.")
    
#     def update_odometer_reading(self, mileage):
#         if mileage >= self.odometer_reading:

#             self.odometer_reading = mileage
#         else:
#             print("You can't roll the odometer value")       
    
#     def increment_reading(self, miles):
#         self.odometer_reading += miles
        

# full_name = Mobile('Google', 'Pixel 7', 2022)  # the attributes are taking values from the instance
# print(full_name.car_description())
# full_name.read_odometer()

# full_name.odometer_reading = 25  # editing the value of attribute by directly accessing it
# full_name.read_odometer()

# full_name.update_odometer_reading(20)
# full_name.read_odometer()

# full_name.increment_reading(100)
# full_name.read_odometer()

# class Privileges:
#     def __init__(self):
#         self.privileges = ['can add post', 'can delete post', 'can ban user']

#     def show_privileges(self):
#         print("The privileges of the user are: ")
#         for privilege in self.privileges:

#             print( f"{privilege}" )

# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
    
#     def user_details(self):
#         print(f"The user name is {self.first_name} {self.last_name} ")
        

# class Admin(User):
#     def __init__(self, first_name, last_name):
#         super().__init__(first_name, last_name)
#         self.privileges = Privileges()


# user_id = Admin('Arghya', 'Biswas') # it is the daughter class of parent User
# user_id.user_details()

# user_id.privileges.show_privileges() # it is showing Admin's privileges


# from random import randint    
# class Die:
#     ''' Initiating the class Die '''
#     def __init__(self, sides=6):
#         self.sides = sides

#     def roll_die(self):
        
#         rand_num = randint(1, self.sides) 

#         print(rand_num)   

# from random import randint

# class Die:
#     ''' Initiating the class Die '''
#     def __init__(self, sides=6):
#         self.sides = sides

#     def roll_die(self):
#         rand_num = randint(1, self.sides) 
#         print(rand_num)

# my_die = Die()
# my_die.roll_die()


    


        









