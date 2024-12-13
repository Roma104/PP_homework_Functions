# main_program.py
from letter_counter import count_letter

def main():
    # Define the text to analyze
    text = "You never get a second chance to make a first impression"
    # Define the letter to count
    letter = 'e'
    # Call the function and display the result
    result = count_letter(text, letter)
    print(f"The number of letter '{letter}': {result}")

if __name__ == "__main__":
    main()
