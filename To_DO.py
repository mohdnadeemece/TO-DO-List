tasks=[]

def show_menu():
       print("\n--- To-Do List Menu ---")
       print("1. View Tasks")
       print("2. Add Task")
       print("3. Mark Task as Complete")
       print("4. Delete Task")
       print("5. Exit")

def view_task():
     if not tasks:
          print("Your To-Do list is empty.")
          return
     else: print(" your task:")

     for Index, task in enumerate(tasks,start=1):
          status="✅" if task['completed'] else "❌"
          print(f"{Index}.{task['title']} [{status}]") 

def add_task():
     title=input("Enter your task title: ")
     task={"title": title, "completed": False}
     tasks.append(task) 
     print(f"task {title} added.")  

def mark_complete():
     view_task()
     try:
      task_num=int(input("Enter your task mark as complete: ")) 
      if 1<= task_num<=len(tasks):
          tasks[task_num-1]['completed']=True
          print(f"your {task_num} marekd as completed.") 

      else:
          print("Inavlid task number.") 

     except ValueError:
         print("please Enter a valid number")

def delete_task():
    view_task()
    try:
        task_num=int(input("Enter task number to delete: "))

        if 1<=task_num <=len(tasks):
            removed=tasks.pop(task_num-1)
            print(f"Task {removed['title']} is deleted.")
        else:
            print("Invalid task number")  
    except ValueError:
        print("Enter valid input number.")       


while True:
    show_menu()

    choice=input("Enter your choice in between (1-5): ")

    if choice == '1':
       view_task()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_complete()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye! 👋")

        break
    else:
        print("Invalid choice. please enter from 1-5")

