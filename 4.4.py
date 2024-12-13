###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
        # Convert the number to its absolute value to handle negatives
    number = abs(number)
    
    # Convert the number to a string, iterate over each character, convert to int, and sum them
    total = sum(int(digit) for digit in str(number))
    return total

any_number = int(input('Enter integer number: '))

result = sum_digits(any_number)

print(f'The sum of the digits in the number {any_number} is {result}')