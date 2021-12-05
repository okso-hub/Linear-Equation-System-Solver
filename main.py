'''
cheatsheet:
https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html

>>> a = np.array([[1, 2], [3, 5]])
>>> b = np.array([1, 2])
>>> x = np.linalg.solve(a, b)
>>> x
Output: array([-1.,  1.])
'''
from numpy import array, linalg
from os import system

clear = lambda: system('clear')


def solve_two_unknowns():

    print("a*x + b*y = c \nd*x + e*y = f")

    a = int(input("Enter value for factor a: "))    
    b = int(input("Enter value for factor b: "))
    c = int(input("Enter value for product c: "))    
    d = int(input("Enter value for factor d: "))
    e = int(input("Enter value for factor e: "))
    f = int(input("Enter value for solution f: "))

    x = array([[a, b], [d, e]])
    y = array([c, f])
    solution = linalg.solve(x, y)

    print(f"The solution is x={solution[0]}; y={solution[1]}")


def solve_three_unknowns():
    
    print("a*x + b*y + c*z = d \ne*x + f*y + g*z = h \ni*x + j*y + k*z = l")

    a = int(input("Enter value for factor a: "))    
    b = int(input("Enter value for factor b: "))
    c = int(input("Enter value for factor c: "))    
    d = int(input("Enter value for solution d: "))
    e = int(input("Enter value for factor e: "))
    f = int(input("Enter value for factor f: "))
    g = int(input("Enter value for factor g: "))
    h = int(input("Enter value for solution h: "))
    i = int(input("Enter value for solution i: "))
    j = int(input("Enter value for factor j: "))
    k = int(input("Enter value for factor k: "))
    l = int(input("Enter value for solution l: "))

    x = array([[a, b, c], [e, f, g], [i, j, k]])
    y = array([d, h, l])
    solution = linalg.solve(x, y)

    print(f"The solutions are x={solution[0]}; y={solution[1]}; z={solution[2]}")

def main():

    choice = int(input("How many unknowns are you looking for? "))

    if choice == 2:
        solve_two_unknowns()
    if choice == 3:
        solve_three_unknowns()


if __name__ == '__main__':
    clear()
    main()

