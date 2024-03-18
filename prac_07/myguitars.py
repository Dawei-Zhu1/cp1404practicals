from guitar import Guitar

FILENAME = 'guitars.csv'
TAB_SPACES_NUMBER = 4


def main():
    print(f'GUITAR MANAGER')
    print(f'Loading {FILENAME}...')
    guitars = get_guitars(FILENAME)
    guitars.sort()
    display_guitars(guitars)


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
