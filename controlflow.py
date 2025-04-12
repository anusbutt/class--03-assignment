# Control flow refers to the order in which statements are executed in a program. In Python, decision-making is achieved using if, elif, and else statements, along with comparison and logical operators.

# example 1

num = 7
if(num > 5):
    print("the number is greater than five")

# example 2
    
num = 7
if(num > 5):
    print("number is greater than five")
else:
    print("the number is less than 5")

# example 3
    
num = 5
if(num > 5):
    print("number is greater than 6")
elif(num == 5):
    print("number is equal to 5")
else:
    print("the number is less than 5")

# example 4
    
age = 81
if(age >= 18 and age <= 60 ):
    print("you are eligible for driving")
else:
    print("you are not eligible for driving")


# example 5
    
age = 15

if(age >= 18):
    if(age <= 30):
        print("you are eligible for army test")
    else:
        print("you are not eligible")
else:
    print("you will be allowed after 18")

    
