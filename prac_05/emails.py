"""
CP1404: Email Handling
By Dawei Zhu
"""


def main():
    email = input('Email: ')
    names_by_email = {}
    while email != '':
        name = get_full_name_from_email(email)
        confirmation = input(f'Is your name {name}? (Y/n) ').lower()
        if confirmation != 'y':
            name = input('Name: ')
        names_by_email[email] = name
        # Loop restarts here
        email = input('Email: ')
    # Program ends
    print()
    for each_email in names_by_email:
        print(f'{names_by_email[each_email]} ({each_email})')


def get_full_name_from_email(email):
    """Base on the email format, return the full name"""
    name = email.split('@')[0]
    # To split the name with a dot
    name = name.split('.')
    name = ' '.join(name)
    # Return the formatted name
    return name.title()


main()
