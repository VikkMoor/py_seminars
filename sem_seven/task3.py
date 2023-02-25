"""Task bout Worker class.
Define public attributes "name", "surname", "position",
and the protected attribute "income"(it must refer
to a dictionary containing elements: salary and bonus. For example, {"wage": wage, "bonus": bonus}.

Create a class "Position" based on the "Worker" class. Implement public methods in the "Position"
obtaining the full name of the employee (get_full_name) and income, taking with bonus (get_total_income).

Check the example on real data (create instances of the "Position" class, transfer data,
check attribute values, call instance methods)"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        total = self._income['wage'] + self._income['bonus']
        return f'{total}'

    def __str__(self):
        return f'Worker: {self.get_full_name()}, her/his position: {self.position}, her/his income: {self.get_total_income()}'


examp = Position('Sophie-Ellis', 'Bextor', 'sexy_singer', 50000, 3000)
print(examp.get_full_name())
print(examp.get_total_income())
print(examp)  # (cuz of __str__)
