tasks = []

def show_menu():
    print("\nTo-Do List")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Quit")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")

def remove_task():
    view_tasks()
    try:
        number = int(input("Enter task number to remove: "))
        if 1 <= number <= len(tasks):
            tasks.pop(number - 1)
            print("Task removed.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Bye!")
        break
    else:
        print("Invalid choice.")
