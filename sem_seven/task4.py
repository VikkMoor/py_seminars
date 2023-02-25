"""Task bout class Matrix.
Make class constructor overload (init() method),
which must have an input data (a list of lists) to form a matrix.
The next step is to implement an overload of the str() method to display the matrix in the usual way.
Next, make an overload of the add() method to implement the operation of adding two
objects of class Matrix (two matrices).
The result of the addition must be a new matrix."""


class Matrix:
    def __init__(self, list_of_lists):
        self.mat = list_of_lists

    def __str__(self):
        string = ''
        for i in self.mat:
            for j in i:
                string = string + '%2s\t' % j
            string = string[:-1]
            string = string + '\n'
        string = string[:-1]
        return string

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.mat)):
            for j in range(len(self.mat)):
                sum_el = other.mat[i][j] + self.mat[i][j]
                numbers.append(sum_el)
                if len(numbers) == len(self.mat):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


a = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
b = [[2, 3, 3], [-2, 1, -6], [5, -3, 0]]
m_1 = Matrix(a)
m_2 = Matrix(b)

print("\nMatrix 1st:")
print(m_1)

print("\nMatrix 2nd:")
print(m_2)

print("\nSum of them:")
print(m_1.__add__(m_2))
