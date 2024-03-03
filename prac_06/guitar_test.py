from guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1924, 16035.40)
    another_guitar = Guitar("My guitar", 2015, 200)
    guitar_50_year_old = Guitar("50 year old guitar", 2024 - 50, 3500)
    print(gibson)
    print('=' * 12)
    print(f'Gibson L-5 CES get_age() - Expected 100. Got {gibson.get_age()}')
    assert gibson.get_age() == 100
    print(f'Another Guitar get_age() - Expected 9. Got {another_guitar.get_age()}')
    assert another_guitar.get_age() == 9
    print(f'Gibson L-5 CES is_vintage() - Expected True. Got {gibson.is_vintage()}')
    assert gibson.is_vintage() is True
    print(f'Another Guitar is_vintage() - Expected False. Got {another_guitar.is_vintage()}')
    assert another_guitar.is_vintage() is False
    print(f'50-year old guitar is_vintage() - Expected True. Got {guitar_50_year_old.is_vintage()}')
    assert guitar_50_year_old.is_vintage() is True


main()
