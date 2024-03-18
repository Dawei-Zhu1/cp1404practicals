from guitar import Guitar

FILENAME = 'guitars.csv'
TAB_SPACES_NUMBER = 4
MENU = """
MENU
(D)isplay my guitars
(A)dd a guitar
(Q)uit
"""


def main():
    print(f'GUITAR MANAGER')
    print(f'Loading {FILENAME}...')
    guitars = get_guitars(FILENAME)
    guitars.sort()
    display_guitars(guitars)
    print(MENU)
    choice = input('>>> ').strip().lower()
    while choice != 'q':
        if choice == 'd':
            display_guitars(guitars)
            print()
        elif choice == 'a':
            new_guitar = get_new_guitar()
            guitars.append(new_guitar)
            print(f'{new_guitar} has been added to my guitar list.')
        else:
            print('Invalid option')
        choice = input('>>> ').strip().lower()

    is_user_want_to_save = input(f'Do you want to save guitar info to {FILENAME}? (Y/n)').strip().lower()
    if is_user_want_to_save == 'y':
        print(f'Saving guitars to {FILENAME}...')
        with open(FILENAME, 'w') as f:
            for guitar in guitars:
                output = ','.join([guitar.name, str(guitar.year), str(guitar.cost)])
                f.write(output + '\n')
        print('Done')
    else:
        print('Guitars are not saved')

    print('Have a nice day!')


def get_guitars(filename):
    """
    Get guitars from csv file
    :param filename:
    :return: list of guitars
    """
    with open(filename, 'r') as f:
        guitar_list = []
        for line in f:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(name, year, cost)
            guitar_list.append(guitar)
    return guitar_list


def get_new_guitar():
    guitar_name = get_valid_text()
    year_bought = get_valid_number('Year: ')
    cost = get_valid_number('Cost: ', 'float')
    return Guitar(guitar_name, year_bought, cost)


def get_valid_text():
    """Return valid guitar name"""
    guitar_name = input('Guitar name: ').strip()
    while not len(guitar_name):
        print('Guitar name cannot be empty!')
        guitar_name = input('Guitar name: ').strip()
    return guitar_name


def get_valid_number(prompt, number_type='int'):
    """Return valid float number"""
    number_type = number_type.strip().lower()
    is_valid = False
    number = None
    while not is_valid:
        try:
            # Type selection
            if number_type == 'float':
                number = float(input(prompt))
            elif number_type == 'int':
                number = int(input(prompt))

            if number < 0:
                print('Number must be greater than 0')
            else:
                is_valid = True
        except ValueError:
            print('Invalid! Must input a valid number')
    return number


def display_guitars(guitar_list):
    """Show all guitars"""
    # Layout
    name_width = longest_name(guitar_list) + TAB_SPACES_NUMBER
    year_width = 4 + TAB_SPACES_NUMBER
    cost_width = 12
    # Add 1 is for $ sign
    full_width = name_width + year_width + cost_width + 1
    # Statistics
    guitar_number = len(guitar_list)
    # Output
    print('=' * full_width)
    print(f'{"Name":{name_width}} {"Year":<{year_width}} {"Cost":^{cost_width}}')
    print('-' * full_width)
    for guitar in guitar_list:
        print(f'{guitar.name:{name_width}} {guitar.year:<{year_width}} ${guitar.cost:10,.2f}')
    print('=' * full_width)
    print(f'You have {guitar_number} guitars' if guitar_number > 1
          else f'You have {guitar_number} guitar')


def longest_name(guitar_list):
    return max([len(guitar.name) for guitar in guitar_list])


if __name__ == '__main__':
    main()
