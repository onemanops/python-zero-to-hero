# Dictionaries: aka "dicts," are used to store and manipulate key-value pairs. 

my_dict = {'key1': 'value1', 'key2': 'value2'}

# create a dictionary
person = {'name': 'John', 'age': 30, 'location': 'New York'}

# access values using keys
print(person['name'])  # prints 'John'
print(person['age'])   # prints 30

# add a new key-value pair to the dictionary
person['profession'] = 'software developer'

# update a value in the dictionary
person['location'] = 'San Francisco'

# remove a key-value pair from the dictionary
del person['age']

print(person)  # Output: {'name': 'John', 'location': 'San Francisco'}

# Remove the key-value pair with key 'key1' and store the value in a variable
removed_value = my_dict.pop('key1')

print(my_dict)  # Output: {'key2': 'value2'}
print(removed_value)  # Output: 'value1'

# Remove all key-value pairs from the dictionary
my_dict.clear()

print(my_dict)  # Output: {}

