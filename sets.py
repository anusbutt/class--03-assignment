# set is the collection of unordered items
# each element in the set is must be unique and immutable 


set = {1, 2, 3, 4, 5}
print(set)

set2 = {1, 2, 2, 2}
print(set2)  # repeated elements stored only once, so it resolved to {1, 2}


# set methods
# 1
# adds an element
set = {1, 2, 3, 4, 5}
set.add(6)
print(set)

# 2
# removes the element
set = {1, 2, 3, 4, 5}
set.remove(3)
print(set)

# 3
# empties the set
set = {1, 2, 3, 4, 5}
set.clear
print(set)

# 4
# removes a random Value
set = {1, 2, 3, 4, 5}
set.pop()
print(set)


# set methods
# 1
# combine both set values and return new
set = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}
union = set.union(set2)
print(union)


# 2
# combines common values and return news
set = {1, 2, 3, 4, 5}
se2 = {1, 2, 3, 4, 5}
inter = set.intersection(set2)
print(inter)



#frozen set
# Freeze the list, and make it unchangeable

fruits = {"apple", "mango", "banana", "papaya"}
x = frozenset(fruits)
print(x)