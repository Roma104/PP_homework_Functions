# main_program.py
from binary_checker import f

def main():
    # Test cases
    binary_number_1 = "1011101"
    binary_number_2 = "1311a10100"
    
    # Check if the numbers are valid binary numbers
    print(f"f({binary_number_1}) returns {f(binary_number_1)}")  # Expected: True
    print(f"f({binary_number_2}) returns {f(binary_number_2)}")  # Expected: False

if __name__ == "__main__":
    main()
