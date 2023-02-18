"""Task bout equality 1+2+3...+n = n(n+1)/2"""


def sum_nums(n): # calculate sum of 1...n
    if n == 1:
        return n
    return n + sum_nums(n - 1)


if __name__ == '__main__':

    a = int(input('Enter integer: '))

    print("Equality check:\n"
          "1+2+...+n = n(n+1)/2")

    print(f'If integer is {a}:\n'
          f'\t- According to the formula n(n+1)/2: {int(a * (a + 1) / 2)}\n'
          f'\t- Sum of 1...n: {sum_nums(a)}')
