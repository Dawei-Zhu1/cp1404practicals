"""
Practice 4 - List Exercises
Student Name: Dawei Zhu - 14613428
Student Email: dawei.zhu@my.jcu.edu.au
"""
QUANTITY_OF_NUMBERS = 5


def main():
    # Basic list operations
    numbers = []
    for i in range(QUANTITY_OF_NUMBERS):
        number = int(input("Number: "))
        numbers.append(number)

    print('The first number is', numbers[0])
    print('The last number is', numbers[-1])
    print('The smallest number is', min(numbers))
    print('The largest number is', max(numbers))
    print('The average number is', sum(numbers) / len(numbers))
    print('=' * 12)

    # Woefully inadequate security checker
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    user_entry = input("Enter your name: ")
    if user_entry in usernames:
        print('Access granted')
    else:
        print('Access denied')


main()
