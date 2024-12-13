def f(n):
#Returns the n-th value of the Fibonacci sequence.
    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    # Calculate Fibonacci numbers up to the n-th value
    for _ in range(3, n + 1):
        a, b = b, a + b
    
    return b

def main():
    # Test :)
    test_cases = [5, 9, 1, 2, 10]
    
    # Run the function for each test case and print the result
    for n in test_cases:
        print(f"f({n}) returns {f(n)}")

if __name__ == "__main__":
    main()

