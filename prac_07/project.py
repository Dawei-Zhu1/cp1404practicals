import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def date_to_string(self):
        return self.start_date.strftime('%d/%m/%Y')

    def is_completed(self):
        """Check whether the percentage is 100"""
        return self.completion_percentage == 100

    def update_completion_percentage(self, new_percentage):
        """Update completion percentage when having input"""
        if new_percentage is not None:
            self.completion_percentage = new_percentage

    def update_priority(self, new_priority):
        """Update priority when having input"""
        if new_priority is not None:
            self.completion_percentage = new_priority

    def __repr__(self):
        """Simple representation of the project"""
        return f'{self} - {self.name} - {self.start_date}'

    def __str__(self):
        """Returns a string representation of the project"""
        return (f'{self.name}, start: {self.date_to_string()}, priority {self.priority}, \
estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%')
