def f(number, even):
 #Returns the sum of either even or odd digits of the given number.
    # Convert the number to a string to iterate over its digits
    digits = str(number)
    
    # Initialize the sum variable
    digit_sum = 0
    
    # Loop through each digit
    for digit in digits:
        # Convert the digit back to an integer
        digit_value = int(digit)
        
        # Add the digit to the sum based on whether it's even or odd
        if even:
            if digit_value % 2 == 0:  # Even digit
                digit_sum += digit_value
        else:
            if digit_value % 2 != 0:  # Odd digit
                digit_sum += digit_value
    
    return digit_sum
