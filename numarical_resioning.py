from sympy import symbols, Eq, solve

# Define the variable
x = symbols('x')

# Define the equation: 4 * x + 4 * x - 92200 + x + 4200 + x = 250000
equation = Eq(4 * x + 4 * x - 92200 + x + 4200 + x, 250000)

# Solve for x
solution = solve(equation, x)

# Print the solution
print(f"The value of x is: {solution[0]}")
x = solution[0]
y = 250000

# a = symbols('a')
# b = symbols('b')
# c = symbols('c')
# d = symbols('d')

a = round(4*x/y*100)
b = round((4*x-92200)/y*100)
c = round(x/y*100)
d = round((x+4200)/y*100)

print(f"The a is: {a} %")
print(f"The b is: {b} %")
print(f"The c is: {c} %")
print(f"The d is: {d} %")
print(f"The total is: {a + b + c + d} %")
