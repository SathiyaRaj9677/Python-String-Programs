# 1. Remove the Duplicates from the string:

s = "i can go to chennai and i can go to madurai"
words = s.split()
empty_list = []
for word in words:
    if word not in empty_list:
        empty_list.append(word)
result = " ".join(empty_list)
print(result)

# 2. Count the word occurrence:

s = "i can go to chennai and i can go to madurai"
words = s.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

# 3. Count the character occurrence:

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

s = "hi how are you?"
s1 = s.split()
new_list = []
for word in s1:
    if word not in new_list:
        new_list.append(word[::-1])
result = " ".join(new_list)
print(result)

# 5. Check the palindrome

s = "malayalam"
if s == s[::-1]:
    print(f"{s} is palindrome")
else:
    print(f"{s} is not palindrome")

# 6. Count the string character

s = "aabbbcdddd"
new_str = ""
for i in s:
    if i not in new_str:
        new_str+=str(s.count(i))+i
print(new_str)

# 7. Remove character from the string

s = "sathya"
new_str = ""
for i in range(len(s)):
    if i!=3:
        new_str+=s[i]
print(new_str)

# 9. Replace the string

s = "sathiyaraj"
new_str = ""
for i in range(len(s)):
    if i % 2 == 1:
        new_str+="x"
    else:
        new_str+=s[i]
print(new_str)

# 10. Find the longest Word From The String

s = "python is a good programming language"
s1 = s.split()
longest_word = ""
for word in s1:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)

# Another Method
s = "python is a good programming language"
s1 = s.split()
longest_word = max(s1, key=len)
print(longest_word)
print(len(longest_word))


# 11.Find the most repeated characters in the string
s = "sathya"
repeated_char = ""
word_count = 0
for char in s:
    count = s.count(char)
    if count > word_count:
        word_count = count
        repeated_char = char
print(repeated_char)
print(word_count)

# 12. Count the vowels in string

s = "Hello World"
vowels = ["a", "e", "i", "o", "u","A","E","I","O","U"]
new_str = ""
count = 0
for i in range(len(s)):
    if s[i] in vowels:
        new_str+=s[i]
        count+=1
print(new_str)
print(count)

s = "Hello World"
vowels = ["a", "e", "i", "o", "u","A","E","I","O","U"]
new_list = []
for char in s:
    if char in vowels:
        new_list.append(char)
result = " ".join(new_list)
print(result)

# 13. Find the vowels position in the string

s = "Hello World"
vowels = ["a", "e", "i", "o", "u","A","E","I","O","U"]
for index, char in enumerate(s):
    if char in vowels:
        print(f"{char} at the position of {index}")


# 14. Remove all vowels from the string
s = "Hello World"
vowels = ["a", "e", "i", "o", "u","A","E","I","O","U"]
new_list = []
for char in s:
    if char not in vowels:
        new_list.append(char)
result = " ".join(new_list)
print(result)

# 15. Replace only the second occurrence of 'a' with 'x'

s = "sathiyaraj"
new_str = ""
count = 0
for i in range(len(s)):
    if s[i] == "a":
        count += 1
        if count == 2:
            new_str += "x"
        else:
            new_str += s[i]
    else:
        new_str += s[i]
print(new_str)


