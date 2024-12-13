def f(sentence):
#Removes all spaces from a given sentence. 
    return sentence.replace(" ", "")

def main():
    # Test >:D
    test_cases = [
        "integrated development environment",
        "A programming language is a system of notation for writing computer programs",
        "Wukong and Macaque because I love monkeys : D",
    ]
    
    # Apply the function and print results
    for sentence in test_cases:
        print(f"Original: '{sentence}'")
        print(f"Modified: '{f(sentence)}'")
        print()

if __name__ == "__main__":
    main()
