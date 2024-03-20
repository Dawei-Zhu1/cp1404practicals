import datetime
from project import Project

FILENAME = 'projects.txt'
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    # Initials
    # Read data from project.txt
    projects = load_projects(FILENAME)
    print(MENU)
    menu_choice = input('>>> ').strip().lower()
    while menu_choice != 'q':
        if menu_choice == 'l':
            filename = get_valid_text('Enter a filename to read the projects: ')
            projects = load_projects(filename)
        if menu_choice == 's':
            filename_for_saving = get_valid_text('Enter a filename to save the projects: ')
            save_projects(projects, filename_for_saving)
            print(f'Project saved as {filename_for_saving} successfully!')
        if menu_choice == 'd':
            categorized_projects = categorize_projects(projects)
            print('Incomplete projects: ')
            for i in categorized_projects[0]:
                print(f'  {i}')
            print('Completed projects: ')
            for i in categorized_projects[1]:
                print(f'  {i}')

        if menu_choice == 'f':
            pass
        if menu_choice == 'a':
            print("Let's add a new project")
            project_name = get_valid_text('Name: ')
            project_start_date = get_valid_date('Start date (dd/mm/yyyy): ')
            project_priority = get_valid_priority('Priority: ')
            project_cost_estimate = get_valid_number('Cost estimate: ', )
            project_percentage = get_valid_percentage('Completion percentage: ')
            new_project = Project(
                project_name,
                project_start_date,
                project_priority,
                project_cost_estimate,
                project_percentage
            )
            projects.append(new_project)

        if menu_choice == 'u':
            # Display projects with index:
            for index, project in enumerate(projects):
                print(index, project)
            project_choice = get_ranged_number(
                0,
                len(projects) - 1,
                'Project Choice: '
            )
            chosen_project = projects[project_choice]
            print(chosen_project)
            # Ask for new inputs
            new_percentage = get_valid_percentage('New Percentage: ', allow_empty=True)
            new_priority = get_valid_priority('New Priority: ', allow_empty=True)
            # Apply changes when inputs are detected
            chosen_project.update_completion_percentage(new_percentage)
            chosen_project.update_completion_priority(new_priority)

        print(MENU)
        menu_choice = input('>>> ').strip().lower()
    # Quit
    print('Thank you for using custom-built project management software.')


def categorize_projects(projects):
    """
    Return a list contains 2 lists
    0. InCompleted
    1. Completed
    """
    completed_projects = []
    incomplete_projects = []
    for i in projects:
        if i.is_completed():
            completed_projects.append(i)
        else:
            incomplete_projects.append(i)
    return [incomplete_projects, completed_projects]


def format_date(date_string):
    """
    Format the string to date
    :param date_string: string with format dd/mm/yyyy
    :return: a Date instant or None if is invalid
    """
    date_parts = date_string.split('/')
    if len(date_parts) == 3:
        day, month, year = [int(date_particle) for date_particle in date_parts]
        date = datetime.date(year, month, day)
    else:
        print('Bad date format. Use / for separation.')
        return None
    return date


def get_valid_date(prompt):
    """Return valid date format."""
    date = None
    is_valid = False
    while not is_valid:
        try:
            date = get_valid_text(prompt)
            date = format_date(date)
            if date:
                is_valid = True
        except ValueError:
            print('Invalid date. Try again.')
    return date


def get_valid_text(prompt):
    """Return text in proper format."""
    text = input(prompt).strip()
    while text == '':
        print('Input cannot be empty')
        text = input(prompt).strip()
    return text


def get_valid_number(prompt, number_type='int', allow_empty=False):
    """Return valid number"""
    number_type = number_type.strip().lower()
    is_valid = False
    number = None
    while not is_valid:
        number = input(prompt).strip()
        if allow_empty and not len(number):
            return None
        try:
            # Type selection
            if number_type == 'float':
                number = float(number)
            elif number_type == 'int':
                number = int(number)

            is_valid = True
        except ValueError:
            print('Invalid! Must input a valid number')
    return number


def get_ranged_number(start, end, prompt, number_type='int', allow_empty=False):
    """
    Inherit from get_number, add the range feature
    :param start: start of range
    :param end: end of range
    :param prompt: str
    :param number_type: 'int', 'float'
    :param allow_empty: bool
    :return: number
    """
    is_valid = False
    number = None
    while not is_valid:
        number = get_valid_number(prompt, number_type, allow_empty=allow_empty)
        # Case Allowing empty, confirmed by parent function
        if number is None:
            return number
        # Case Not allowing empty
        if number < start:
            print(f'Number must be >= than {start}')
        elif number > end:
            print(f'Number must be <= {end}')
        else:
            is_valid = True
    return number


def get_valid_percentage(prompt, allow_empty=False):
    """Get number in percent format."""
    return get_ranged_number(0, 100, prompt, 'int', allow_empty)


def get_valid_priority(prompt, allow_empty=False):
    """Return number in priority format."""
    return get_ranged_number(1, 10, prompt, 'int', allow_empty)


def load_projects(filename):
    """Read the original file and return python objects in list"""
    with open(filename, 'r') as f:
        projects = []
        # Skip the titles
        f.readline()
        # Process contents
        for line in f:
            parts = line.split('\t')
            project_name = parts[0].strip()
            start_date = format_date(parts[1].strip())
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(project_name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


def save_projects(data, filename):
    """Write project to file"""
    with open(filename, 'w') as f:
        f.write('\t'.join(
            [
                'Name',
                'Start Date',
                'Priority',
                'Cost Estimate',
                'Completion Percentage'
            ]
        ) + '\n')
        for project in data:
            output = '\t'.join([
                project.name,
                project.start_date,
                str(project.priority),
                str(project.cost_estimate),
                str(project.completion_percentage)
            ])
            f.write(output + '\n')


if __name__ == '__main__':
    main()
