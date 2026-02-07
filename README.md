# Task Tracker CLI

A simple command-line task manager built with Python that allows users to create, update, delete, and track tasks directly from the terminal.

This project focuses on practicing file handling, JSON data storage, command-line interfaces, and structured program design.

## Project URL

[https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)


## Features

* Add new tasks
* Update existing tasks
* Delete tasks
* Mark tasks as **in-progress** or **done**
* List all tasks
* Filter tasks by status
* Automatic timestamp tracking (`createdAt`, `updatedAt`)
* Persistent storage using a local JSON file

---

## Requirements

* Python 3.x
* No external libraries required

---

## Installation

Clone the repository:

```
git clone https://github.com/ashmeet-chhabra/task-tracker
cd task-tracker
```

(Optional) Make the script executable on macOS/Linux:

```
chmod +x task_cli.py
```

---

## Usage

Run the script from the terminal:

```
python task_cli.py <command> [arguments]
```

---

## Commands

### Add a Task

```
python task_cli.py add "Buy groceries"
```

---

### Update a Task

```
python task_cli.py update 1 "Buy groceries and cook dinner"
```

---

### Delete a Task

```
python task_cli.py delete 1
```

---

### Mark Task Status

Mark as in progress:

```
python task_cli.py mark-in-progress 1
```

Mark as done:

```
python task_cli.py mark-done 1
```

---

### List Tasks

List all tasks:

```
python task_cli.py list
```

Filter by status:

```
python task_cli.py list done
python task_cli.py list in-progress
python task_cli.py list todo
```

---

## Data Storage

Tasks are stored locally in a `tasks.json` file created automatically in the project directory.

Example structure:

```
{
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2026-01-01 10:00:00",
    "updatedAt": "2026-01-01 10:00:00"
}
```

---

---

## License

This project is open-source and available under the MIT License.


