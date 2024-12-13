def f(name):
#Returns the acronym of the given text.
    words = name.split()  # Split the text into words
    acronym = "".join(word[0] for word in words)  # Take the first letter of each word and capitalize it
    return acronym

def main():
    # Test 

    test_cases = [
        "Internet of Things",
        "For Your Information",
        "Python",
        "Sun Wukong THE Great Sage Equal to Heaven",
        "Six Eard Macaque",
    ]
    
    # Apply the function and print results
    for name in test_cases:
        result = f(name)
        print(f'f("{name}") returns "{result}"')

if __name__ == "__main__":
    main()
