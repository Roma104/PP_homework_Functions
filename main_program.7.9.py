from digit_sum import f

def main():
    # Test sample
    numbers = [
        (3124, True),    # Sum of even digits: 6
        (3124, False),   # Sum of odd digits: 4
        (20576, False),  # Sum of odd digits: 12
        (20576, True),   # Sum of even digits: 8
        (13115, True)    # Sum of even digits: 0
    ]
    
    # Run the function for each test case and print the result
    for number, even in numbers:
        print(f"f({number},{even}) returns {f(number, even)}")

if __name__ == "__main__":
    main()
