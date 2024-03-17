"""
CP1404: Wimbledon
By Dawei Zhu
"""


def main():
    records_by_champion = {}
    countries_won = []
    with open('wimbledon.csv', 'r', encoding='utf-8-sig') as infile:
        # Skip title line
        infile.readline()
        for line in infile:
            data = line.strip().split(',')
            country_of_team, champion = data[1], data[2]
            if not records_by_champion.get(champion):
                records_by_champion[champion] = 0
            records_by_champion[champion] += 1
            countries_won.append(country_of_team)

    unique_country_won = get_list_with_unique_elements(countries_won)
    print('Wimbledon Champions: ')
    for each_champion in records_by_champion:
        print(f'{each_champion}: {records_by_champion[each_champion]}')
    print()
    print(f'These {len(unique_country_won)} countries have won Wimbledon: ')
    print(f'{", ".join(unique_country_won)}')


def get_list_with_unique_elements(words):
    """Make the elements in the list unique"""
    words = list(set(words))
    words.sort()
    return words


main()
