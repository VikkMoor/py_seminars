"""Simple calculator"""
print('Enter two numbers and the symbol of the mathematical operation, "0" as the sign of the operation will shutdown the program.')
def calculator(action=None):
    action_dict = {'+': lambda x, y: x + y,
                   '-': lambda x, y: x - y,
                   '*': lambda x, y: x * y,
                   '/': lambda x, y: x / y}
    if action is None:
        action = input('Enter the symbol of the mathematical operation: ')
    if action in action_dict:
        try:
            number1 = int(input('Enter the 1st number: '))
            number2 = int(input('Enter the 2nd number: '))
            print(f'Result: {action_dict[action](number1, number2)}')
        except ValueError:
            print('Enter a number, please')
        except ZeroDivisionError:
            print('Zero division error.')
        return calculator()
    elif action == '0':
        return print('Program shutdown.')
    else:
        print('Enter correct math symbol, please.')
        return calculator()
print(calculator())