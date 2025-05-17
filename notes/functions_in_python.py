# Functions in python
# Types of function ---
"""
1. Built-in function
2. User defined function
3. lambda function
"""

# User defined function
# the function will not take any input and it will return nothing
def addtion():
    a = 20
    b = 30 
    print(a+b)

addtion()

# The function which can take input and it will not return anything
def addtion1(a,b):
    print(a+b)

addtion1(30,40)

# The function which can not take any input and it will return something
def addtion2():
    a = 10
    b = 80

    return a+b

res = addtion2()
print(res)

# The function which can take input and it will return something
def addtion3(a,b):
    return a+b

res1 = addtion3(90,20)
print(res1)


