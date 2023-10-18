import datetime

class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def __str__(self):
        return f"Description: {self.description}, Due Date: {self.due_date}, Priority: {self.priority}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date, priority):
        task = Task(description, due_date, priority)
        self.tasks.append(task)
        self.sort_tasks()

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")

    def set_due_date(self, task_index, due_date):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].due_date = due_date
            print("Due date set successfully.")
        else:
            print("Invalid task index.")

    def set_priority(self, task_index, priority):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].priority = priority
            print("Priority set successfully.")
        else:
            print("Invalid task index.")

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"Task {i}: {task}")

    def sort_tasks(self):
        self.tasks.sort(key=lambda task: (task.due_date, -task.priority))

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Set Due Date")
        print("4. Set Priority")
        print("5. List Tasks")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
            priority = int(input("Enter priority (1-5): "))
            todo_list.add_task(description, due_date, priority)
        elif choice == "2":
            task_index = int(input("Enter task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "3":
            task_index = int(input("Enter task index to set due date: "))
            due_date = input("Enter new due date (YYYY-MM-DD): ")
            due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
            todo_list.set_due_date(task_index, due_date)
        elif choice == "4":
            task_index = int(input("Enter task index to set priority: "))
            priority = int(input("Enter new priority (1-5): "))
            todo_list.set_priority(task_index, priority)
        elif choice == "5":
            todo_list.list_tasks()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
