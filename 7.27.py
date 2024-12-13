def f(product_code):
    # Ensure the product code has exactly 4 digits
    if len(product_code) != 4:
        return False
    
    # Extract the first three digits and the fourth digit (control digit)
    first_three_digits = product_code[:3]
    control_digit = int(product_code[3])
    
    # Calculate the sum of the first three digits
    sum_of_first_three = sum(int(digit) for digit in first_three_digits)
    
    # Calculate the remainder when the sum is divided by 7
    remainder = sum_of_first_three % 7
    
    # Return True if the remainder matches the control digit
    return remainder == control_digit

def main():
    # Test time :D !
    test_cases = [
        "1082",
        "2035",
        "1114",
        "7071",
    ]
    
    # Apply the function and print results
    for code in test_cases:
        result = f(code)
        print(f'f("{code}") returns {result}')

if __name__ == "__main__":
    main()
