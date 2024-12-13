import keyboard  # Importing the custom module

# Reads employee's data from keyboard
first_name = keyboard.input_string('Enter first name: ')
last_name = keyboard.input_string('Enter last name: ')
age = keyboard.input_integer('Enter age: ')
salary = keyboard.input_real('Enter salary: ')
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n) ')

# Prints employee's record
print('\nDATA RECORD')
print('===========')
print('Name:', first_name, last_name)
print('Age:', age)
if not is_salary_hidden:
    print('Salary:', f'${salary:.2f}')
else:
    print('Salary: [HIDDEN]')

    
