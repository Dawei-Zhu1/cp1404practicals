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
    projects = []
    # Read data from project.txt
    print(MENU)
    choice = input('>>> ').strip().lower()
    while choice != 'q':
        if choice == 'l':
            projects = load_projects(FILENAME)
        if choice == 's':
            pass
        if choice == 'd':
            for i in projects:
                print(i)
        print(MENU)
        choice = input('>>> ').strip().lower()


def load_projects(filename):
    with open(filename, 'r') as f:
        project_list = []
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
            project_list.append(
                Project(project_name, start_date, priority, cost_estimate, completion_percentage)
            )
    return project_list


if __name__ == '__main__':
    main()
