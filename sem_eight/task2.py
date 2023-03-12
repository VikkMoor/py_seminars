"""Task bout learning json module.
Write a script for to automate
filling file orders.json with data."""

import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', encoding='utf-8') as f:
        data = json.load(f)
        data["orders"].append({
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        })

    with open('orders.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4,
                  ensure_ascii=False)  # ensure_ascii for Cyrillic (need to open for it in utf-8 in str№9)


write_order_to_json('Calculator', 15, 2000, 'Sidorov S.S.', '11.03.2023')
write_order_to_json('Computer_mouse', 15, 1500, 'Sidorov S.S.', '11.03.2023')
