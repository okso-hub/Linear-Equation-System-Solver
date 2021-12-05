from numpy import array, linalg
from os import system

clear = lambda: system('clear')


def solve_two_unknowns():

    print("a*x + b*y = c \nd*x + e*y = f")

    a = float(input("Enter value for factor a: "))    
    b = float(input("Enter value for factor b: "))
    c = float(input("Enter value for product c: "))    
    d = float(input("Enter value for factor d: "))
    e = float(input("Enter value for factor e: "))
    f = float(input("Enter value for solution f: "))

    x = array([[a, b], [d, e]])
    y = array([c, f])
    solution = linalg.solve(x, y)

    print(f"The solutions are x={solution[0]}; y={solution[1]}.")


def solve_three_unknowns():
    
    print("a*x + b*y + c*z = d \ne*x + f*y + g*z = h \ni*x + j*y + k*z = l")

    a = float(input("Enter value for factor a: "))    
    b = float(input("Enter value for factor b: "))
    c = float(input("Enter value for factor c: "))    
    d = float(input("Enter value for solution d: "))
    e = float(input("Enter value for factor e: "))
    f = float(input("Enter value for factor f: "))
    g = float(input("Enter value for factor g: "))
    h = float(input("Enter value for solution h: "))
    i = float(input("Enter value for solution i: "))
    j = float(input("Enter value for factor j: "))
    k = float(input("Enter value for factor k: "))
    l = float(input("Enter value for solution l: "))

    x = array([[a, b, c], [e, f, g], [i, j, k]])
    y = array([d, h, l])
    solution = linalg.solve(x, y)

    print(f"The solutions are x={solution[0]}; y={solution[1]}; z={solution[2]}.")


def solve_four_unknowns():
    
    print("a*x + b*y + c*z + d*w = e \nf*x + g*y + h*z + i*w = j \nk*x + l*y + m*z + n*w = o \np*x + q*y + r*z + s*w = t")

    a = float(input("Enter value for factor a: "))    
    b = float(input("Enter value for factor b: "))
    c = float(input("Enter value for factor c: "))    
    d = float(input("Enter value for factor d: "))
    e = float(input("Enter value for solution e: "))
    f = float(input("Enter value for factor f: "))
    g = float(input("Enter value for factor g: "))
    h = float(input("Enter value for factor h: "))
    i = float(input("Enter value for factor i: "))
    j = float(input("Enter value for solution j: "))
    k = float(input("Enter value for factor k: "))
    l = float(input("Enter value for factor l: "))
    m = float(input("Enter value for factor m: "))
    n = float(input("Enter value for factor n: "))
    o = float(input("Enter value for solution o: "))
    p = float(input("Enter value for factor p: "))
    q = float(input("Enter value for factor q: "))
    r = float(input("Enter value for factor r: "))
    s = float(input("Enter value for factor s: "))
    t = float(input("Enter value for solution t: "))

    x = array([[a, b, c, d], [f, g, h, i], [k, l, m, n], [p, q, r, s]])
    y = array([e, j, o, t])
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

