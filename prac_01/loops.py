"""
CP1404/CP5632 - Week 1 Practical - Loops
Student Name: Dawei Zhu - 14613428
Student Email: dawei.zhu@my.jcu.edu.au
"""
print("Example: displays all the odd numbers between 1 and 20 with a space between each")
for i in range(1, 21, 2):
    print(i, end=' ')
print("\n")

print("a. count in 10s from 0 to 100")
for i in range(0, 101, 10):
    print(i, end=' ')
print("\n")

print("b. count down from 20 to 1")
for i in range(20, 0, -1):
    print(i, end=' ')
print("\n")

print("c. print n stars")
numbers_of_stars = int(input("Number of stars: "))
for i in range(0, numbers_of_stars):
    print('*', end='')
print("\n")

print("d. print n lines of increasing star:")
numbers_of_lines = int(input("Number of stars: "))
for i in range(numbers_of_lines):
    for j in range(i + 1):
        print('*', end='')
    if i < numbers_of_lines - 1:
        # If it is not the last line, no return
        print()



