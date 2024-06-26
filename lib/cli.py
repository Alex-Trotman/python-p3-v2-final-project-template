# Importing various helper functions used for task and project management
from helpers import (
    exit_program,
    list_projects,
    list_project_tasks,
    create_task,
    edit_task,
    complete_task,
    delete_task,
    clear,
    open_project,
    create_project,
    edit_project,
    delete_project
)

# Display the main menu for the overall program
def menu():
    print("*" * 100)
    print("Get organized and stay productive with TaskMaster. Manage your tasks and projects effortlessly.")
    print("Type 'clear' to clear the terminal")
    print("*" * 100)
    print("Enter the number corresponding to your desired action, or type 'exit' to quit at any time.")
    print("0. Exit the program")
    print("1. List all projects")
    print("2. Open project")
    print("3. Manage projects")

# Display the menu for managing tasks within a project
def task_menu():
    print("Please select an option:")
    print("0. Back to main menu")
    print("1. Create task")
    print("2. Edit task")
    print("3. Complete task")
    print("4. Delete task")

# Display the menu for managing projects
def manage_projects_menu():
    print("Please select an option:")
    print("0. Back to main menu")
    print("1. Create project")
    print("2. Edit project")
    print("3. Delete project")

# Entry point of the CLI application
def main():
    while True:
        menu()
        choice = input("> ")

        # Handle the user's selection
        if choice == "0":
            exit_program()
        elif choice == "clear":
            clear()
        elif choice == "exit":
            exit_program()
        elif choice == "1":
            list_projects()
        elif choice == "2":
            project = open_project()
            clear()
            project_loop(project)
        elif choice == "3":
            manage_projects()
        else:
            print("Invalid choice")

# Manage tasks within a specific project
def project_loop(project):
    list_project_tasks(project)
    while True:
        task_menu()
        choice = input("> ")

        if choice == "0":
            clear()
            main()
        elif choice == "clear":
            clear()
        elif choice == "exit":
            clear()
            main()
        elif choice == "1":
            create_task(project)
        elif choice == "2":
            edit_task(project)
        elif choice == "3":
            complete_task(project)
        elif choice == "4":
            delete_task(project)

# Manage project operations (create, edit, delete)
def manage_projects():
    list_projects()
    while True:
        manage_projects_menu()
        choice = input("> ")

        if choice == "0":
            clear()
            main()
        elif choice == "clear":
            clear()
        elif choice == "exit":
            clear()
            main()
        elif choice == "1":
            create_project()
        elif choice == "2":
            edit_project()
        elif choice == "3":
            delete_project()

# Run the program if executed directly
if __name__ == "__main__":
    main()
