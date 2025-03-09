def generate_pascals_triangle_row(n):
    row = [1]
    for k in range(1, n + 1):
        row.append(row[k - 1] * (n - k + 1) // k)
    return row

def main():
    print("Enter a number up to 10 to get the corresponding row of Pascal's Triangle:")
    n = int(input("Number (0-10): "))

    if 0 <= n <= 10:
        row = generate_pascals_triangle_row(n)
        print("Pascal's Triangle Row", n, ":", row)
    else:
        print("Please enter a number between 0 and 10.")

# Example usage
main()
