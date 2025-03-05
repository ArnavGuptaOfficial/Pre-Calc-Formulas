import math

def EXPGROWTH():
    print("Select what you want to calculate:")
    print("1. Final Value")
    print("2. Time")
    print("3. Initial Value")
    
    choice = input("Enter the number of your choice (1, 2, or 3): ")

    if choice == "1":
        # Calculate final value
        y0 = float(input("Enter the initial value (y₀): "))
        k = float(input("Enter the growth rate (k) as a decimal (e.g., 0.05 for 5%): "))
        t = float(input("Enter the time period (t): "))
        
        final_value = y0 * math.exp(k * t)
        print(f"The final value after exponential growth is: {final_value:.2f}")

    elif choice == "2":
        # Calculate time
        y0 = float(input("Enter the initial value (y₀): "))
        final_value = float(input("Enter the final value: "))
        k = float(input("Enter the growth rate (k) as a decimal (e.g., 0.05 for 5%): "))
        
        if final_value <= 0 or y0 <= 0:
            print("Initial and final values must be greater than zero.")
        else:
            t = math.log(final_value / y0) / k
            print(f"The time period required is: {t:.2f} units")

    elif choice == "3":
        # Calculate initial value
        final_value = float(input("Enter the final value: "))
        k = float(input("Enter the growth rate (k) as a decimal (e.g., 0.05 for 5%): "))
        t = float(input("Enter the time period (t): "))
        
        if final_value <= 0:
            print("Final value must be greater than zero.")
        else:
            y0 = final_value / math.exp(k * t)
            print(f"The initial value is: {y0:.2f}")

    else:
        print("Invalid input. Please select 1, 2, or 3.")

# Example usage:
if __name__ == "__main__":
    EXPGROWTH()
