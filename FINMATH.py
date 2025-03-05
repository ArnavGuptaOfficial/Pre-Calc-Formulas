import math

# Function to calculate monthly payment (M)
def monthly_payment(P, annual_rate, years):
    r = (annual_rate / 100) / 12  # Convert annual rate to monthly rate
    n = years * 12  # Convert years to months
    if r == 0:
        return P / n  # No interest case
    return P * r * (1 + r)**n / ((1 + r)**n - 1)

# Function to calculate loan amount (P)
def loan_amount(M, annual_rate, years):
    r = (annual_rate / 100) / 12
    n = years * 12
    if r == 0:
        return M * n
    return M * ((1 + r)**n - 1) / (r * (1 + r)**n)

# Function to calculate interest rate (approximate solution)
def interest_rate(P, M, years):
    n = years * 12
    low = 0.01
    high = 100
    while high - low > 0.0001:  # Binary search to find rate
        mid = (high + low) / 2
        r = (mid / 100) / 12
        estimated_M = P * r * (1 + r)**n / ((1 + r)**n - 1)
        if estimated_M > M:
            high = mid
        else:
            low = mid
    return round((high + low) / 2, 4)

# Function to calculate number of years (Years)
def number_of_years(P, M, annual_rate):
    r = (annual_rate / 100) / 12
    if r == 0:
        return P / M / 12
    return math.log(M / (M - P * r)) / (12 * math.log(1 + r))

# Main loop
while True:
    print("\nMortgage Calculator - TI-84 Python CE")
    print("1. Find Monthly Payment")
    print("2. Find Loan Amount")
    print("3. Find Interest Rate")
    print("4. Find Number of Years")
    print("5. Exit")
    
    try:
        choice = int(input("Choose an option (1-5): "))

        if choice == 1:
            P = eval(input("Property Value or Loan Amount (P): "))
            annual_rate = eval(input("Annual Interest Rate (%): "))
            years = eval(input("Loan Term (Years): "))
            print("Monthly Payment:", round(monthly_payment(P, annual_rate, years), 2))

        elif choice == 2:
            M = eval(input("Monthly Payment (M): "))
            annual_rate = eval(input("Annual Interest Rate (%): "))
            years = eval(input("Loan Term (Years): "))
            print("Loan Amount:", round(loan_amount(M, annual_rate, years), 2))

        elif choice == 3:
            P = eval(input("Loan Amount (P): "))
            M = eval(input("Monthly Payment (M): "))
            years = eval(input("Loan Term (Years): "))
            print("Estimated Interest Rate (%):", interest_rate(P, M, years))

        elif choice == 4:
            P = eval(input("Loan Amount (P): "))
            M = eval(input("Monthly Payment (M): "))
            annual_rate = eval(input("Annual Interest Rate (%): "))
            print("Loan Term (Years):", round(number_of_years(P, M, annual_rate), 2))

        elif choice == 5:
            print("Goodbye!")
            break  # Exit loop

        else:
            print("Invalid input. Try again.")

    except:
        print("Error: Enter valid numbers!")
