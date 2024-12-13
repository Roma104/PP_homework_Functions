# main_program.py
from card_masker import hide

def main():
    # Sample credit card number
    card_number = "5290312400019022"
    # Mask the card number
    masked_card = hide(card_number)
    # Print the masked card number
    print(f"Masked card number: {masked_card}")

if __name__ == "__main__":
    main()
