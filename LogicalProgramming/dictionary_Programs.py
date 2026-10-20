# 1. Create a dictionary with keys as numbers from 1 to 5 and values as their squares:
d = {}
for i in range(1, 6):
    d[i] = i ** 2
print(d)

# 2. Count the frequency of each character in a string:
s = "hello world"
char_count = {}
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)   

# 3. Create a dictionary with keys as numbers from 1 to 5 and values as their cubes:
d = {}
for i in range(1, 6):
    d[i] = i ** 3
print(d)

#4. Count the frequency of each character in a string:
s = "hello world"
char_count = {}
for char in s:
    if char in char_count:  
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count) 

# 4. Create a dictionary with keys as numbers from 1 to 5 and values as their factorials:
d = {}
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 
for i in range(1, 6):
    d[i] = factorial(i)
print(d)    


