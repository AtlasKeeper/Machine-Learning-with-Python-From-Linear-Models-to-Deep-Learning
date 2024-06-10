from math import sqrt

# Calculate critical points
x1 = (1/39) - (sqrt(118)/39)
x2 = (1/39) + (sqrt(118)/39)

# Calculate the second derivatives at the critical points
f_double_prime_x1 = -2 * sqrt(118)
f_double_prime_x2 = 2 * sqrt(118)

print(f"x1 = {x1:.4f}")
print(f"x2 = {x2:.4f}")
print(f"f''(x1) = {f_double_prime_x1:.4f}")
print(f"f''(x2) = {f_double_prime_x2:.4f}")
