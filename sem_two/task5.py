words = input('Please, enter numbers separated by spaces: ').split(' ')
i = 0
for el in words:
    if len(el) > 10:
        print(f'{i + 1}. {el[0: 10]}')
    else:
        print(f'{i + 1}. {el}')
    i += 1
