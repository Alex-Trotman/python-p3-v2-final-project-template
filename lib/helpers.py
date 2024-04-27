# lib/helpers.py

from models.project import Project
from models.task import Task

def exit_program():
    print("Goodbye!")
    exit()

def list_projects():
    projects = Project.get_all()
    for project in projects:
        print(project)


def find_project_by_name():
    name = input("Enter the project's name: ")
    project = Project.find_by_name(name)
    print(project) if project else print(
        f'Project {name} not found')


def find_project_by_id():
    id_ = input("Enter the project's id: ")
    project = Project.find_by_id(id_)
    print(project) if project else print(f'Project {id_} not found')


def create_project():
    name = input("Enter the project's name: ")
    description = input("Enter the project's description: ")
    try:
        project = Project.create(name, description)
        print(f'Success: {project}')
    except Exception as exc:
        print("Error creating project: ", exc)


def update_project():
    id_ = input("Enter the project's id: ")
    if project := Project.find_by_id(id_):
        try:
            name = input("Enter the project's new name: ")
            project.name = name
            description = input("Enter the project's new description: ")
            project.description = description

            project.update()
            print(f'Success: {project}')
        except Exception as exc:
            print("Error updating project: ", exc)
    else:
        print(f'Project {id_} not found')


def delete_project():
    id_ = input("Enter the project's id: ")
    if project := Project.find_by_id(id_):
        project.delete()
        print(f'Project {id_} deleted')
    else:
        print(f'Project {id_} not found')


def list_project_tasks():
    project_id = input("Enter the project's id: ")
    project = Project.find_by_id(project_id)
    
    if project:
        print(f"Listing tasks for Project {project_id}: {project.name}")
        tasks = project.tasks()
        if tasks:
            for task in tasks:
                print(task)
        else:
            print("No tasks found in this project.")
    else:
        print(f"Project with ID {project_id} not found")
