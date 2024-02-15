"""
CP1404/CP5632 - Practical
Student Name: Dawei Zhu - 14613428
Student Email: dawei.zhu@my.jcu.edu.au
Answer the following questions:
1. When will a ValueError occur?
    When any input got non-numeric contents, even literal "one two three..."

2. When will a ZeroDivisionError occur?
    When the denominator got a zero

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Add a block of code to get valid denominator
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # get valid denominator
    while not denominator:
        print("0 is not a valid denominator")
        denominator = int(input("Enter the denominator:"))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

