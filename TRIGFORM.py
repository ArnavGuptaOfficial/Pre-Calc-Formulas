import math

def double_angle_formulas(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    
    sin_double = 2 * math.sin(angle_radians) * math.cos(angle_radians)
    cos_double = math.cos(angle_radians)**2 - math.sin(angle_radians)**2
    tan_double = 2 * math.tan(angle_radians) / (1 - math.tan(angle_radians)**2)

    print("Double Angle Formulas:")
    print(f"sin(2 * {angle_degrees}°) = {sin_double:.3f}")
    print(f"cos(2 * {angle_degrees}°) = {cos_double:.3f}")
    print(f"tan(2 * {angle_degrees}°) = {tan_double:.3f}")

def half_angle_formulas(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    
    sin_half = math.sqrt((1 - math.cos(angle_radians)) / 2)
    cos_half = math.sqrt((1 + math.cos(angle_radians)) / 2)
    tan_half = math.sqrt((1 - math.cos(angle_radians)) / (1 + math.cos(angle_radians)))
    
    print("Half Angle Formulas:")
    print(f"sin({angle_degrees}° / 2) = {sin_half:.3f}")
    print(f"cos({angle_degrees}° / 2) = {cos_half:.3f}")
    print(f"tan({angle_degrees}° / 2) = {tan_half:.3f}")

def sum_difference_formulas(angle_a_degrees, angle_b_degrees):
    angle_a_radians = math.radians(angle_a_degrees)
    angle_b_radians = math.radians(angle_b_degrees)

    sin_sum = math.sin(angle_a_radians) * math.cos(angle_b_radians) + math.cos(angle_a_radians) * math.sin(angle_b_radians)
    sin_diff = math.sin(angle_a_radians) * math.cos(angle_b_radians) - math.cos(angle_a_radians) * math.sin(angle_b_radians)
    
    cos_sum = math.cos(angle_a_radians) * math.cos(angle_b_radians) - math.sin(angle_a_radians) * math.sin(angle_b_radians)
    cos_diff = math.cos(angle_a_radians) * math.cos(angle_b_radians) + math.sin(angle_a_radians) * math.sin(angle_b_radians)
    
    tan_sum = (math.tan(angle_a_radians) + math.tan(angle_b_radians)) / (1 - math.tan(angle_a_radians) * math.tan(angle_b_radians))
    tan_diff = (math.tan(angle_a_radians) - math.tan(angle_b_radians)) / (1 + math.tan(angle_a_radians) * math.tan(angle_b_radians))

    print("Sum and Difference Formulas:")
    print(f"sin({angle_a_degrees}° + {angle_b_degrees}°) = {sin_sum:.3f}")
    print(f"sin({angle_a_degrees}° - {angle_b_degrees}°) = {sin_diff:.3f}")
    print(f"cos({angle_a_degrees}° + {angle_b_degrees}°) = {cos_sum:.3f}")
    print(f"cos({angle_a_degrees}° - {angle_b_degrees}°) = {cos_diff:.3f}")
    print(f"tan({angle_a_degrees}° + {angle_b_degrees}°) = {tan_sum:.3f}")
    print(f"tan({angle_a_degrees}° - {angle_b_degrees}°) = {tan_diff:.3f}")

def main():
    print("Trigonometric Functions")
    print("1. Double Angle Formulas")
    print("2. Half Angle Formulas")
    print("3. Sum and Difference Formulas")
    
    choice = int(input("Enter your choice (1, 2, or 3): "))

    if choice == 1:
        angle_degrees = float(input("Enter the angle in degrees: "))
        double_angle_formulas(angle_degrees)
    elif choice == 2:
        angle_degrees = float(input("Enter the angle in degrees: "))
        half_angle_formulas(angle_degrees)
    elif choice == 3:
        angle_a_degrees = float(input("Enter the first angle in degrees: "))
        angle_b_degrees = float(input("Enter the second angle in degrees: "))
        sum_difference_formulas(angle_a_degrees, angle_b_degrees)
    else:
        print("Invalid choice. Please select either 1, 2, or 3.")

# Run the main function
main()
