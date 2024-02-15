"""
Prac 03 - Files
Student Name: Dawei Zhu - 14613428
Student Email: dawei.zhu@my.jcu.edu.au
"""
FILE1_DIRECTORY = './name.txt'
FILE2_DIRECTORY = './number.txt'


def main():
    # 1. Write the name into name.txt
    f = open(FILE1_DIRECTORY, 'w')
    username = input('Enter your name: ')
    f.write(username)
    f.close()
    print()

    # 2. Print the name in name.txt
    with open(FILE1_DIRECTORY, 'r') as f:
        print(f'Your name is {f.read()}')
    print()

    # 3. Read first 2 lines/numbers in number.txt
    with open(FILE2_DIRECTORY, 'r') as f:
        total = 0
        for i in range(2):
            total += int(f.readline())
    # assert total == 59
    print(f'The sum of first 2 number in "{FILE2_DIRECTORY} is {total}.')
    print()

    # 4. Print ALL line of number.txt
    total = sum_all_numbers_in_the_file(FILE2_DIRECTORY)

    print(f'The sum of all numbers in the file is {total}.')


def sum_all_numbers_in_the_file(filename):
    """
    Get file directory and sum all numbers in it, one line for each number
    """
    total = 0
    with open(filename, 'r') as f:
        for line in f:
            total += int(line)
    return total


main()
