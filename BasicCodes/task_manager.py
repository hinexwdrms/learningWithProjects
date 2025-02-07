import json
from datetime import date
import os

FILE_PATH = "C:\\VScode\\gettingstarted\\python test files\\new_file.json"

#print the tasks in readable form!

def create_file():
    if os.path.exists(FILE_PATH):
        print(f"The file '{FILE_PATH}' already exists.")
    else:
        with open(FILE_PATH, "w") as file:
            json.dump({}, file)
        print(f"'{FILE_PATH}' created successfully!")

def add_task():
    try:
        with open(FILE_PATH, "r") as file:
            existing_tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_tasks = {}

    try:
        entries = int(input("Input the number of Tasks that you would like to add: "))

        for i in range(entries):
            task_status = "IN PROGRESS"
            task_description = input(f"Enter description for task {i+1}: ")
            due_date = input("Enter due date for the task (optional, press ENTER to SKIP): ")
            date_created = str(date.today())
            date_modified = date_created

            task_id = len(existing_tasks) + 1
            existing_tasks[str(task_id)] = {
                "description": task_description,
                "due date": due_date if due_date else None,
                "date created": date_created,
                "date modified": date_modified,
                "task status": task_status
            }

        with open(FILE_PATH, "w") as file:
            json.dump(existing_tasks, file, indent=4)
        print("-----Successfully added tasks!-----")

    except ValueError:
        print("ONLY INTEGERS ALLOWED.")

def edit_task():
    print("----------Current Tasks----------")
    try:
        with open(FILE_PATH, "r") as file:
            tasks = json.load(file)
            if not tasks:
                print("No tasks available.")
                return
            print(json.dumps(tasks, indent=4))
    except (FileNotFoundError, json.JSONDecodeError):
        print("No tasks to display.")
        return

    to_edit = input("Enter the task_id of the task that you would like to edit: ")

    if to_edit in tasks:
        print(f"Task details: {tasks[to_edit]}")
        print("Which attribute would you like to edit?")
        print("1. Task status")
        print("2. Task description")
        print("3. Due date")

        edit_choice = input("Enter your choice (1/2/3): ")

        if edit_choice == "1":
            tasks[to_edit]["task status"] = input("Enter the new task status: ")
        elif edit_choice == "2":
            tasks[to_edit]["description"] = input("Enter the new task description: ")
        elif edit_choice == "3":
            tasks[to_edit]["due date"] = input("Enter the new due date (or leave blank to clear): ")
            tasks[to_edit]["due date"] = tasks[to_edit]["due date"] if tasks[to_edit]["due date"] else None
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            return
        
        tasks[to_edit]["date modified"] = str(date.today())

        with open(FILE_PATH, "w") as file:
            json.dump(tasks, file, indent=4)
        print("Changes saved successfully!")
    else:
        print(f"Task ID '{to_edit}' not found. Please try again.")

def delete_task():
    try:
        with open(FILE_PATH, "r") as file:
            existing_tasks = json.load(file)
            if not existing_tasks:
                print("No tasks found in the file!")
                return
            print("----------Current Tasks----------")
            print(json.dumps(existing_tasks, indent=4))
    except (FileNotFoundError, json.JSONDecodeError):
        print("No tasks to display.")
        return

    key_to_remove = input("Enter the task_id of the task you wish to remove: ")

    if key_to_remove.isdigit() and key_to_remove in existing_tasks:
        confirm = input(f"Are you sure you want to delete task ID '{key_to_remove}'? (yes/no): ").lower()
        if confirm == "yes":
            del existing_tasks[key_to_remove]
            reassigned_tasks = {str(i+1): task for i, task in enumerate(existing_tasks.values())}
            with open(FILE_PATH, "w") as file:
                json.dump(reassigned_tasks, file, indent=4)
            print(f"Task ID '{key_to_remove}' removed successfully.")
        else:
            print("Deletion canceled.")
    else:
        print("Please enter a valid numeric task ID.")

def view(): #add the feature to view the tasks on the basis of task status!
    try:
        with open(FILE_PATH, "r") as file:
            tasks = json.load(file)
            if not tasks:
                print("No tasks available.")
                return
            print("----------Current Tasks----------")
            print(json.dumps(tasks, indent=4))
    except (FileNotFoundError, json.JSONDecodeError):
        print("No tasks to display.")

print("______Welcome to the TASK MANAGER!______")
player_agreement = True

while player_agreement:
    print(
        "What would you like to do?"
        "\n1. Write a new task"
        "\n2. Delete a task"
        "\n3. Edit an existing task"
        "\n4. View all tasks"
        "\n5. Create new file"
    )
    user_action = input("--->(Press X to exit): ")

    if user_action == "1":
        add_task()
    elif user_action == "2":
        delete_task()
    elif user_action == "3":
        edit_task()
    elif user_action == "4":
        view()
    elif user_action == "5":
        create_file()
    elif user_action.lower() == "x":
        print("Thank you for using Task Manager! Goodbye!")
        player_agreement = False
    else:
        print("Please select a valid option (1/2/3/4/5) or 'X' to exit.")
        