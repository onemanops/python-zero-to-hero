# Tuples

# Create a tuple containing three elements
point = (1, 2, 3)

# Access elements of a tuple using indices
x = point[0]  # x is 1
y = point[1]  # y is 2
z = point[2]  # z is 3

# Tuples can also be used to unpack values from iterables
numbers = (1, 2, 3)
a, b, c = numbers  # a is 1, b is 2, c is 3

# Tuples can be used as keys in dictionaries (since they are immutable)
coordinates = {(0, 0): 'origin', (1, 0): 'x-axis', (0, 1): 'y-axis'}
print(coordinates[(0, 0)])  # Output: "origin"
