

def findPayment(FV, r, n, t, b):
    return ((FV*(a))/(x))*b



# Main loop
while True:
 
    print("1. Find Payment Amount")
    print("2. Exit")
    
    try:
        choice = int(input("Choose (1-2): "))
        
        
        
        if choice == 1:
            FV = eval(input("Future value of the annuity: "))
            n = eval(input("Compounded how many times a year: "))
            r = eval(input("Annual interest rate (in percent): ")) / 100
            t = eval(input("Number of years: "))
            b = 1+(r/n)
            a = 1-b
            x = (1/b)**(t*n)
            print("Payment Amount:", findPayment(FV, r, n, t, b, x , a ))

        
       
        elif choice == 2:
            print("Goodbye!")
            break  # Exit

        else:
            print("Invalid input. Try again.")

    except ValueError:
        print("Error: Enter valid numbers!")
