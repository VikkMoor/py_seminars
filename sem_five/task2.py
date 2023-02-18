"""Count even and odd digits in the number"""


def nums_count(num, even=0, odd=0):
    if num == 0:
        return f'Odd digits - {odd}, Even digits - {even}'
    if num % 2 == 0:
        even += 1
        num = num // 10
        return nums_count(num, even, odd)
    else:
        odd += 1
        num = num // 10
        return nums_count(num, even, odd)


try:
    print(f'Enter a number: ')
    n = int(input())
except ValueError:
    print(f'Enter a NUMBER, please: ')
    n = int(input())
print(f'In the number {n} {nums_count(n)}')
