"""Task bout exception class. Create such class
that should check the list for having only numbers.
The exception class must control the data types of the list items.
Note: the length of the list is not fixed. Items are requested indefinitely,
until the user stops the script himself by entering the “stop” command (for example).
So the script ends and the generated list with numbers is displayed on the screen."""


class Numbers(Exception):
    def __init__(self, txt):
        self.txt = txt


els = []
print('Enter numbers one by one with enter or "stop" for complete:')
while True:

    try:
        el = input()
        if el == 'stop':
            break
        if not el.isdigit():
            raise Numbers('It was not a number!')
        els.append(el)
    except Numbers as err:
        print(err)
print(els)
