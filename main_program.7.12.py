from asteriks import f

def main():
    # Test cases
    test_cases = [4, 1, 5, 3, 0]
    
    # Run the function for each test case and print the result
    for n in test_cases:
        print(f"f({n}) returns {f(n)}")

if __name__ == "__main__":
    main()
