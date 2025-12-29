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
            return json.load(file)
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
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = get_timestamp()
            save_tasks(tasks)
            print(f"Task marked as {status}")
            return
    print('Error: Task not found')

def list_tasks(filter_status=None):
    tasks = load_tasks()
    filtered_tasks = tasks if not filter_status else [
        task for task in tasks if task['status'] == filter_status
    ]

    if not filtered_tasks:
        print("No tasks found")
        return

    for task in filtered_tasks:
        print(f"[{task['id']}] {task['description']} ({task['status']})")


def main():
    # ensures proper input
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        return

    command = sys.argv[1]

    try:
        if(command == 'add'):
            description = sys.argv[2]
            add_task(description)

        elif(command == 'update'):
            id = int(sys.argv[2])
            description = sys.argv[3]
            update_task(id, description)

        elif(command == 'delete'):
            id = int(sys.argv[2])
            delete_task(id)

        elif(command == 'mark-in-progress'):
            id = int(sys.argv[2])
            mark_task(id, 'in-progress')
        
        elif(command == 'mark-done'):
            id = int(sys.argv[2])
            mark_task(id, 'done')

        elif(command == 'list'):
            filter_status = None if len(sys.argv) < 3 else sys.argv[2]
            list_tasks(filter_status)

        else:
            print('Unknown command')

    except IndexError:
        print("Error: Missing arguments")
    except ValueError:
        print("Error: Invalid task ID")

if __name__ == '__main__':
    main()