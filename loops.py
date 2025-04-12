# there are two loops in python which is used very commonly
# while loop
# for loop
# loops are used to repeat instructions

# while loops
a = 1
while a <= 5:
    print(a)
    a += 1

# example 2
    
a = 1
while a <= 5:
    print(a)
    if(a == 3):
        break
    a += 1

# example 3
a = 1
while a <= 5:
    print(a)
    a += 1
    if(a == 3):
        continue


# for loop

names = ["onion", "potato", "cocumber"]
for veg in names:
    print(veg)

# example 2
    
names = ["onion", "potato", "cocumber"]
for veg in names:
    if veg == "potato":
        break
print(veg)

# example 3
    
names = ["onion", "potato", "cocumber"]
for veg in names:
    if veg == "potato":
        continue
print(veg)

# range

for x in range(6):
    print(x)

# example 2
    
for x in range(6):
    if x == 4:
        break
    print(x)

    
# example 3
    
for x in range(6):
    if x == 4:
        continue
    print(x)

# example 4
# it will print even number from 2 to 10
for x in range(2, 11, 2): #(start, stop, step)
     print(x)

# example 5
# for empty loop
     
for x in [1, 2, 3]:
    pass