import math

def calculate_side(a, b, angle_C):
    # Convert angle to radians
    angle_C_rad = math.radians(angle_C)
    # Use the Law of Cosines to calculate the side length
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(angle_C_rad))
    return c

def calculate_angle(a, b, c):
    # Use the Law of Cosines to calculate the angle (in radians)
    angle_C_rad = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
    # Convert radians to degrees
    angle_C = math.degrees(angle_C_rad)
    return angle_C

def law_of_cosines():
    print("What would you like to calculate?")
    print("1: Find the length of a side")
    print("2: Find an angle")
    
    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        angle_C = float(input("Enter the angle (in degrees) between sides a and b: "))
        c = calculate_side(a, b, angle_C)
        print("The length of side c is:", c)
    
    elif choice == 2:
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        c = float(input("Enter the length of side c: "))
        angle_C = calculate_angle(a, b, c)
        print("The angle (in degrees) is:", angle_C)
    
    else:
        print("Invalid choice. Please select 1 or 2.")

# Run the function
law_of_cosines()
