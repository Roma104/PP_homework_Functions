def f(n):
#Returns numbers from 1 to n as a concatenated string.
    return ''.join(str(i) for i in range(1, n + 1))
