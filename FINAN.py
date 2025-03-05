# Future value of an annuity functions
def futureValue(P, r, n, t):
    return P * ((1 + r/n)**(n*t) - 1) / (r/n)

def findPayment(FV, r, n, t):
    return FV / (((1 + r/n)**(n*t) - 1) / (r/n))

def findInterestRate(FV, P, n, t):
    # For simplicity, this function will use an iterative approach to find r
    r = 0.01  # Initial guess
    while futureValue(P, r, n, t) < FV:
        r += 0.0001
    return r

def findCompoundingPeriods(FV, P, r, t):
    # This function will use an iterative approach to find n
    n = 1  # Initial guess
    while futureValue(P, r, n, t) < FV:
        n += 1
    return n

def findYears(FV, P, r, n):
    # This function will use an iterative approach to find t
    t = 0.1  # Initial guess
    while futureValue(P, r, n, t) < FV:
        t += 0.1
    return t


# Main loop
while True:
    print("1. Find Future Value")
    print("2. Find Payment Amount")
    print("3. Find Interest Rate")
    print("4. Find Compounding Periods")
    print("5. Find Number of Years")
    print("6. Exit")
    
    try:
        choice = int(input("Choose (1-6): "))
        
        if choice == 1:
            P = eval(input("Payment amount per period: "))
            n = eval(input("Compounded how many times a year: "))
            r = eval(input("Annual interest rate (in percent): ")) / 100
            t = eval(input("Number of years: "))
            print("Future Value:", futureValue(P, r, n, t))
        
        elif choice == 2:
            FV = eval(input("Future value of the annuity: "))
            n = eval(input("Compounded how many times a year: "))
            r = eval(input("Annual interest rate (in percent): ")) / 100
            t = eval(input("Number of years: "))
            print("Payment Amount:", findPayment(FV, r, n, t))
        
        elif choice == 3:
            FV = eval(input("Future value of the annuity: "))
            P = eval(input("Payment amount per period: "))
            n = eval(input("Compounded how many times a year: "))
            t = eval(input("Number of years: "))
            print("Interest Rate:", findInterestRate(FV, P, n, t) * 100, "%")
        
        elif choice == 4:
            FV = eval(input("Future value of the annuity: "))
            P = eval(input("Payment amount per period: "))
            r = eval(input("Annual interest rate (in percent): ")) / 100
            t = eval(input("Number of years: "))
            print("Compounding Periods:", findCompoundingPeriods(FV, P, r, t))
        
        elif choice == 5:
            FV = eval(input("Future value of the annuity: "))
            P = eval(input("Payment amount per period: "))
            r = eval(input("Annual interest rate (in percent): ")) / 100
            n = eval(input("Compounded how many times a year: "))
            print("Number of Years:", findYears(FV, P, r, n))
        
        elif choice == 6:
            print("Goodbye!")
            break  # Exit

        else:
            print("Invalid input. Try again.")

    except ValueError:
        print("Error: Enter valid numbers!")
