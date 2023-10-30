todo=[]             #list for todo
def add_task():                 # adding task to list
    task=input("enter your task: ")
    todo.append(task)
    print("Task is added to list")
def view_task():        #tasks in the list
    if not todo:
        print("There is no task in to-do list")
    else:
        print("TO-DO LIST: ")
        for index,task in enumerate(todo, start=1):
            print(f"{index}. {task}")
def delete_task():          #deleting a task
    view_task()
    t_index=int(input("Enter the index of the task to delete"))
    if 0<=t_index<len(todo):
        deleted_task=todo.pop(t_index)
        print(f"{deleted_task} has been deleted")
    else:
        print("Invalid index of task.")
def update_task():      #updating a task
    view_task()
    t_index=int(input("Enter the index of the task to update(index starts from 0): "))
    if 0<=t_index<len(todo):
        new_task=input("Enter the task to update: ")
        todo[t_index]=new_task
        print("Task updated Successfully.")
    else:
        print("Invalid index")
while True:
    print("\nTO-DO LIST OPTIONS")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. Exit")
    choice=input("Select an option from above(1/2/3/4/5): ")
    if choice=="1":
        add_task()
    elif choice=="2":
        view_task()
    elif choice=="3":
        delete_task()
    elif choice=="4":
        update_task()
    elif choice=="5":
        break
    else:
        print("Invalid option")