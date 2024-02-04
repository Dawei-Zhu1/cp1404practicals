"""
CP1404/CP5632 - Week 1 Practical - Sales Bonus
Student Name: Dawei Zhu - 14613428
Student Email: dawei.zhu@my.jcu.edu.au

Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

Pseudocode:
get sales
while sales >= 0
    calculate bonus (this line is intentionally incomplete pseudocode)
    print bonus
    get sales
do next thing
"""
BASIC_BONUS_RATE = 0.1
HIGH_BONUS_RATE = 0.15

sales = float(input("Enter sales: $"))
# Loop when sales are not negative
while sales >= 0:
    if sales < 1000:
        bonus = sales * BASIC_BONUS_RATE
    else:
        bonus = sales * HIGH_BONUS_RATE
    print(f"The bonus is ${bonus:.2f}")
    sales = float(input("Enter sales: $"))
