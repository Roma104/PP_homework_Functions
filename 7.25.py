def f(x, y):
    total_sum = 0
    
    # Iterate through the range from x to y (inclusive)
    for num in range(x, y + 1):
        if num % 6 == 0 and num % 4 != 0:  # Divisible by 6(Since it means it's both devided by 3 AND 2) but not divisible by 4 !!!! :D
            total_sum += num
            
    return total_sum

def main():
    # Test ^^
    test_cases = [
        (1, 20),
        (10, 30)
    ]
    
    # Apply the function and print results
    for x, y in test_cases:
        result = f(x, y)
        print(f'f({x},{y}) returns {result}')

if __name__ == "__main__":
    main()
