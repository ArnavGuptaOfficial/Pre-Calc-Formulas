import math

def calculate_growth():
    print("What would you like to calculate?")
    print("1: Final Amount")
    print("2: Initial Amount")
    print("3: Rate of Growth")
    print("4: Time Passed")
    
    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        initial_amount = float(input("Enter the initial amount: "))
        rate_of_growth = float(input("Enter the rate of growth: "))
        time_passed = float(input("Enter the time passed: "))
        final_amount = initial_amount * math.e ** (rate_of_growth * time_passed)
        print("Final Amount:", final_amount)

    elif choice == 2:
        final_amount = float(input("Enter the final amount: "))
        rate_of_growth = float(input("Enter the rate of growth: "))
        time_passed = float(input("Enter the time passed: "))
        initial_amount = final_amount / (math.e ** (rate_of_growth * time_passed))
        print("Initial Amount:", initial_amount)

    elif choice == 3:
        initial_amount = float(input("Enter the initial amount: "))
        final_amount = float(input("Enter the final amount: "))
        time_passed = float(input("Enter the time passed: "))
        rate_of_growth = math.log(final_amount / initial_amount) / time_passed
        print("Rate of Growth:", rate_of_growth)

    elif choice == 4:
        initial_amount = float(input("Enter the initial amount: "))
        final_amount = float(input("Enter the final amount: "))
        rate_of_growth = float(input("Enter the rate of growth: "))
        time_passed = math.log(final_amount / initial_amount) / rate_of_growth
        print("Time Passed:", time_passed)

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

# Run the function
calculate_growth()
