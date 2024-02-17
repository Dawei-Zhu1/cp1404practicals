"""
Practice 4 - List Warmup
Student Name: Dawei Zhu - 14613428
Student Email: dawei.zhu@my.jcu.edu.au
"""


def main():
    numbers = [3, 1, 4, 1, 5, 9, 2]
    # numbers[0] == 3 # The first index
    # numbers[-1] == 2 # The last index
    # numbers[3] == 1 # Which is in the fourth index to the left
    # numbers[:-1] == [3, 1, 4, 1, 5, 9] # All but except the last
    # numbers[3:4] == [1]
    # (5 in numbers) == True
    # (7 in numbers) == False
    # ("3" in numbers) == False
    # numbers +  == [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

    print('1. Change the first element of numbers to "ten"')
    numbers[0] = 'ten'
    print(numbers, end='\n' * 2)

    print('2. Change the last element of numbers to 1')
    numbers[-1] = 1
    print(numbers, end='\n' * 2)

    print('3. Print all the elements from numbers except the first two (slice)')
    print(numbers[2:], end='\n' * 2)

    print('4. Print whether 9 is an element of numbers')
    print(9 in numbers, end='\n' * 2)


main()
