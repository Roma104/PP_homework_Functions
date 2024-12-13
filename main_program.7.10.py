from negative_even_counter import f

def main():
    # Test result review
    test_cases = [
        (-7, 8),   # Count of negative even numbers: 3
        (-1, 11),  # Count of negative even numbers: 0
        (-10, 0),  # Count of negative even numbers: 5
        (-8, 4)    # Count of negative even numbers: 4
    ]
    
    # Run the function for each test case and print the result
    for x, y in test_cases:
        print(f"f({x},{y}) returns {f(x, y)}")

if __name__ == "__main__":
    main()
