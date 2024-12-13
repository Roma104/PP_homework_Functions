def power(x, n):
    # Our base case: x^0 = 1
    if n == 0:
        return 1
    # if not: x^n = x * x^(n-1)
    else:
        return x * power(x, n - 1)

# Example owo : calculate 5^3
result = power(5, 3)
print(f"5^3 is: {result}")
