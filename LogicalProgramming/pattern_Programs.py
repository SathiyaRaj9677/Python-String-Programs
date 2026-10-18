# 7. Right-Angled Triangle

for i in range(1, 6):
    print("* " * i)

# OUTPUT:
# *
# * *
# * * *
# * * * *
# * * * * *


# 8. Inverted Right-Angled Triangle

for i in range(5, 0, -1):
    print("* " * i)

# OUTPUT:
# * * * * *
# * * * *
# * * *
# * *
# *


# 9. Right-Aligned Triangle

for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)

# OUTPUT:
#     *
#    **
#   ***
#  ****
# *****


# 10. Pyramid Pattern

for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)

# OUTPUT:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *


# 11. Inverted Pyramid Pattern

for i in range(5, 0, -1):
    print(" " * (5 - i) + "* " * i)

# OUTPUT:
# * * * * *
#  * * * *
#   * * *
#    * *
#     *


# 12. Diamond Pattern

for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)

for i in range(4, 0, -1):
    print(" " * (5 - i) + "* " * i)

# OUTPUT:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *


# 13. Number Triangle

for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

# OUTPUT:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


# 14. Repeated Number Triangle

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# OUTPUT:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# 15. Inverted Number Triangle

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# OUTPUT:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1


# 16. Descending Number Triangle

for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# OUTPUT:
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1


# 17. Continuous Number Triangle

num = 1

for i in range(1, 6):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()

# OUTPUT:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15


# 18. Inverted Continuous Number Triangle

num = 1

for i in range(5, 0, -1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# OUTPUT:
# 1 2 3 4 5
# 6 7 8 9
# 10 11 12
# 13 14
# 15


# 19. Alternating 0 and 1 Pattern

for i in range(1, 6):
    for j in range(1, i + 1):
        print((i + j) % 2, end=" ")
    print()

# OUTPUT:
# 0
# 1 0
# 0 1 0
# 1 0 1 0
# 0 1 0 1 0


# 20. Alphabet Triangle

for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

# OUTPUT:
# A
# A B
# A B C
# A B C D
# A B C D E


# 21. Repeated Alphabet Triangle

for i in range(1, 6):
    print(chr(64 + i) * i)

# OUTPUT:
# A
# BB
# CCC
# DDDD
# EEEEE


# 22. Inverted Alphabet Triangle

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    print()

# OUTPUT:
# A B C D E
# A B C D
# A B C
# A B
# A


# 23. Hollow Square Pattern

for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# OUTPUT:
# * * * * *
# *       *
# *       *
# *       *
# * * * * *


# 24. Hollow Right-Angled Triangle

for i in range(1, 6):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# OUTPUT:
# *
# * *
# *   *
# *     *
# * * * * *


# 25. X Pattern

size = 5

for i in range(size):
    for j in range(size):
        if i == j or i + j == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# OUTPUT:
# *       *
#   *   *
#     *
#   *   *
# *       *


# 26. Plus Pattern

size = 5
middle = size // 2

for i in range(size):
    for j in range(size):
        if i == middle or j == middle:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# OUTPUT:
#     *
#     *
# * * * * *
#     *
#     *


# 27. Multiplication Table Triangle

for i in range(1, 6):
    for j in range(1, i + 1):
        print(i * j, end="\t")
    print()

# OUTPUT:
# 1
# 2    4
# 3    6    9
# 4    8    12   16
# 5    10   15   20   25


# 28. Floyd's Triangle

num = 1

for i in range(1, 6):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()

# OUTPUT:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15


# 29. Palindrome Number Pyramid

for i in range(1, 6):
    print(" " * (5 - i), end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()

# OUTPUT:
#     1
#    121
#   12321
#  1234321
# 123454321


# 30. Butterfly Pattern

size = 5

for i in range(1, size + 1):
    print("*" * i + " " * (2 * (size - i)) + "*" * i)

for i in range(size - 1, 0, -1):
    print("*" * i + " " * (2 * (size - i)) + "*" * i)

# OUTPUT:
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


# 31. Binary Triangle

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j % 2, end=" ")
    print()

# OUTPUT:
# 1
# 1 0
# 1 0 1
# 1 0 1 0
# 1 0 1 0 1


# 32. Right-Aligned Number Triangle

for i in range(1, 6):
    print(" " * (5 - i), end="")

    for j in range(1, i + 1):
        print(j, end="")

    print()

# OUTPUT:
#     1
#    12
#   123
#  1234
# 12345


# 33. Descending Repeated Number Pattern

for i in range(5, 0, -1):
    print(str(i) * i)

# OUTPUT:
# 55555
# 4444
# 333
# 22
# 1


# 34. Square Number Pattern

for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")
    print()

# OUTPUT:
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5


# 35. Reverse Star Triangle

for i in range(1, 6):
    print(" " * (i - 1) + "*" * (6 - i))

# OUTPUT:
# *****
#  ****
#   ***
#    **
#     *


# 36. Continuous Reverse Number Pattern

num = 15

for i in range(5, 0, -1):
    for j in range(i):
        print(num, end=" ")
        num -= 1
    print()

# OUTPUT:
# 15 14 13 12 11
# 10 9 8 7
# 6 5 4
# 3 2
# 1


# 37. Checkerboard Pattern

for i in range(5):
    for j in range(5):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()

# OUTPUT:
# * # * # *
# # * # * #
# * # * # *
# # * # * #
# * # * # *


# 38. Hollow Pyramid

size = 5

for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")

    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == size:
            print("*", end="")
        else:
            print(" ", end="")

    print()

# OUTPUT:
#     *
#    * *
#   *   *
#  *     *
# *********


# 39. Number Diamond

size = 5

for i in range(1, size + 1):
    print(" " * (size - i), end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()

for i in range(size - 1, 0, -1):
    print(" " * (size - i), end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()

# OUTPUT:
#     1
#    121
#   12321
#  1234321
# 123454321
#  1234321
#   12321
#    121
#     1


# 40. Pascal's Triangle

from math import factorial

size = 5

for i in range(size):
    print(" " * (size - i), end="")

    for j in range(i + 1):
        value = factorial(i) // (factorial(j) * factorial(i - j))
        print(value, end=" ")

    print()

# OUTPUT:
#      1
#     1 1
#    1 2 1
#   1 3 3 1