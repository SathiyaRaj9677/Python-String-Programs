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
