"""Task bout month (list)"""
mon = int(input('Enter number of month, please: '))
mon_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
mon_list = ''
for i in range(len(mon_num)):
    if 2 < mon_num[i] < 6:
        mon_list = 'spring'
    elif 5 < mon_num[i] < 9:
        mon_list = 'summer'
    elif 8 < mon_num[i] < 11:
        mon_list = 'autumn'
    else:
        mon_list = 'winter'
    if mon == mon_num[i]:
        print(*{mon_list})

