'''
Syntax	                            Meaning	                            Result type
a, b = [10, 20]	            Unpack values into variables	           Individual values
a, *b = [10, 20, 30]	    Collect remaining values	                 b is a list
*args	                    Pack positional arguments	                   Tuple
func(*values)	        Unpack iterable into arguments	                Positional arguments
**kwargs	            Pack keyword arguments	                            Dictionary
func(**data)	    Unpack dictionary into keyword arguments	        Keyword arguments

Remember: * is used with iterables such as lists and tuples,
while ** is used with dictionaries when passing keyword arguments.
During unpacking, the number and names of the arguments must match the function's parameters
unless the function allows extra arguments.

'''



#List packing and unpacking

# 1: Basic list unpacking

a, b, c = [1, 2, 3]

print(a)
print(b)
print(c)

# OUTPUT:
# 1
# 2
# 3



# Program 2: Unpacking with one starred variable

a, b, *c = [1, 2, 3]

print(a)
print(b)
print(c)

# OUTPUT:
# 1
# 2
# [3]



# Program 3: Collecting multiple remaining values

a, b, *c = [1, 2, 3, 4, 5]

print(a)
print(b)
print(c)

# OUTPUT:
# 1
# 2
# [3, 4, 5]



# Program 4: Starred variable in the middle

a, *b, c = [1, 2, 3, 4, 5]

print(a)
print(b)
print(c)

# OUTPUT:
# 1
# [2, 3, 4]
# 5




# Program 5: Starred variable at the beginning

*a, b, c = [1, 2, 3, 4, 5]

print(a)
print(b)
print(c)

# OUTPUT:
# [1, 2, 3]
# 4
# 5


# ===================================================================================
# Tuple packing and unpacking

# Program 6: Basic tuple unpacking

a, b, c = (1, 2, 3)

print(a)
print(b)
print(c)

# OUTPUT:
# 1
# 2
# 3




# Program 7: Tuple without parentheses

t = 10, 20, 30

print(t)
print(type(t))

# OUTPUT:
# (10, 20, 30)
# <class 'tuple'>




# Program 8: Starred tuple unpacking

a, b, *c = (1, 2, 3, 4, 5)

print(a)
print(b)
print(c)

# OUTPUT:
# 1
# 2
# [3, 4, 5]




# Program 9: Starred variable in the middle of a tuple

a, *b, c = (1, 2, 3, 4, 5)

print(a)
print(b)
print(c)

# OUTPUT:
# 1
# [2, 3, 4]
# 5


# =================================================================

#  Packing using *args

# Program 10: Normal function arguments

def add_numbers(num1, num2):
    print(num1 + num2)

add_numbers(10, 20)

# OUTPUT:
# 30


# Program 11: Pack multiple arguments using *args

def add_numbers(*num):
    print(num)
    print(type(num))

add_numbers(10, 20, 30, 40)

# OUTPUT:
# (10, 20, 30, 40)
# <class 'tuple'>



# Program 12: First argument plus remaining arguments

def add_numbers(num1, *num):
    print(num1)
    print(num)

add_numbers(10, 20, 30, 40)

# OUTPUT:
# 10
# (20, 30, 40)




# Program 13: Add multiple numbers using *args

def add_numbers(*num):
    print(sum(num))

add_numbers(10, 20, 30, 40)

# OUTPUT:
# 100

# Program 14: Find maximum and minimum values

def find_values(*numbers):
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))

find_values(10, 50, 20, 5, 40)

# OUTPUT:
# Maximum: 50
# Minimum: 5



# Program 15: Multiply multiple numbers

def multiply_numbers(*numbers):
    result = 1

    for number in numbers:
        result *= number

    print(result)

multiply_numbers(2, 3, 4)

# OUTPUT:
# 24



# ======================================================
# Unpacking using *


# Program 16: Unpack a list into function arguments

def add_numbers(num1, num2):
    print(num1 + num2)

list_of_num = [10, 20]

add_numbers(*list_of_num)

# OUTPUT:
# 30



# Program 17: Unpack a tuple into function arguments

def add_numbers(a, b, c):
    print(a + b + c)

numbers = (10, 20, 30)

add_numbers(*numbers)

# OUTPUT:
# 60



# Program 18: Merge two lists using unpacking

list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = [*list1, *list2]

print(merged_list)

# OUTPUT:
# [1, 2, 3, 4, 5, 6]



# Program 19: Unpack values into separate variables

numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)

# OUTPUT:
# First: 10
# Middle: [20, 30, 40]
# Last: 50


# ==============================================================================================

# Dictionary packing using **kwargs


# Program 20: Normal positional arguments

def contact_list(tom, jack):
    print(tom)
    print(jack)

contact_list(123, 456)

# OUTPUT:
# 123
# 456




# Program 21: Keyword arguments

def contact_list(tom, jack):
    print(tom)
    print(jack)

contact_list(tom=123, jack=456)

# OUTPUT:
# 123
# 456




# Program 22: Pack keyword arguments using **kwargs

def contact_list(**friends):
    print(friends)
    print(type(friends))

contact_list(tom=123, jack=456, jill=789)

# OUTPUT:
# {'tom': 123, 'jack': 456, 'jill': 789}
# <class 'dict'>



# Program 23: Access dictionary values inside **kwargs

def contact_list(**friends):
    for name, number in friends.items():
        print(name, number)

contact_list(tom=123, jack=456, jill=789)

# OUTPUT:
# tom 123
# jack 456
# jill 789




# Program 24: Count keyword arguments

def show_details(**details):
    print("Number of details:", len(details))

show_details(name="Sathya", age=33, role="QA Engineer")

# OUTPUT:
# Number of details: 3



# ======================================================================
# Dictionary unpacking using **

# Program 25: Unpack a dictionary into function arguments

def contact_list(tom, jack, jill):
    print(tom)
    print(jack)
    print(jill)

dic_friends = {
    "tom": 123,
    "jack": 456,
    "jill": 789
}

contact_list(**dic_friends)

# OUTPUT:
# 123
# 456
# 789



# Program 26: Merge dictionaries using **

dict1 = {"name": "Sathya", "role": "QA Engineer"}
dict2 = {"experience": 7, "language": "Python"}

merged_dict = {**dict1, **dict2}

print(merged_dict)

# OUTPUT:
# {'name': 'Sathya', 'role': 'QA Engineer',
#  'experience': 7, 'language': 'Python'}



# Program 27: Override values while merging dictionaries

dict1 = {"name": "Sathya", "role": "Tester"}
dict2 = {"role": "Automation Engineer", "language": "Python"}

merged_dict = {**dict1, **dict2}

print(merged_dict)

# OUTPUT:
# {'name': 'Sathya', 'role': 'Automation Engineer',
#  'language': 'Python'}


# ===========================================================================================
# Combined packing and unpacking

# Program 28: Use *args and **kwargs together

def employee_details(*skills, **details):
    print("Skills:", skills)
    print("Details:", details)

employee_details(
    "Python",
    "Selenium",
    name="Sathya",
    role="QA Engineer"
)

# OUTPUT:
# Skills: ('Python', 'Selenium')
# Details: {'name': 'Sathya', 'role': 'QA Engineer'}




# Program 29: Function with normal arguments, *args, and **kwargs

def employee_details(name, *skills, **details):
    print("Name:", name)
    print("Skills:", skills)
    print("Other details:", details)

employee_details(
    "Sathya",
    "Python",
    "Pytest",
    experience=7,
    domain="Banking"
)

# OUTPUT:
# Name: Sathya
# Skills: ('Python', 'Pytest')
# Other details: {'experience': 7, 'domain': 'Banking'}



# Program 30: Practical QA automation example

def run_test(test_name, *checks, **config):
    print("Test:", test_name)
    print("Checks:", checks)
    print("Configuration:", config)

run_test(
    "test_login",
    "status_code",
    "response_body",
    environment="test",
    browser="chrome"
)

# OUTPUT:
# Test: test_login
# Checks: ('status_code', 'response_body')
# Configuration: {'environment': 'test', 'browser': 'chrome'}







