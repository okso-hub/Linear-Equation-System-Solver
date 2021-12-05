# Linear Equation System Solver

This program takes a linear equation system and solves for all unknown variables.

## How the program works

Let's say you need to solve the given linear equation system:

2x + 4y = 10  
 x +  y = 4

After directing to the directory where the program is stored, simply run the program using the command  `python main.py`.

This brings up the following line:

```
python main.py
How many unknowns are you looking for? 
```

In our case, we have two unknwons (x & y). 

```
python main.py
How many unknowns are you looking for? 2
```
Then, you will have to input the factors of you unknowns.

```
python main.py
How many unknowns are you looking for? 2
a*x + b*y = c 
d*x + e*y = f
Enter value for factor a: 2
Enter value for factor b: 4
Enter value for product c: 10
Enter value for factor d: 1
Enter value for factor e: 1
Enter value for solution f: 4
```

After entering the last parameter, you will get the solution.

```
python main.py
How many unknowns are you looking for? 2
a*x + b*y = c 
d*x + e*y = f
Enter value for factor a: 2
Enter value for factor b: 4
Enter value for product c: 10
Enter value for factor d: 1
Enter value for factor e: 1
Enter value for solution f: 4
The solution is x=3.0; y=1.0
```
