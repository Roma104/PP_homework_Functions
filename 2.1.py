###
# Program for testing built-in functions
#

#the largest number: 7,5,6,3,8,2
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

#the smallest number: 4,7,2,3,9,8
min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

#length of the phrase: "computer science"
str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

#reads letter read from the keyboard
letter = input('Enter letter from keyboard:')
print('Letter from a keybord is:', letter)

#number representing the string "20303"
number = int('20303')
print('number representing the string:', number)

#binary string representing decimal number 304
binary = bin(304)
print('binary string representing decimal number 304:', binary)

#hexadecimal string representing decimal number 304
hexadecimal = hex(304)
print('hexadecimal string representing decimal number 304:', hexadecimal)


#integer representing the Unicode code of the € sign
unicode = ord('€')
print('integer representing the Unicode code of the € sign is:', unicode)

#absolute value of -17
absolute = abs(-17)
print('absolute valuse of -17 is:', absolute)