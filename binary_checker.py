# binary_checker.py
def f(binary_number):
##Returns True if the string represents a valid binary number, False otherwise.
    # Check if all characters in the string are either '0' or '1'
    return all(char in '01' for char in binary_number)
