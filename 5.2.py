def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_m(n):
    return n/100

def cm_to_inches(n):
    """Convert centimeters to inches."""
    return n / 2.54  # There are 2.54 cm in an inch.

def ft_in_to_cm(feet, inches):
    """Convert feet and inches to centimeters."""
    total_inches = (feet * 12) + inches  # 12 inches in a foot
    return total_inches * 2.54

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'100cm = {cm_to_inches(100):.2f} inches')
    print(f'5 feet 3 inches = {ft_in_to_cm(5, 3):.2f} cm')
