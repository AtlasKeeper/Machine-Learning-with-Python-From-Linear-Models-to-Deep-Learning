from sympy import symbols, sqrt

# Define the variable and the function
x = symbols('x')
f = 13*x**3 - x**2 - 3*x + 10

# Define critical points
x1 = (1/39) - (sqrt(118)/39)
x2 = (1/39) + (sqrt(118)/39)

# Evaluate the function at critical points and endpoints
f_x1 = f.subs(x, x1).evalf()
f_x2 = f.subs(x, x2).evalf()
f_neg4 = f.subs(x, -4).evalf()
f_4 = f.subs(x, 4).evalf()

print("f(x1) =", f_x1)
print("f(x2) =", f_x2)
print("f(-4) =", f_neg4)
print("f(4) =", f_4)

# Determine global min and max
global_min = min(f_x1, f_x2, f_neg4, f_4)
global_max = max(f_x1, f_x2, f_neg4, f_4)

print("Global minimum value of f(x) on [-4, 4] is at x =", 
      [x1, x2, -4, 4][[f_x1, f_x2, f_neg4, f_4].index(global_min)], "with value", global_min)
print("Global maximum value of f(x) on [-4, 4] is at x =", 
      [x1, x2, -4, 4][[f_x1, f_x2, f_neg4, f_4].index(global_max)], "with value", global_max)
