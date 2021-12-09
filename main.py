from numpy import array, linalg
import os

clear = lambda: os.system('clear') if os.name == 'posix' else os.system('cls')


def solve_two_unknowns():

    print("a1*x + b1*y = c1 \na2*x + b2*y = c3")

    a1 = float(input("Enter value for factor a1: "))    
    b1 = float(input("Enter value for factor b1: "))
    c1 = float(input("Enter value for product c1: "))    
    a2 = float(input("Enter value for factor a2: "))
    b2 = float(input("Enter value for factor b2: "))
    c2 = float(input("Enter value for solution c2: "))

    x = array([[a1, b1], [a2, b2]])
    y = array([c1, c2])
    solution = linalg.solve(x, y)

    print(f"The solutions are x={solution[0]}; y={solution[1]}.")


def solve_three_unknowns():
    
    print("a1*x + b1*y + c1*z = d1 \na2*x + b2*y + c2*z = d2 \na3*x + b3*y + c3*z = d3")

    a1 = float(input("Enter value for factor a1: "))    
    b1 = float(input("Enter value for factor b1: "))
    c1 = float(input("Enter value for factor c1: "))    
    d1 = float(input("Enter value for solution d1: "))
    a2 = float(input("Enter value for factor a2: "))
    b2 = float(input("Enter value for factor b2: "))
    c2 = float(input("Enter value for factor c2: "))
    d2 = float(input("Enter value for solution d2: "))
    a3 = float(input("Enter value for factor a3: "))
    b3 = float(input("Enter value for factor b3: "))
    c3 = float(input("Enter value for factor c3: "))
    d3 = float(input("Enter value for solution d3: "))

    x = array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
    y = array([d1, d2, d3])
    solution = linalg.solve(x, y)

    print(f"The solutions are x={solution[0]}; y={solution[1]}; z={solution[2]}.")


def solve_four_unknowns():
    
    print("a1*x + b1*y + c1*z + d1*w = e1 \na2*x + b2*y + c2*z + d2*w = e2 \na3*x + b3*y + c3*z + d3*w = e3 \na4*x + b4*y + c4*z + d4*w = e4")

    a1 = float(input("Enter value for factor a1: "))    
    b1 = float(input("Enter value for factor b1: "))
    c1 = float(input("Enter value for factor c1: "))    
    d1 = float(input("Enter value for factor d1: "))
    e1 = float(input("Enter value for solution e1: "))

    a2 = float(input("Enter value for factor a2: "))
    b2 = float(input("Enter value for factor b2: "))
    c2 = float(input("Enter value for factor c2: "))
    d2 = float(input("Enter value for factor d2: "))
    e2 = float(input("Enter value for solution e2: "))

    a3 = float(input("Enter value for factor a3: "))
    b3 = float(input("Enter value for factor b3: "))
    c3 = float(input("Enter value for factor c3: "))
    d3 = float(input("Enter value for factor d3: "))
    e3 = float(input("Enter value for solution e3: "))

    a4 = float(input("Enter value for factor a4: "))
    b4 = float(input("Enter value for factor b4: "))
    c4 = float(input("Enter value for factor c4: "))
    d4 = float(input("Enter value for factor d4: "))
    e4 = float(input("Enter value for solution e4: "))

    x = array([[a1, b1, c1, d1], [a2, b2, c2, d2], [a3, b3, c3, d3], [a4, b4, c4, d4]])
    y = array([e1, e2, e3, e4])
    solution = linalg.solve(x, y)

    print(f"The solutions are x={solution[0]}; y={solution[1]}; z={solution[2]}; w={solution[3]}.")


def main():

    choice = int(input("How many unknowns are you looking for? "))

    if choice == 2:
        solve_two_unknowns()
    if choice == 3:
        solve_three_unknowns()
    if choice == 4:
        solve_four_unknowns()


if __name__ == '__main__':
    clear()
    main()

