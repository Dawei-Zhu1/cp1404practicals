COLOUR_NAME_WITH_CODE = {
    'Absolute Zero': '#0048ba',
    'Aqua': '#00ffff',
    'Baby Blue': '#89cff0',
    'Black': '#000000',
    'Blond': '#faf0be',
    'Brown': '#a52a2a',
    'Cadet Grey': '#91a3b0',
    'Daffodil': '#ffff31',
    'Earth Yellow': '#e1a95f',
    'Falu Red': '#801818',
    'GO Green': '#00ab66',
    'Han Blue': '#446ccf',
    'Iceberg': '#71a6d2',
    'Jade': '#00a86b',
    'Kelly Green': '#4cbb17',
    'Languid Lavender': '#d6cadd',
    'Pink': '#ffc0cb',
    'White': '#ffffff'
}


def main():
    user_query = input('Search colours with name: ').strip().lower()
    # Separate all colour names
    display_colour_name = list(COLOUR_NAME_WITH_CODE.keys())
    # Separate all hex codes
    colour_codes = list(COLOUR_NAME_WITH_CODE.values())
    # make all names lower
    colour_keys_lower_case = [
        colour_name.lower()
        for colour_name in display_colour_name
    ]

    while user_query != '':
        if user_query in colour_keys_lower_case:
            colour_code_index = colour_keys_lower_case.index(user_query)
            colour_code = colour_codes[colour_code_index]
            print(f'{display_colour_name[colour_code_index]:>24}: {colour_code}')
        else:
            print('No colour found, either this colour is not recorded or you made a typo.')
        user_query = input('Search colours with name: ').strip().lower()
    # End
    print('Program terminated.')


main()
