"""Task bout sportsman"""
a = int(input('Enter the first day distance: '))
b = int(input('Enter the limit of km: '))
c = 1
print(f'{c}st day: {a}')
while a < b:
    a = round((a + a / 10), 2)
    c += 1
    print(f'{c} day: {a}')
print(f'Solved: at the {c} day sprinter reach the result - at least {b} kilometers')
