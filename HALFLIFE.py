import math

def half_life_calculator():
    print("Half-Life Calculator")
    print("Choose what you would like to find:")
    print("1. Half-Life of the substance (in years)")
    print("2. Time passed (in years)")
    print("3. Percent of the substance left")
    print("4. Amount of the substance left")
    print("5. Initial amount of the substance")
    
    choice = int(input("Enter your choice (1, 2, 3, 4, or 5): "))

    if choice == 1:
        initial_amount = float(input("Enter the initial amount: "))
        final_amount = float(input("Enter the final amount: "))
        time = float(input("Enter the time passed in years: "))
        half_life = time / (math.log(initial_amount / final_amount) / math.log(2))
        print("Half-Life: {:.3f} years".format(half_life))
    
    elif choice == 2:
        initial_amount = float(input("Enter the initial amount: "))
        final_amount = float(input("Enter the final amount: "))
        half_life = float(input("Enter the half-life in years: "))
        time = half_life * (math.log(initial_amount / final_amount) / math.log(2))
        print("Time Passed: {:.3f} years".format(time))
    
    elif choice == 3:
        initial_amount = float(input("Enter the initial amount: "))
        final_amount = float(input("Enter the final amount: "))
        percent_left = (final_amount / initial_amount) * 100
        print("Percent Left: {:.3f}%".format(percent_left))
    
    elif choice == 4:
        initial_amount = float(input("Enter the initial amount: "))
        half_life = float(input("Enter the half-life in years: "))
        time = float(input("Enter the time passed in years: "))
        amount_left = initial_amount * (0.5) ** (time / half_life)
        print("Amount Left: {:.3f}".format(amount_left))

    elif choice == 5:
        final_amount = float(input("Enter the final amount: "))
        half_life = float(input("Enter the half-life in years: "))
        time = float(input("Enter the time passed in years: "))
        initial_amount = final_amount / (0.5 ** (time / half_life))
        print("Initial Amount: {:.3f}".format(initial_amount))
    
    else:
        print("Invalid choice. Please select a number between 1 and 5.")

# Example usage
half_life_calculator()
