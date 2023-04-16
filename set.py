# Sets:

numbers = [1, 2, 3, 4, 5, 1, 4, 4]

# Create a set from a list
unique_numbers = set(numbers)  # unique_numbers is {1, 2, 3, 4, 5}

# Check if an element is in a set
print(4 in unique_numbers)  # Output: True
print(6 in unique_numbers)  # Output: False

# Perform set operations
evens = {2, 4, 6, 8, 10}
odds = {1, 3, 5, 7, 9}
primes = {2, 3, 5, 7}

# Union (elements in either set)
print(evens | odds)  # Output: {2, 4, 6, 8, 10, 1, 3, 5, 7, 9}

# Intersection (elements in both sets)
print(evens & primes)  # Output: {2}

# Difference (elements in the first set but not the second)
print(evens - primes)  # Output: {4, 6, 8, 10}
