def f(password):
 
    #Validates a password IF:
    #- Must be at least 6 characters long.
    #- All characters in the password must be unique.

    if len(password) < 6:
        return False  # Password is too short
    if len(set(password)) != len(password):
        return False  # Duplicate characters found
    return True

def main():
    # Test cases
    test_cases = [
        "ax15",
        "book123",
        "A2water3",
        "qwerty",
        "",
        "SunWUkoNg"
    ]
    
    # Apply the function and print results
    for pwd in test_cases:
        result = f(pwd)
        print(f'f("{pwd}") returns {result}')

if __name__ == "__main__":
    main()
