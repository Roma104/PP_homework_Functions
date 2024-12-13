def f(expression):
    result = 0
    current_num = 0
    current_op = '+'
    
    for char in expression:
        if char.isdigit():  # If the character is a digit, update current number
            current_num = int(char)
        elif char in '+-':  # character is an operator
            if current_op == '+':
                result += current_num 
            elif current_op == '-':
                result -= current_num 
            
            current_op = char  
            current_num = 0  # Reset current number for the next digit
    
    # At the end, apply the last operation with the last number
    if current_op == '+':
        result += current_num
    elif current_op == '-':
        result -= current_num
    
    return result

def main():
    # Test owo
    test_cases = [
        "2+3",
        "3+8+1",
        "2+3-4+5-0", 
    ]
    
    # Apply the function and print results
    for expr in test_cases:
        try:
            result = f(expr)
            print(f'f("{expr}") returns {result}')
        except ValueError as e:
            print(f'f("{expr}") raises an error: {e}')

if __name__ == "__main__":
    main()
