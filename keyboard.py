# Module to handle different types of input

def input_string(message):
   #Reads and returns a string from the keyboard.
    return input(message)

def input_integer(message):
    #Reads and returns an integer from the keyboard.
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def input_real(message):
    #Reads and returns a real number (float) from the keyboard.
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a real number.")

def input_boolean(message):
    #Reads and returns a boolean value based on 'y' or 'n' input.
    while True:
        response = input(message).strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")