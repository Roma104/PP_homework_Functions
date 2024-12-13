from aritmatic_operations import f

def main():
    # Test :)
    test_cases = [
        (2, 3, "+"),   # 5
        (2, 3, "%"),   # 2
        (2, 3, "**"),  # 8
        (2, 3, "*"),   # 6
        (2, 3, "-")    # -1
    ]
    
    # Run the function for each test case and print the result
    for number1, number2, operator in test_cases:
        print(f"f({number1}, {number2}, '{operator}') returns {f(number1, number2, operator)}")

if __name__ == "__main__":
    main()
