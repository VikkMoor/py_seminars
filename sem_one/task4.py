a = int(input("Enter the company's revenue: "))
b = int(input("Enter the company's costs: "))
if b > a:
    print(f'The financial result - the loss. Its value is: {b - a}.')
elif a > b:
    print(f'The financial result - the profit. Its value is: {a - b}.')
    print("So, let's calculate the rentability (profit/revenue)")
    print(f'The rentability value = {round(((a - b) / a), 1)}')
    c = int(input("Indicate the number of employees: "))
    print(f'Company profit per employee: {round((a - b) / c, 1)}')
else:
    print("Company at breakeven point.")
