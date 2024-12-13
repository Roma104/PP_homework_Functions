# card_masker.py
def hide(card_number):
#Masks the credit card number, showing only the first two and last four digits.
    return card_number[:2] + '*' * 10 + card_number[-4:]
