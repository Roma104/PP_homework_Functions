def is_prime(number):
#Check if a number is prime. 
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def f(n):
#Returns the n-th prime number.
    count = 0  # Count of primes found
    candidate = 2  # Starting number to check for primes
    
    while True:
        if is_prime(candidate):
            count += 1
            if count == n:  # If n-th prime is found, return it
                return candidate
        candidate += 1

def main():
    # Test cases
    test_cases = [1, 5, 666]
    
    # Apply the function and print results
    for n in test_cases:
        print(f"f({n}) returns {f(n)}")

if __name__ == "__main__":
    main()

