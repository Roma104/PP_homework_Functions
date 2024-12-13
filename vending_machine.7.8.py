# vending_machine.py
def f(amount_to_pay):
#Returns the minimum number of coins needed to pay the given amount."""
    coins = 0
    
    # Use as many 5 PLN coins as possible
    coins += amount_to_pay // 5
    amount_to_pay %= 5
    
    # Use as many 2 PLN coins as possible
    coins += amount_to_pay // 2
    amount_to_pay %= 2
    
    # Use 1 PLN coins for the remainder
    coins += amount_to_pay // 1
    
    return coins

def main():
    # Test sample
    amounts = [23, 8, 2, 0]
    
    # Check the minimum number of coins for each amount
    for amount in amounts:
        print(f"f({amount}) returns {f(amount)}")

if __name__ == "__main__":
    main()