#mini-project
#Simple To-Do List (Add & View)
tasks = []
#an empty list
while True:
    action = input("Add a task or view tasks? (add/add 3 tasks/view/exit): ").lower()
    if action == "add":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif action == "add 3 tasks":
        task1=input("enter task1: ")
        task2=input("enter task2: ")
        task3=input("enter task3: ")
        tasks.append(task1)
        tasks.append(task2)
        tasks.append(task3)
    elif action == "view":
        print("Your tasks:", tasks)
    elif action == "exit":
        break
    else:
        print("Invalid input.")
