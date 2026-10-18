# 1. Remove duplicates from the list

l = [1, 2, 3, 4, 5, 6, 4, 9, 2, 1]
new_list = []
for i in l:
    if i not in new_list:
        new_list.append(i)
print(new_list)
