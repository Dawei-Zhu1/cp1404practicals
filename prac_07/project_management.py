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
            pass
        if menu_choice == 'u':
            # Display projects with index:
            for index, project in enumerate(projects['Incomplete']):
                print(index, project)

            project_choice = get_valid_project_choice(len(projects['Incomplete']))
        print(MENU)
        menu_choice = input('>>> ').strip().lower()
    # Quit
    print('Thank you for using custom-built project management software.')


def get_valid_project_choice(valid_range):
    """To avoid unwanted choice, return valid project choice"""
    project_choice = get_valid_number('Project Choice: ')
    print(project_choice, range(valid_range))
    while project_choice not in range(valid_range):
        print('Invalid choice, out of range.')
        project_choice = get_valid_number('Project Choice: ')
    return project_choice


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


def get_valid_number(prompt, number_type='int'):
    """Return valid number"""
    number_type = number_type.strip().lower()
    is_valid = False
    number = None
    while not is_valid:
        try:
            # Type selection
            if number_type == 'float':
                number = float(input(prompt))
            elif number_type == 'int':
                number = int(input(prompt))

            if number < 0:
                print('Number must be greater than 0')
            else:
                is_valid = True
        except ValueError:
            print('Invalid! Must input a valid number')
    return number


if __name__ == '__main__':
    main()
