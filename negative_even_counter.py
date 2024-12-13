
def f(x, y):
 #Returns the number of negative even numbers in the range <x, y>.
    count = 0
    for num in range(x, y):
        if num < 0 and num % 2 == 0:
            count += 1
    return count
