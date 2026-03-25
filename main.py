def fibonacci_series(n):
    """Generate Fibonacci series up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_series = [0, 1]
    for _ in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    
    return fib_series


def is_palindrome(number):
    """Check if a number is a palindrome."""
    num_str = str(number)
    return num_str == num_str[::-1]


def main():
    try:
        # Fibonacci input
        num_terms = int(input("Enter the number of terms for Fibonacci series: "))
        fib_series = fibonacci_series(num_terms)
        print("Fibonacci Series:", fib_series)

        # Palindrome input
        num_to_check = int(input("Enter a number to check if it is a palindrome: "))
        if is_palindrome(num_to_check):
            print(f"{num_to_check} is a palindrome number.")
        else:
            print(f"{num_to_check} is not a palindrome number.")

    except ValueError:
        print("Please enter a valid integer!")


if __name__ == "__main__":
    main()
