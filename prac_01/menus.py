"""
CP1404/CP5632 - Week 1 Practical - Menus
Student Name: Dawei Zhu - 14613428
Student Email: dawei.zhu@my.jcu.edu.au

Pseudocode:
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
MENU = """(H)ello
(G)oodbye
(Q)uit"""
# Get name
name = input("Enter name: ").title().strip()
# Display menu & get choice
print(MENU)
choice = input(">>> ").upper().strip()
# Loop while not quit
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    # Display menu & get choice within the loop
    print(MENU)
    choice = input(">>> ").upper().strip()
# Show this message when it is finished
print("Finished.")
