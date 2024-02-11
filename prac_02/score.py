"""
CP1404/CP5632 - Week 2 Practical - Score
Student Name: Dawei Zhu - 14613428
Student Email: dawei.zhu@my.jcu.edu.au
"""
import random


def main():
    score = float(input("Enter score: "))
    result = determine_the_result(score)
    print(result)
    # Extra test
    print("=== Random score test ===")
    random_score = random.randint(1, 100)
    print("Score:", random_score, "result:", determine_the_result(random_score))


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


# If I want export the functions, I must add this part, rather than merely main()

# if __name__ == "__main__":
#     main()

# If I simply call main() like below, It till run the entire program
main()
