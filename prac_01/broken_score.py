"""
CP1404/CP5632 - Week 1 Practical
Broken program to determine score status
Student Name: Dawei Zhu - 14613428
Student Email: dawei.zhu@my.jcu.edu.au
"""
score = float(input("Enter score: "))
if score < 0 or score > 100:
    # Invalid if outside the range 0 ~ 100 inclusive.
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")