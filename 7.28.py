def f(dice):
    max_count = 1  # At least one dice roll will be there ig
    current_count = 1  # Current sequence count
    max_digit = dice[0]  # The digit that is part of the longest sequence
    current_digit = dice[0]  # The digit in the current sequence
    
    # Iterate through the string, starting from the second character
    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            # If the current digit is the same as the previous one, increment the current sequence count
            current_count += 1
        else:
            # If the current digit is different, reset current sequence count
            current_count = 1
            current_digit = dice[i]
        
        # Update the maximum sequence length if needed
        if current_count > max_count:
            max_count = current_count
            max_digit = current_digit
    
    return int(max_digit)


def main():
    # Test yet again :d
    test_cases = [
        "5233165554211",  # Expected output: 5
        "2133"             # Expected output: 3
    ]
    
    # Apply the function and print results
    for dice in test_cases:
        result = f(dice)
        print(f'f("{dice}") returns {result}')

if __name__ == "__main__":
    main()