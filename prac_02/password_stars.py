MINIMUM_PASSWORD_LENGTH = 8


def main():
    password = get_password()
    display_password_in_asterisks(password)


def display_password_in_asterisks(password):
    print(len(password) * "*")


def get_password():
    password = input("Enter your password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Password must be at least {} symbols.".format(MINIMUM_PASSWORD_LENGTH))
        password = input("Enter your password: ")
    return password


main()
