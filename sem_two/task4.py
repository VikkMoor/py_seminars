"""Task bout swap adjacent numbers"""
elem_user = input('Enter digits separated by spaces: ')


def create_list(elements):
    nums = []
    for el in elem_user:
        i = 0
        if el in ' ':
            continue
        else:
            nums.append(el)
            i += 1
    return nums


def change_position(lis):
    for i in range(0, len(lis) - 1, 2):
        lis[i], lis[i + 1] = lis[i + 1], lis[i]
    return lis


print(f'{change_position(create_list(elem_user))}')
