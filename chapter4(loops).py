magicians=['hector', 'victor', 'sherlock', 'feluda']
for magician in magicians:
    print(magician.title(), f'that was a great trick')
    print(f"Congratulations! {magician.title()} for your show!\n") # indented, so executed inside the loop
print("That was a great show.")  #unindented, so executed outside the loop

squares=[]
for value in range(1,10):
	squares.append(value**3/2)
print(squares)

# list cpmprehension
# inside the square bracket first define the expression for the values you want 
# to store in the new list Then, write a for loop to generate the numbers you 
# want to feed into the expression
# squares=[value**2 for value in range(1,10)]
# print(squares)

# printing a list of numbers between 1 to 20 inclusive
# numbers=[value for value in range(1,21)]  
# print(numbers) # task 4-3

# printing a list of infinite numbers

# numbers=[]
# for value in range(1,1000000):
# 	numbers.append(value)
# print(numbers) #task 4-4
# summation = sum(numbers) 
# print(summation) # task 4-5
# print(min(numbers))
# print(max(numbers))

# #make a list of the odd numbers from 1 to 20.
# numbers_1=[]
# for value in range(1,21,2):
# 	numbers_1.append(value)
# print(numbers_1)

# #Make a list of the multiples of 3 from 3 to 30
# numbers_2=[]
# for value in range(3,33,3):
# 	numbers_2.append(value)
# print(numbers_2)

# numbers_3=[]
# for value in range(1,11):
# 	numbers_3.append(value**3)
# print(numbers_3)

# #list comprehension

# numbers_3=[value**3 for value in range(1,11)]
# print(numbers_3)


# players=['martin', 'helix', 'john', 'jessie', 'ronaldo', 'hazard']

# print('Here are my list of first 3 players:')

# for player in players[:3]:
# 	print(player.title())

# foods.py
# copying items from a list to another
# my_food= ['pizza', 'burger', 'cola', 'mirinda']
# my_friend_food=my_food[:]
# my_friend_food.append('sandwich')
# my_food.insert(2, 'pasta')
# print('This is my food',my_food)
# print("This is my friend's food",my_friend_food)

# tuples

# friends=('arafat', 'mushfique', 'hasnat', 'zihad')
# for friend in friends:
# 	print(friend)
# friends.append('argha')
	
