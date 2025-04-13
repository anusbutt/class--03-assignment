# dictionaries are used to store data values in key:value pairs
# they are unordered,mutable and dont allow duplicate keys

dict = {
    "name": "anus",
    "education": "intermediate",
    "age": 19,
    "marks": [23, 45, 76, 87],
    "isregular": True
}
print(dict)

# nested dictionaries

dict = {
    "name": "anus",
    "education": "intermediate",
    "age": 19,
    "marks": {
        "math": 89,
        "physic": 91,
        "chemistry": 90
    },
    "isregular": True
}
print(dict)

# dictionary methods
# 1
# return all keys
dict = {
    "name": "anus",
    "education": "intermediate",
    "age": 19,
    "marks": [23, 45, 76, 87],
    "isregular": True
}
keys = dict.keys()
print(keys)

# 2
# return all values
dict = {
    "name": "anus",
    "education": "intermediate",
    "age": 19,
    "marks": [23, 45, 76, 87],
    "isregular": True
}
values = dict.values()
print(values)

# 3
# return all pairs
dict = {
    "name": "anus",
    "education": "intermediate",
    "age": 19,
    "marks": [23, 45, 76, 87],
    "isregular": True
}
items = dict.items()
print(items)

# 4
# returns the key according to values
dict = {
    "name": "anus",
    "education": "intermediate",
    "age": 19,
    "marks": [23, 45, 76, 87],
    "isregular": True
}
keyValue = dict.get("age")
print(keyValue)

# 5
# inserts the specified items to the dictionary
dict = {
    "name": "anus",
    "education": "intermediate",
    "age": 19,
    "marks": [23, 45, 76, 87],
    "isregular": True
}
dict.update({"fathername": "yousuf butt"})
print(dict)