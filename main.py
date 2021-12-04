'''
cheatsheet:
https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html

>>> a = np.array([[1, 2], [3, 5]])
>>> b = np.array([1, 2])
>>> x = np.linalg.solve(a, b)
>>> x
Output: array([-1.,  1.])
'''
from numpy import array
from numpy import linalg


def solve_two_unknowns():
    a = int(input("Enter value for factor a: "))    
    b = int(input("Enter value for factor b: "))
    c = int(input("Enter value for product c: "))    
    d = int(input("Enter value for factor d: "))
    e = int(input("Enter value for factor e: "))
    f = int(input("Enter value for solution f: "))

    x = array([[a, b], [d, e]])
    y = array([c, f])
    solution = linalg.solve(x, y)

    print(f"The solution is {solution}")


def solve_three_unknowns():
    pass


def main():
    solve_two_unknowns()


if __name__ == '__main__':
    main()

