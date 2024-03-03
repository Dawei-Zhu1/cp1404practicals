class ProgrammingLanguage:
    def __init__(self, name, language_type, reflection, year):
        self.name = name
        self.language_type = language_type
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.language_type == 'Dynamic'

    def __str__(self):
        return f'{self.name}, {self.language_type} Typing, Reflection={self.reflection}, First appeared in {self.year}'
