def f(palindrome):
#Checks if the given expression is a palindrome.   MY GOAT BALL IS CALLED PALINDROM AAAAAAAA
    # Clean the input: remove non-alphanumeric characters and convert to lowercase
    cleaned = "".join(char.lower() for char in palindrome if char.isalnum())
    
    # Check if the cleaned string is the same as its reverse
    return cleaned == cleaned[::-1]

def main():
    # Test !
    test_cases = [
        ("radar", True),
        ("12-11-21", True),
        ("book", False),
        ("A to kanapa pana kota", True),
        ("Not a palindrome", False),
    ]
    
    # Run the function for each test case and print the results
    for expression, expected in test_cases:
        result = f(expression)
        print(f"f('{expression}') returns {result})")

if __name__ == "__main__":
    main()

