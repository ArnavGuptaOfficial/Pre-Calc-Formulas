# Arithmetic Functions
def arithmetic_nth_term(a, d, n):
    return a + (n - 1) * d

def arithmetic_sum(a, d, n):
    return n / 2 * (2 * a + (n - 1) * d)

def find_common_difference(a1, a2):
    return a2 - a1

# Geometric Functions
def geometric_nth_term(a, r, n):
    return a * r**(n - 1)

def geometric_sum(a, r, n):
    if r == 1:
        return a * n
    return a * (1 - r**n) / (1 - r)

def geometric_infinite_sum(a, r):
    if abs(r) < 1:
        return a / (1 - r)
    return "Diverges"

def find_common_ratio(a1, a2):
    return a2 / a1

# Main loop
while True:
    print("\n1. Arithmetic Series")
    print("2. Geometric Series")
    print("3. Exit")
    
    try:
        choice = int(input("Choose (1-3): "))
        
        if choice == 1:
            print("\n1. Find nth term")
            print("2. Find sum of n terms")
            print("3. Find common difference")
            sub_choice = int(input("Choose (1-3): "))

            if sub_choice == 1:
                a = eval(input("First term (a): "))
                d = eval(input("Common difference (d): "))
                n = eval(input("Term number (n): "))
                print("Nth term:", arithmetic_nth_term(a, d, n))

            elif sub_choice == 2:
                a = eval(input("First term (a): "))
                d = eval(input("Common difference (d): "))
                n = eval(input("Number of terms (n): "))
                print("Sum:", arithmetic_sum(a, d, n))

            elif sub_choice == 3:
                a1 = eval(input("First term (a1): "))
                a2 = eval(input("Second term (a2): "))
                print("Common difference (d):", find_common_difference(a1, a2))

            else:
                print("Invalid choice.")

        elif choice == 2:
            print("\n1. Find nth term")
            print("2. Find sum of n terms")
            print("3. Infinite sum")
            print("4. Find common ratio")
            sub_choice = int(input("Choose (1-4): "))

            if sub_choice == 1:
                a = eval(input("First term (a): "))
                r = eval(input("Common ratio (r): "))
                n = eval(input("Term number (n): "))
                print("Nth term:", geometric_nth_term(a, r, n))

            elif sub_choice == 2:
                a = eval(input("First term (a): "))
                r = eval(input("Common ratio (r): "))
                n = eval(input("Number of terms (n): "))
                print("Sum:", geometric_sum(a, r, n))

            elif sub_choice == 3:
                a = eval(input("First term (a): "))
                r = eval(input("Common ratio (r): "))
                print("Infinite sum:", geometric_infinite_sum(a, r))

            elif sub_choice == 4:
                a1 = eval(input("First term (a1): "))
                a2 = eval(input("Second term (a2): "))
                print("Common ratio (r):", find_common_ratio(a1, a2))

            else:
                print("Invalid choice.")

        elif choice == 3:
            print("Goodbye!")
            break  # Exit

        else:
            print("Invalid input. Try again.")

    except:
        print("Error: Enter valid numbers!")
