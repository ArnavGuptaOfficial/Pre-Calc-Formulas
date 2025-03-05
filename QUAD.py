import math

print("Quadratic Formula Solver")
print("Equation: ax^2 + bx + c = 0")

# Input coefficients
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Calculate discriminant
discriminant = b**2 - 4*a*c

# Check discriminant value
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Roots are real and distinct:")
    print("x1 =", round(root1, 2), "x2 =", round(root2, 2))
elif discriminant == 0:
    root = -b / (2*a)
    print("Roots are real and equal:")
    print("x =", round(root, 2))
else:
    real_part = -b / (2*a)
    imag_part = math.sqrt(-discriminant) / (2*a)
    print("Roots are complex:")
    print("x1 =", round(real_part, 2), "+", round(imag_part, 2), "i")
    print("x2 =", round(real_part, 2), "-", round(imag_part, 2), "i")
