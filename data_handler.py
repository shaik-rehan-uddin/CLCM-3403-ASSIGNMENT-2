import json


# Load tasks from the JSON file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks


# Save tasks to the JSON file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


# Function to add a new task
def add_task(name, description, priority, due_date):
    tasks = load_tasks()
    new_task = {
        "name": name,
        "description": description,
        "priority": priority,
        "due_date": due_date.strftime("%Y-%m-%d"),
    }
    tasks.append(new_task)
    save_tasks(tasks)


# Function to edit a task
def edit_task(index, name, description, priority, due_date):
    tasks = load_tasks()
    edited_task = {
        "name": name,
        "description": description,
        "priority": priority,
        "due_date": due_date.strftime("%Y-%m-%d"),
    }
    tasks[index] = edited_task
    save_tasks(tasks)


# Function to remove a task
def remove_task(index):
    tasks = load_tasks()
    del tasks[index]
    save_tasks(tasks)
