"""Task bout learning yaml module.
Write a script for to automate
filling file yaml format with data.."""

import yaml

DATA_IN = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
           'items_quantity': 4,
           'items_price': {'computer': '1000€',
                           'keyboard': '50€',
                           'mouse': '7€',
                           'printer': '300€'}
           }

with open('file_2.yaml', 'w', encoding='utf-8') as f_in:
    yaml.dump(DATA_IN, f_in, default_flow_style=False, allow_unicode=True)

with open("file_2.yaml", 'r', encoding='utf-8') as f_out:
    DATA_OUT = yaml.load(f_out, Loader=yaml.SafeLoader)

print(DATA_IN == DATA_OUT)
