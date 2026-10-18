# Program 1: Check even or odd

num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# OUTPUT:
# Odd



# Program 2: Sum of digits

num = 1234
total = 0
while num > 0:
    total += num % 10
    num //= 10

print(total)

# OUTPUT:
# 10



# Program 3: Count the digits in a number

num = 12345
count = len(str(abs(num)))
print(count)

# OUTPUT:
# 5



# Program 4: Swap two numbers

a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)

# OUTPUT:
# a = 20
# b = 10



# Program 5: Find the second-largest distinct number

numbers = [10, 20, 30, 30, 25]

unique_numbers = sorted(set(numbers))

if len(unique_numbers) >= 2:
    print(unique_numbers[-2])
else:
    print("Second-largest number does not exist")

# OUTPUT:
# 25




# Program 6: Print Fibonacci series

n = int(input("Enter the number of terms: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# OUTPUT:
# Enter the number of terms: 10
# 0 1 1 2 3 5 8 13 21 34





# Program 7: Fibonacci series in a list

def fibonacci(n):
    fib = []
    a, b = 0, 1

    for i in range(n):
        fib.append(a)
        a, b = b, a + b

    return fib

print(fibonacci(10))

# OUTPUT:
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]



# Program 8: Check whether a number is Fibonacci

def is_fibonacci(n):
    if n < 0:
        return False

    a, b = 0, 1

    while a < n:
        a, b = b, a + b

    return a == n

print(is_fibonacci(5))
print(is_fibonacci(6))

# OUTPUT:
# True
# False





# Program 9: Reverse using string slicing

num = 12345

reversed_num = int(str(num)[::-1])

print(reversed_num)

# OUTPUT:
# 54321



# Program 10: Reverse using a while loop

num = 12345
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(reverse)

# OUTPUT:
# 54321





# Program 11: Check whether a number is a palindrome

num = 121

if str(num) == str(num)[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# OUTPUT:
# Palindrome



# Program 12: Palindrome without string conversion

num = 121
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

# OUTPUT:
# Palindrome




# Program 13: Factorial using a for loop

n = 5
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)

# OUTPUT:
# 120



# Program 14: Factorial using a function

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact

print(factorial(5))
print(factorial(10))

# OUTPUT:
# 120
# 3628800



# Program 15: Factorial using recursion

def factorial(n):
    if n < 0:
        raise ValueError("Number must not be negative")

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

# OUTPUT:
# 120



# Program 16: Check whether a number is prime

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

num = 17

if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")

# OUTPUT:
# Prime number




# Program 17: Print prime numbers from 1 to 100

for num in range(2, 101):
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

# OUTPUT:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43
# 47 53 59 61 67 71 73 79 83 89 97




# Program 18: Print the first 100 prime numbers

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

count = 0
num = 2

while count < 100:
    if is_prime(num):
        print(num, end=" ")
        count += 1

    num += 1




# Program 19: Check Armstrong number

num = 153
digits = str(num)
power = len(digits)

total = 0

for digit in digits:
    total += int(digit) ** power

if total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

# OUTPUT:
# Armstrong number




# Program 20: Print Armstrong numbers from 1 to 1000

for num in range(1, 1001):
    digits = str(num)
    power = len(digits)

    total = sum(int(digit) ** power for digit in digits)

    if total == num:
        print(num, end=" ")

# OUTPUT:
# 1 2 3 4 5 6 7 8 9 153 370 371 407



# Program 21: Find largest, middle and smallest numbers

num1 = 25
num2 = 30
num3 = 20

numbers = [num1, num2, num3]
numbers.sort(reverse=True)

print("Largest:", numbers[0])
print("Middle:", numbers[1])
print("Smallest:", numbers[2])

# OUTPUT:
# Largest: 30
# Middle: 25
# Smallest: 20




# Program 22: Find the largest number without max()

a, b, c = 25, 30, 20

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest:", largest)

# OUTPUT:
# Largest: 30




# Program 23: Convert binary string to decimal

binary_string = input("Enter a binary string: ")

decimal_number = int(binary_string, 2)

print("Decimal equivalent:", decimal_number)

# INPUT:
# 100

# OUTPUT:
# Decimal equivalent: 4




# Program 24: Binary to decimal without int(..., 2)

binary_string = "100"
decimal_number = 0

for digit in binary_string:
    decimal_number = decimal_number * 2 + int(digit)

print(decimal_number)

# OUTPUT:
# 4




# Program 25: Check whether a number is positive, negative or zero

num = -5

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# OUTPUT:
# Negative



# Program 26: Find the sum of the first N natural numbers

n = 10
total = 0

for i in range(1, n + 1):
    total += i

print(total)

# OUTPUT:
# 55



# Program 27: Check whether a number is a perfect number

num = 28
total = 0

for i in range(1, num):
    if num % i == 0:
        total += i

if total == num:
    print("Perfect number")
else:
    print("Not a perfect number")

# OUTPUT:
# Perfect number



# Program 28: Find the GCD of two numbers

import math

a = 24
b = 36

print(math.gcd(a, b))

# OUTPUT:
# 12



# Program 29: Find the LCM of two numbers

import math

a = 12
b = 18

lcm = abs(a * b) // math.gcd(a, b)

print(lcm)

# OUTPUT:
# 36



# Program 30: Swap two numbers

a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)

# OUTPUT:
# a = 20
# b = 10



# Program 31: Find the second-largest distinct number

numbers = [10, 20, 30, 30, 25]

unique_numbers = sorted(set(numbers))

if len(unique_numbers) >= 2:
    print(unique_numbers[-2])
else:
    print("Second-largest number does not exist")

# OUTPUT:
# 25

