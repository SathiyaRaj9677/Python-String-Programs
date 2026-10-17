# 1. Remove the Duplicates from the string:

s = "i can go to chennai and i can go to madurai"
words = s.split()
empty_list = []
for word in words:
    if word not in empty_list:
        empty_list.append(word)
result = " ".join(empty_list)
print(result)

# 2. Count the word occurance:

s = "i can go to chennai and i can go to madurai"
words = s.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

# 3. Count the character occurance:

s = "i can go to chennai and i can go to madurai"
char_count = {}
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)

# 4. Reverse the string:

s = "hi how are you?"
s1 = s.split()
for word in s1:
    print(word[::-1], end=" ")

s = "hi how are you?"
s1 = s.split()
reversed_str = ""
for word in s1:
    reversed_str += word[::-1]
print(reversed_str, end=" ")


# 5. Check the palindrome

s = "malayalam"
if s == s[::-1]:
    print(f"{s} is palindrome")
else:
    print(f"{s} is not palindrome")

# 6. Count the string charecters

s = "aabbbcdddd"
new_str = ""
for i in s:
    if i not in new_str:
        new_str+=str(s.count(i))+i
print(new_str)

