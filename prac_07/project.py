class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        return f'{self} - {self.name} - {self.start_date}'

    def __str__(self):
        """Returns a string representation of the project"""
        return f'{self.name} - {self.start_date}'
