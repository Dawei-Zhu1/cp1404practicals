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
            pass
        if menu_choice == 's':
            pass
        if menu_choice == 'd':
            for category in projects:
                print(f'{category}:')
                for project in projects[category]:
                    print(f'  {project}')

        if menu_choice == 'f':
            pass
        if menu_choice == 'a':
            print("Let's add a new project")
            project_name = get_valid_text('Name: ')
            project_start_date = get_valid_text('Start date (dd/mm/yy): ')
            project_priority = get_valid_priority('Priority: ')
            project_cost_estimate = get_valid_text('Cost estimate: ')
            project_percentage = get_valid_percentage('Completion percentage: ')

            print()
        if menu_choice == 'u':
            # Display projects with index:
            incomplete_project = projects['Incomplete']
            for index, project in enumerate(incomplete_project):
                print(index, project)
            project_choice = get_valid_number(
                0,
                len(projects['Incomplete']) - 1,
                'Project Choice: '
            )
            chosen_project = incomplete_project[project_choice]
            print(chosen_project)
            # Ask for new inputs
            new_percentage = get_valid_percentage('New Percentage: ')
            new_priority = get_valid_priority('New Priority: ')
            # Apply changes when inputs are detected
            if new_priority:
                chosen_project.priority = new_priority
            if new_percentage:
                chosen_project.completion_percentage = new_percentage

        print(MENU)
        menu_choice = input('>>> ').strip().lower()
    # Quit
    print('Thank you for using custom-built project management software.')


def get_valid_percentage(prompt):
    return get_valid_number(0, 100, prompt, 'int', True)


def get_valid_priority(prompt):
    return get_valid_number(0, 10, prompt, 'int', True)


def get_valid_text(prompt):
    text = input(prompt).strip()
    while text == '':
        print('Input cannot be empty')
        text = input(prompt).strip()
    return text


def get_valid_number(start, end, prompt, number_type='int', allow_empty=False):
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

            if number < start:
                print(f'Number must be >= than {start}')
            elif number > end:
                print(f'Number must be <= {end}')
            else:
                is_valid = True
        except ValueError:
            print('Invalid! Must input a valid number')
    return number


def load_projects(filename):
    with open(filename, 'r') as f:
        categorized_projects = {'Incomplete': [], 'Completed': []}
        # Skip the titles
        f.readline()
        # Process contents
        for line in f:
            parts = line.split('\t')
            project_name = parts[0].strip()
            start_date = parts[1].strip()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(project_name, start_date, priority, cost_estimate, completion_percentage)
            if completion_percentage == 100:
                categorized_projects['Completed'].append(project)
            else:
                categorized_projects['Incomplete'].append(project)
    return categorized_projects


if __name__ == '__main__':
    main()
