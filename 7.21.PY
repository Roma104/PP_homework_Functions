def f(number1, number2, number3):
#Returns the difference between the largest and smallest of three numbers.
    largest = max(number1, number2, number3)
    smallest = min(number1, number2, number3)
    return largest - smallest


def main():
    # Test :3
    test_cases = [
        (7, 4, 9),
        (2, 12, 8),
        (10, 10, 10), 
        (-5, 0, 5),    
    ]
    
    # Apply the function and print results
    for numbers in test_cases:
        result = f(*numbers)
        print(f"f{numbers} returns {result}")

if __name__ == "__main__":
    main()
