from negative_check import f

def main():
    # Test sample :D
    test_cases = [
        (11, 6, -4),  # At least one negative number: True
        (5, 4, 14),   # No negative numbers: False
        (-1, -2, -3),   # All negative number: True
        (0, 0, 0),    # What if zer'os: False
    ]
    
    # Run the function for each test case and print the result
    for n1, n2, n3 in test_cases:
        print(f"f({n1}, {n2}, {n3}) returns {f(n1, n2, n3)}")

if __name__ == "__main__":
    main()
