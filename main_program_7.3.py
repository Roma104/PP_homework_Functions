# main_program.py
from month_module import month

def main():
    try:
        # Get the month number from the user
        n = int(input("Enter month number: "))
        # Call the function and display the result
        print(f"The name of month {n} is {month(n)}")
    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 12.")

if __name__ == "__main__":
    main()
