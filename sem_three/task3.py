"""Task bout goods and tuples"""
goods = []
def fill_database():
    i = 1
    ans = input(f'Enter new position? Yes/No: ').lower()
    while ans == 'yes':
        tur = (i, {'name': input(f'Enter new name: '),
                   'price': input(f'Enter new price: '),
                   'amount': input(f'Enter amount: '),
                   'units': input(f'Enter units: ')})
        goods.append(tur)
        i += 1
        ans = input(f'Enter new position? Yes/No: ').lower()
    return goods


def goods_analytics(goods):
    temp_names = []
    temp_prices = []
    temp_quantities = []
    temp_unit = []
    for element in goods:
        temp_names.append(element[1]['name'])
        temp_prices.append(element[1]['price'])
        temp_quantities.append(element[1]['amount'])
        temp_unit.append(element[1]['units'])
    result_dict = {'name': temp_names, 'price': temp_prices,
                   'amount': temp_quantities, 'units': temp_unit}
    return [f'\t{el}\n' for el in result_dict.items()]


fill_database()
print(*goods_analytics(goods))