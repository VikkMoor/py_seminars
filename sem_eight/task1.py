"""Task bout learning CSV module.
Write a script for sampling of data from 3 txt files and
generating a new "reporting" file in CSV format."""

import csv
import re


def get_data(titles, files):
    collect_data = {}  # creating empty dictionary
    for f in files:
        # for getting dictionary from file: {'key1':'val1', 'key2':'val2',...}
        x = {m.groups()[0]: m.groups()[1] for m in re.finditer(r'(.+): +(.+)', open(f, encoding="utf-8").read())}
        [collect_data.setdefault(name, []).append(x[name]) for name in titles]  # collecting needed info from dictionary
    return list(zip(*[[key, *val] for key, val in collect_data.items()]))  # create list and matrix transposition


def write_to_csv(file, table):
    with open(file, "w", encoding="utf-8") as f:
        csv.writer(f).writerows(table)


info = get_data(("Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"),
                ("info_1.txt", "info_2.txt", "info_3.txt"))
write_to_csv("info.csv", info)
