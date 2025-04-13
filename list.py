# a built-in data type that stores set of values
# it can store elements of different types(integers, floatm string, etc)

cars = ["corolla", "civic", "audi", "mercedez"]
cars[1] = "elantra"    # allowed in python because lists are mutable 
print(cars)
print(len(cars))    # you also can check the lenght

# list slicing

marks = [45, 78, 98, 47, 67, 97]
print(marks[0:5])  # it returns [45, 78, 98, 47, 67]
print(marks[:5])  # same as previous [45, 78, 98, 47, 67]
print(marks[0:])  # it returns full list
print(marks[-3:-1]) # its returns [47, 67]

# list methods

list = [1, 2, 3, 4, 5]
list.append(6) # add one element at the end 
print(list)

list = [3, 2, 1, 4, 5]

list.sort()  # sorts in ascending order
print(list) 

list.sort(reverse=True)  # sort in descending order
print(list)

list.reverse() # reverses list
print (list)

list.insert(3, 8)  # insert element at index (idx, el)
print(list)

# methods of lists

list = [1, 2, 3, 4, 5]
list.remove(1)   # remove first occurence of the element
print(list)

list = [1, 2, 3, 4, 5]
list.pop(3)
print(list)  # removes element at index
