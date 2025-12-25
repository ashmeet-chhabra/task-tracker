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
    pass

def update_task(task_id, description):
    pass

def delete_task(task_id):
    pass

def mark_task(task_id, status):
    pass

def list_tasks(filter_status=None):
    pass

def main():
    load_tasks()
    exit()

    # ensures proper input
    if len(sys.argv) < 2:
        print("Usage: python <command> [arguments]")

    command = sys.argv[1]

    if(command == 'add'):
        description = sys.argv[2]

if __name__ == '__main__':
    main()