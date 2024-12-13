# main_program.py
from range_checker import is_in_range

def main():
    # Input the number and range
    number = int(input("A number: "))
    x = int(input("Enter x(lower range):"))
    y = int(input("Enter y(upper range):"))  # Define the range
        # Check if the number is in the range
           
    result = is_in_range(number, x, y)

    print(f"Number {number} in the range <{x},{y}>: {'yes' if result else 'no'}")


if __name__ == "__main__":
    main()
    