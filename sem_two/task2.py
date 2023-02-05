"""Task bout digit in the number"""
import math

a = int(input('Enter random positive integer, please: '))
a_max = 0
b = 0
while a > 0:
    b = a % 10
    a = math.floor(a / 10)
    if b > a_max:
        a_max = b
print(f'The biggest digit is: {a_max}')
