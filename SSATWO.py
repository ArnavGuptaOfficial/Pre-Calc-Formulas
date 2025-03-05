import math

def sas_solver():
    print("SAS Triangle Solver")
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    C = float(input("Enter angle C (degrees): "))
    C_rad = math.radians(C)
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C_rad))
    A = math.degrees(math.asin((a * math.sin(C_rad)) / c))
    B = 180 - C - A
    print("Results:")
    print("Side c =", round(c, 2))
    print("Angle A =", round(A, 2), "degrees")
    print("Angle B =", round(B, 2), "degrees")

def ssa_solver():
    print("SSA Triangle Solver")
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    A = float(input("Enter angle A (degrees): "))
    A_rad = math.radians(A)

    try:
        # Calculate possible angle B (first solution)
        B_rad1 = math.asin(b * math.sin(A_rad) / a)
        B1 = math.degrees(B_rad1)
        C1 = 180 - A - B1
        c1 = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(C1)))

        # Check for a second possible solution
        B2 = 180 - B1
        if A + B2 < 180:  # Second solution is valid only if the sum of angles is < 180
            C2 = 180 - A - B2
            c2 = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(C2)))

            print("Results (Two Solutions):")
            print("Solution 1:")
            print("Angle B =", round(B1, 2), "degrees")
            print("Angle C =", round(C1, 2), "degrees")
            print("Side c =", round(c1, 2))
            print("Solution 2:")
            print("Angle B =", round(B2, 2), "degrees")
            print("Angle C =", round(C2, 2), "degrees")
            print("Side c =", round(c2, 2))
        else:
            print("Results (One Solution):")
            print("Angle B =", round(B1, 2), "degrees")
            print("Angle C =", round(C1, 2), "degrees")
            print("Side c =", round(c1, 2))

    except ValueError:
        print("No solution is possible with the given inputs.")

print("Choose a triangle case to solve:")
print("1: SAS (Side-Angle-Side)")
print("2: SSA (Side-Side-Angle)")
choice = int(input("Enter choice (1 or 2): "))

if choice == 1:
    sas_solver()
elif choice == 2:
    ssa_solver()
else:
    print("Invalid choice!")
