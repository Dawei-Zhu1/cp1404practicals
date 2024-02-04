"""
CP1404/CP5632 - Week 1 Practical - Temperature
Student Name: Dawei Zhu - 14613428
Student Email: dawei.zhu@my.jcu.edu.au

Pseudocode for temperature conversion
show menu
get choice
while choice is not quit:
    if choose celsius_to_fahrenheit:
        get celsius
        farenheit = celsius * 9.0 / 5 + 32
        show farenheit
    elif choose fahrenheit_to_celsius:
        get fahrenheit
        celsius = 5 / 9 * (fahrenheit - 32)
        show celsius
    else:
        show invalid message
    print menu
    get choice
print thank you

"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
