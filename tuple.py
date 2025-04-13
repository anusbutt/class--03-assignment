# a built-in data types that lets us create immutable sequences of values

tuple = (1, 2, 3, 4, 5)
print(tuple)
# tuple[0] = 2 # not allowed

# tuple methods
# 1

tuple = (4, 43, 5, 23, 2)
index = tuple.index(23)  # Searches the tuple for a specified value and returns the position of where it was found
print(index)

# 2

tuple = (2, 4, 43, 2, 5, 23, 2)
count = tuple.count(2)  # Returns the number of times a specified value occurs in a tuple
print(count)