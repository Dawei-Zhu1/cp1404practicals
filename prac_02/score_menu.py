"""
Student Name: Dawei Zhu - 14613428
Student Email: <EMAIL>
"""
MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""


def main():
    # Request user to enter a score first
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").strip().upper()
    # Menu starts
    while choice != "Q":
        if choice == "G":
            # Get a new valid score
            score = get_valid_score()
        elif choice == "P":
            # Print result
            print(determine_the_result(score))
        elif choice == "S":
            print(int(score) * "*")
        else:
            print("Invalid choice")
        # Loop restarts
        print(MENU)
        choice = input(">>> ").strip().upper()
    # Loop ends
    print("See you!")


def get_valid_score():
    """Ask the user to enter a valid score"""
    user_score = float(input("Enter score: "))
    while user_score < 0 or user_score > 100:
        # Invalid if outside the range 0 ~ 100 inclusive.
        print("Invalid score, please enter a number between 0 and 100 (inclusive)")
        user_score = float(input("Enter score: "))
    return user_score


def determine_the_result(score):
    """
    Determine the result based on the score from 0 to 100
    :param score: float
    :return: string
    """
    if score < 0 or score > 100:
        # Invalid if outside the range 0 ~ 100 inclusive.
        return "Invalid score, please enter a number between 0 and 100 (inclusive)"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


# if __name__ == "__main__":
#     main()

main()
