"""Task bout month (list)"""
mon = int(input('Enter number of month, please: '))
if 8 < mon < 11:
    print('autumn')
elif 2 < mon < 6:
    print('spring')
elif 5 < mon < 9:
    print('summer')
else:
    print('winter')
