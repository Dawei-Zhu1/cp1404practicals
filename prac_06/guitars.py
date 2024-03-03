from guitar import Guitar


def main():
    guitars = []
    print('My guitars!')

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    guitar_name = input('Name: ')
    while guitar_name != '':
        year = int(input('Year: '))
        cost = float(input('Cost: '))
        guitars.append(
            Guitar(name=guitar_name, year=year, cost=cost)
        )
        guitar_name = input('Name: ')

    conclude_guitars(guitars)


def conclude_guitars(guitars):
    """
    Get the guitar list, and display the name, year and price of each guitar
    """
    for i in enumerate(guitars):
        guitar_count, guitar = i[0] + 1, i[1]
        name_max_length = get_longest_length(
            [guitar.name for guitar in guitars]
        )
        vintage_status = '(vintage)' if guitar.is_vintage() else ''
        print(f'Guitar {guitar_count}: {guitar.name:>{name_max_length}}, worth ${guitar.cost:10,.2f} {vintage_status}')


def get_longest_length(items):
    """Get the length of the longest word"""
    length = 0
    for i in items:
        if len(i) > length:
            length = len(i)
    return length


main()
