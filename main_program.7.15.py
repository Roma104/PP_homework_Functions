from people_in_room import f

def main():
    # Test !
    test_cases = [
        ("+-+++-+---", True),  # At least 3 people at the same time
        ("+-+-+-+-", False),   # not 3 people at the same time
        ("+-++-+-", False),   # not 3 people at the same time
        ("+-++-++-+---", True),# At least 3 people at the same time
    ]
    
    # Run the function for each test case and print the result
    for detector, expected in test_cases:
        result = f(detector)
        print(f"f('{detector}') returns {result})")

if __name__ == "__main__":
    main()
