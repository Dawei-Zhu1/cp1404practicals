MINIMUM_PASSWORD_LENGTH = 8


def main():
    password = get_valid_password()
    print(turn_password_to_asterisks(password))


def turn_password_to_asterisks(password):
    return len(password) * "*"


def get_valid_password():
    password = input("Enter your password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Password must be at least {} symbols.".format(MINIMUM_PASSWORD_LENGTH))
        password = input("Enter your password: ")
    return password


main()
