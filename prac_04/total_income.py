"""
CP1404/CP5632 Practical - Total Income
Student Name: Dawei Zhu - 14613428
Student Email: dawei.zhu@my.jcu.edu.au
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes)


def print_income_report(incomes):
    """
    Display income report
    I remove the arg for number_of_month
    """
    print("\nIncome Report\n-------------")
    total = 0
    month_count = 0
    for income in incomes:
        total += income
        month_count += 1
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month_count, income, total))


main()
