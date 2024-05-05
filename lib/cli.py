from helpers import (
    exit_program,
    list_projects,
    find_project_by_name,
    find_project_by_id,
    create_project,
    update_project,
    delete_project,
    list_project_tasks,
    list_tasks,
    find_task_by_name,
    find_task_by_id,
    create_task,
    edit_task,
    delete_task,
    clear,
    open_project,
    manage_projects
)
import typer


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "clear":
            clear()
        elif choice == "1":
            list_projects()
        elif choice == "2":
            selected_project = open_project()
            clear()
            project_loop(selected_project)
        elif choice == "3":
            manage_projects()
        # elif choice == "4":
        #     create_project()
        # elif choice == "5":
        #     update_project()
        # elif choice == "6":
        #     delete_project()
        # elif choice == "7":
        #     list_project_tasks()
        # elif choice == "8":
        #     list_tasks()
        # elif choice == "9":
        #     find_task_by_name()
        # elif choice == "10":
        #     find_task_by_id()
        # elif choice == "11":
        #     create_task()
        # elif choice == "12":
        #     update_task()
        # elif choice == "13":
        #     delete_task()
        else:
            print("Invalid choice")

def project_loop(project_id):
    list_project_tasks(project_id)
    while True:
        task_menu()
        choice = input("> ")
        if choice == "0":
            clear()
            main()
        elif choice == "clear":
            clear()
        elif choice == "1":
            create_task(project_id)
        elif choice == "2":
            edit_task(project_id)
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task(project_id)


        
def task_menu():
    print("Please select an option:")
    print("0. Back to main menu")
    print("1. Create task")
    print("2. Edit task")
    print("3. Complete task")
    print("4. Delete task")


def menu():
    print("Type 'clear' to clear the terminal")
    print("*" * 100)
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all projects")
    print("2. Open project")
    print("3. Manage projects")
    # print("4. Create project")
    # print("5. Update project")
    # print("6. Delete project")
    # print("7. List all tasks in a project")
    # print("8. List all tasks")
    # print("9. Find task by name")
    # print("10. Find task by id")
    # print("11. Create task")
    # print("12. Update task")
    # print("13. Delete task")


if __name__ == "__main__":
    main()
