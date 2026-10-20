# 1. Remove duplicates from the list

l = [1, 2, 3, 4, 5, 6, 4, 9, 2, 1]
new_list = []
for i in l:
    if i not in new_list:
        new_list.append(i)
print(new_list)


# 2. Count the repeated items occurrence in the list:

l = [1, 2, 3, 4, 5, 6, 4, 9, 2, 1]
count_dict = {}
for i in l:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1
print(count_dict)


# 3. Remove the concecutive duplicates from the list:
l = [1, 2, 2, 3, 4, 5, 6, 4, 9, 9, 2, 1, 1]
new_list = []
for i in range(len(l)):
    if i == 0 or l[i] != l[i - 1]:
        new_list.append(l[i])
print(new_list)

# 4. Move 0 to the end of the list:
l = [1, 2, 0, 3, 4, 0, 5, 6, 0, 4, 9, 2, 1]
for i in l:
    if i == 0:
        l.remove(i)
        l.append(i)
print(l)

# 5. Find the maximun and minimum number from the list:
l = [1, 2, 3, 4, 5, 6, 4, 9, 2, 1]
max_num = l[0]
min_num = l[0]
for i in l:
    if i > max_num:
        max_num = i
    if i < min_num:
        min_num = i
print(f"Maximum number is: {max_num}")
print(f"Minimum number is: {min_num}")

# 6. Find the second largest number from the list:
l = [1, 2, 3, 4, 5, 6, 4, 9, 2, 1]
max_num = l[0]
second_max = l[0]
for i in l:
    if i > max_num:
        second_max = max_num
        max_num = i
    elif i > second_max and i != max_num:
        second_max = i
print(f"Second largest number is: {second_max}")

# 7. Find the second smallest number from the list:
l = [1, 2, 3, 4, 5, 6, 4, 9, 2, 1]
min_num = l[0]
second_min = l[0]
for i in l:
    if i < min_num:
        second_min = min_num
        min_num = i
    elif i < second_min and i != min_num:
        second_min = i
print(f"Second smallest number is: {second_min}")

# 8. Count the list item occurrence:
l = [1, 2, 3, 4, 5, 6, 4, 9, 2, 1]
count_dict = {}
for i in l:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1
print(count_dict)

# 9. Find the common elements from the two lists:
l1 = [1, 2, 3, 4, 5, 6, 4, 9, 2, 1]
l2 = [1, 2, 3, 4, 5, 6, 4, 9, 2, 1, 10, 11, 12]
common_elements = []
for i in l1:
    if i in l2 and i not in common_elements:
        common_elements.append(i)
print(common_elements) 

# 10. Reverse the list:
l = [1, 2, 3, 4, 5, 6, 4, 9, 2, 1]
reversed_list = []
for i in range(len(l)-1, -1, -1):
    reversed_list.append(l[i])
print(reversed_list)    

# 11. Sort the list:
l = [1, 2, 3, 4, 5, 6, 4, 9, 2, 1]
for i in range(len(l)):     
    for j in range(i + 1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print(l)

# 12. Find the missing number from the list:
l = [1, 2, 3, 4, 5, 6, 8, 9, 10]
n = len(l) + 1
total = n * (n + 1) // 2
sum_of_list = sum(l)
missing_number = total - sum_of_list
print(f"The missing number is: {missing_number}")

# 13. Remove the second occurrence of the 1 from the list:
l = [1, 2, 3, 4, 5, 6,  4, 9, 2, 1, 10, 11, 12]
count = 0
for i in range(len(l)):
    if l[i] == 1:
        count += 1
        if count == 2:
            l.pop(i)
            break
print(l)


# 14. Make the nested list from the given list:
l = [1, 2, 3, 4, 5, 6, 4, 9, 2, 1]
nested_list = []
for i in range(0, len(l), 2):
    nested_list.append(l[i:i + 2])
print(nested_list)  

# 15. Convert nested list to the single list:
nested_list = [[1, 2], [3, 4], [5, 6], [4, 9], [2, 1]]
single_list = []
for sublist in nested_list:
    for item in sublist:
        single_list.append(item)
print(single_list)

# 16. Combine two lost without zero:
l1 = [1, 2, 3, 4, 5, 6, 0, 4, 9, 2, 1]
l2 = [1, 2, 3, 4, 5, 6, 0, 4, 9, 2, 1]
combined_list = []
for i in l1:
    if i != 0:
        combined_list.append(i)
for i in l2:
    if i != 0:
        combined_list.append(i)
print(combined_list)    
