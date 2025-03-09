def calculateMonthlyPayment(P, annual_rate, years):
    monthly_rate = annual_rate / 100 / 12
    total_payments = years * 12
    monthly_payment = (P * monthly_rate * (1 + monthly_rate) ** total_payments) / ((1 + monthly_rate) ** total_payments - 1)
    return monthly_payment

# Main loop
while True:
    print("1. Calculate Monthly Mortgage Payment")
    print("2. Exit")
    
    try:
        choice = int(input("Choose (1-2): "))
        
        if choice == 1:
            P = float(input("Loan amount (Principal): "))
            annual_rate = float(input("Annual interest rate (in percent): "))
            years = int(input("Loan term (in years): "))
            monthly_payment = calculateMonthlyPayment(P, annual_rate, years)
            print(f"Monthly Payment: ${monthly_payment:.2f}")
        elif choice == 2:
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")
    except ValueError:
        print("Error: Enter valid numbers!")
