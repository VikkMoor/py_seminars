"""Task bout month (dict)"""
mon = input('Enter number of month, please: ')
mon_dict = {'1': 'winter', '2': 'winter', '3': 'spring', '4': 'spring', '5': 'spring', '6': 'summer', '7': 'summer', '8': 'summer', '9': 'autumn', '10': 'autumn', '11': 'winter', '12': 'winter'}
for item in mon_dict:
    if item == mon:
        print(*{mon_dict[item]})
    else:
        continue
