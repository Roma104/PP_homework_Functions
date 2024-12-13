def f(number):
  #Returns the sum of all repeated digits in a number.
    # Convert the number to a string to process its digits
    num_str = str(number)
    
    # Count occurrences of each digit
    digit_count = {}
    for digit in num_str:
        digit_count[digit] = digit_count.get(digit, 0) + 1
    
    # Calculate the sum of repeated digits (entire contribution)
    repeated_sum = 0
    for digit, count in digit_count.items():
        if count > 1:
            repeated_sum += int(digit) * count
    
    return repeated_sum


def main():
    # Test cases
    test_cases = [1027, 230335, 513553007, 666]
    
    # Apply the function and print results
    for number in test_cases:
        print(f"f({number}) returns {f(number)}")

if __name__ == "__main__":
    main()

