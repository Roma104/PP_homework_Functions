# month_module.py
def month(n):
#Returns the name of the month corresponding to the month number.
    result = ''
    if n == 1:
        result = 'Styczeń'
    elif n == 2:
        result = 'Luty'
    elif n == 3:
        result = 'Marzec'
    elif n == 4:
        result = 'Kwiecień'
    elif n == 5:
        result = 'Maj'
    elif n == 6:
        result = 'Czerwienc'
    elif n == 7:
        result = 'Lipiec'
    elif n == 8:
        result = 'Sierpień'
    elif n == 9:
        result = 'Wrzesień'
    elif n == 10:
        result = 'Październik'
    elif n == 11:
        result = 'Listopad'
    elif n == 12:
        result = 'Grudzień'
    else:
        result = "Invalid month number. Please enter a number between 1 and 12."

    return result
