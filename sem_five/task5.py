"""Guessing the number 1...100 with 10 tries"""
import random

numb = random.randint(0, 101)


def game(count, num):
    print(f'Try №{count}')
    answer = int(input('Enter the number from 0 to 100: '))
    if count == 10 or answer == num:
        if answer == num:
            print('Hooray!')
        else:
            print(f'Hidden number was: {num}')
    else:
        if answer < num:
            print(f'Your answer is less than hidden number ;)')
        else:
            print(f'Your answer is greater than hidden number ;)')
        game(count + 1, num)


game(1, numb)
