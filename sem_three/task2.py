"""Task bout rating"""
my_list = [7, 5, 3, 3, 2]
new_el = int(input('Enter new element of rating: '))
for i in range(len(my_list)):
    if my_list[i] < new_el:
        my_list.insert(i, new_el)
        break
    elif my_list[-1] > new_el:
        my_list.append(new_el)
        break
    elif my_list[len(my_list) - 1] == new_el:
        my_list.append(new_el)
        break
print(*my_list)
