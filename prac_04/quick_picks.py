"""
Prac 04 - Quick Picks
Student Name: Dawei Zhu - 14613428
Student Email: dawei.zhu@my.jcu.edu.au
"""
import random
from random import sample

ROW_CAPACITY = 6
CELL_VALUE_MIN = 1
CELL_VALUE_MAX = 45


def main():
    picks = int(input('How many quick picks? '))
    for i in range(picks):
        row = get_random_sample_list(CELL_VALUE_MIN, CELL_VALUE_MAX, ROW_CAPACITY)
        for j in row:
            print(f'{j:2} ', end='')
        print()


def get_random_sample_list(min_value, max_value, quantity):
    """
    Generate a random list without repeat
    Then sorting the list in ascending order
    """
    row = sample(
        range(min_value, max_value + 1),
        quantity
    )
    row.sort()
    return row


main()
