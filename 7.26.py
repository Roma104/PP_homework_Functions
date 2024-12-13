def f(text):
    # Join all characters in the text with a dash
    return '-'.join(text)

def main():
    # Test :3
    test_cases = [
        "University",
        "UE",
        "x",
        "",
    ]
    
    # Apply the function and print results
    for text in test_cases:
        result = f(text)
        print(f'f("{text}") returns "{result}"')

if __name__ == "__main__":
    main()
