THIS_YEAR = 2024


class Guitar():
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of the guitar"""
        return THIS_YEAR - self.year

    def is_vintage(self):
        """If the guitar is at least 50 years old, return true"""
        if self.get_age() >= 50:
            return True
        else:
            return False
