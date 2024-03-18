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
    choice = input('>>> ').strip().lower()
    while choice != 'q':
        if choice == 'l':
            pass
        if choice == 's':
            pass
        if choice == 'd':
            for category in projects:
                print(f'{category}:')
                for project in projects[category]:
                    print(f'  {project}')

        if choice == 'f':
            pass
        if choice == 'a':
            pass
        if choice == 'u':
            pass
        print(MENU)
        choice = input('>>> ').strip().lower()
    # Quit
    print('Thank you for using custom-built project management software.')


def load_projects(filename):
    with open(filename, 'r') as f:
        categorized_projects = {'Incomplete':[], 'Completed':[]}
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
