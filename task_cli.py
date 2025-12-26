import os
import sys
import json
from datetime import datetime

FILE_NAME = 'tasks.json'

# utility
def load_tasks():

    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, 'r') as file:
        try:
            return(json.load(file))
        except json.JSONDecodeError:
            return []
        
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def get_timestamp():
    return datetime.now().strftime('%Y-%m-%d: %H:%M:%S')

# core features
def add_task(description):
    tasks = load_tasks()
    task = {
        'id': get_next_id(tasks),
        'description': description,
        'status': 'todo',
        'createdAt': (temp_time := get_timestamp()),
        'updatedAt': temp_time
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task['id']})")

def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = get_timestamp()
            save_tasks(tasks)
            print("Task updated successfully")
            return
        print('Error: Task not found')

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task['id'] != task_id]

    if len(tasks) == len(new_tasks):
        print("Error: Task not found")
        return
    
    save_tasks(new_tasks)
    print("Task deleted successfully")

def mark_task(task_id, status):
    pass

def list_tasks(filter_status=None):
    tasks = load_tasks()
    filtered_tasks = tasks if not filter_status else [
        task for task in tasks if task['status'] == filter_status
    ]

    if not filtered_tasks:
        print("No tasks found")
        return

    for task in tasks:
        print(f"[{task['id']}] {task['description']} ({task['status']})")


def main():
    # ensures proper input
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        return

    command = sys.argv[1]

    if(command == 'add'):
        description = sys.argv[2]

if __name__ == '__main__':
    main()