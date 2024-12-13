def sum_natural(n):
    # Our base: when n is 1, return 1
    if n == 1:
        return 1
    # Recursive case: sum n and the sum of numbers before it
    else:
        return n + sum_natural(n - 1)

# Example: calculate the sum of natural numbers from 1 to 10
result = sum_natural(10)
print(f"Sum of natural numbers from 1 to 10 is: {result}")
