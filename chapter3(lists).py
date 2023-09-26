# bicycles=['trek', 'jason', 'phoenix', 'blade', 'mountain']
# message=f'My first bicycle was {bicycles[0].title()}.'
# print(message)
# print(bicycles)
# bicycles[0]='martin' # modifying an element of list
# print(bicycles)
# bicycles.append('demian') # adding a value to list
# print(bicycles)

# # inserting element in an empty list

# motorcycles=[]
# motorcycles.append('honda')
# motorcycles.append('royal enfield')
# motorcycles.insert(1,'ducati')
# motorcycles.insert(3,'suzuki') #insert adds an element at any position
# motorcycles.append('yamaha')
# motorcycles.append('scooti') #append adds an element at the end 
# print(motorcycles)


# popped_bicycles=bicycles.pop() #pop removes the last element of a list by default
# print(bicycles)

# too_expensive= 'yamaha'
# motorcycles.remove(too_expensive) #use this method when you know the entry but not its position
# print(motorcycles)
# print(f"\tA {too_expensive.title()} is very expensive for me.")

locations = ['dhaka', 'istanbul', 'moscow', 'usa', 'amsterdam', 'tokyo', 'canberra', 'singapore', 'delhi']
print(sorted(locations)) # sorted is a function
print(sorted(locations, reverse=True)) #reversing a list
locations.sort()  # sort is a method
print(locations)
locations.sort(reverse=True) # reversing a list with sort method
print(locations)
print(len(locations))