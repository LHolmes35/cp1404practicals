"""
Project management - Prac 07
Estimate time = 1hr 20mins
Actual time = 2hrs 35mins
"""

from prac_07.project import Project
import datetime


MENU = "- (L)oad Projects\n- (S)ave Projects\n- (D)isplay Projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate Project\n- (Q)uit Project"
FILENAME = "projects.txt"


def main():

    projects = load_projects(FILENAME)
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            filename = input("File to load from: ")
            load_projects(filename)
        elif menu_choice == "S":
            save_projects(projects, FILENAME)
        elif menu_choice == "D":
            display_projects(projects)
        elif menu_choice == "F":
            filter_projects(projects)
        elif menu_choice == "A":
            add_new_project(projects)
        elif menu_choice == "U":
            update_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        menu_choice = input(">>> ").upper()
    save_projects(projects, FILENAME)


def load_projects(filename):
    projects = []
    in_file = open(filename, "r", encoding="utf-8-sig")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split("	")
        parts[2] = int(parts[2])
        parts[3] = float(parts[3])
        parts[4] = int(parts[4])
        project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
        projects.append(project)
    in_file.close()
    return projects


def save_projects(projects, filename):
    with open(filename, "w", encoding="utf-8-sig") as out_file:
        for project in projects:
            print(f"{project.name}	{project.start_date}	{project.priority}	{project.cost_estimate}	{project.percentage_complete}", file=out_file)
    out_file.close()


def display_projects(projects):
    incomplete_projects = []
    complete_projects = []
    for project in projects:
        if not project.is_complete():
            incomplete_projects.append(project)
        else:
            complete_projects.append(project)
    print("Incomplete projects: ")
    incomplete_projects.sort()
    for project in incomplete_projects:
        print(" ", project)
    print("Completed projects: ")
    complete_projects.sort()
    for project in complete_projects:
        print(" ", project)


def filter_projects(projects):
    date_string = input("Show the projects that start after date (dd/mm/yyyy): ")
    date_choice = datetime.datetime.strptime(date_string, '%d/%m/%Y').date()
    for project in projects:
        if project.start_date > date_choice:
            print(project)


def add_new_project(projects):
    print("Let's add a new project")
    new_name = input("Name: ")
    new_start_date = input("Start date (dd/mm/yyyy): ")
    new_priority = int(input("Priority: "))
    new_cost_estimate = float(input("Cost: $"))
    new_percentage_complete = int(input("Percent complete: "))
    new_project = Project(new_name, new_start_date, new_priority, new_cost_estimate, new_percentage_complete)
    projects.append(new_project)


def update_project(projects):
    for project in projects:
        print(f"{project}")
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])
    new_percentage = int(input("New Percentage: "))
    projects[project_choice].percentage_complete = new_percentage
    try:
        new_priority = int(input("New Priority: "))
        projects[project_choice].priority = new_priority
    except ValueError:
        pass


main()
