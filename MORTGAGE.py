import math

def calculate_monthly_payment(PV, r, years):
    monthly_rate = r / 100 / 12
    total_payments = years * 12
    monthly_payment = (PV * monthly_rate * (1 + monthly_rate) ** total_payments) / ((1 + monthly_rate) ** total_payments - 1)
    return monthly_payment, total_payments

def mortgage_calculator():
    print("Mortgage Calculator")
    print("1. Calculate Monthly Mortgage Payment and Principal/Interest Breakdown")
    print("2. Exit")
    
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        PV = float(input("Loan amount (Principal): "))
        r = float(input("Annual interest rate (in percent): "))
        years = int(input("Loan term (in years): "))
        payment_number = int(input("Payment number to check (e.g., 10 for the 10th payment): "))
        
        monthly_payment, total_payments = calculate_monthly_payment(PV, r, years)
        total_paid = monthly_payment * 12*years
        print("Monthly Payment: ${:.2f}".format(monthly_payment))
        print("Total Amount Paid Over the Loan Term: ${:.2f}".format(total_paid))
        
        remaining_balance = PV
        monthly_rate = r / 100 / 12
        
        for i in range(1, payment_number + 1):
            interest_payment = remaining_balance * monthly_rate
            principal_payment = monthly_payment - interest_payment
            remaining_balance -= principal_payment
        
        print("Payment Number:", payment_number)
        print("Principal Portion: ${:.2f}".format(principal_payment))
        print("Interest Portion: ${:.2f}".format(interest_payment))
    elif choice == 2:
        print("Goodbye!")
    else:
        print("Invalid choice. Please select 1 or 2.")

# Example usage
mortgage_calculator()
