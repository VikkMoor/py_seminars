"""Reverse number"""


def reverse_num(num):
    if num < 10:
        return str(num)
    else:
        last = str(num % 10)
        return last + reverse_num(num // 10)


print(reverse_num(int(input('Enter a number: '))))
