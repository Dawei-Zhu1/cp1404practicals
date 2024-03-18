from guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    guitars = get_guitars(FILENAME)
    guitars.sort()
    print(guitars)


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


if __name__ == '__main__':
    main()
