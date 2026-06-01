# 📝 To-Do List App (Python)

A simple command-line To-Do List application built with Python.

This project demonstrates the use of:

* Lists
* Functions
* File Handling
* User Input
* Basic Data Persistence

Tasks are automatically stored in a text file so they remain available even after the program is closed.

---

# Features

✅ Add new tasks

✅ Remove existing tasks

✅ Mark tasks as completed

✅ Remove completed status

✅ View completed and incomplete tasks

✅ Save tasks to a file

✅ Load tasks from a file automatically

---

# Project Structure

```
project/
│
├── todo.py
├── saved.txt
└── README.md
```

### Files

| File        | Description              |
| ----------- | ------------------------ |
| `todo.py`   | Main application         |
| `saved.txt` | Stores tasks permanently |
| `README.md` | Project documentation    |

---

# How It Works

The application maintains two lists:

```python
main_list = []
completed_list = []
```

### Incomplete Tasks

Stored inside:

```python
main_list
```

Example:

```python
['Brush Teeth', 'Study Python']
```

### Completed Tasks

Stored inside:

```python
completed_list
```

Example:

```python
['Buy Milk']
```

---

# Task Status Format

When saved to the file:

### Incomplete Task

```text
Study Python []
```

### Completed Task

```text
Buy Milk [DONE]
```

This makes it easy for the program to identify task status when loading data.

---

# Menu Options

When the program starts:

```text
1.task add
2.task remove
3.Mark as completed
4.Remove Completed Mark
5.Check Completed & In Completed Task
```

---

## 1. Add Task

Adds a new task to the incomplete task list.

Example:

```text
Task Name
Study Python
```

Result:

```python
main_list = ['Study Python']
```

---

## 2. Remove Task

Removes a task from the incomplete list.

Example:

```text
Task Name
Study Python
```

Before:

```python
main_list = ['Study Python']
```

After:

```python
main_list = []
```

---

## 3. Mark as Completed

Moves a task from incomplete tasks to completed tasks.

Before:

```python
main_list = ['Study Python']
completed_list = []
```

After:

```python
main_list = []
completed_list = ['Study Python']
```

---

## 4. Remove Completed Mark

Moves a task back to the incomplete list.

Before:

```python
main_list = []
completed_list = ['Study Python']
```

After:

```python
main_list = ['Study Python']
completed_list = []
```

---

## 5. View Tasks

Displays all tasks.

Example Output:

```text
Completed List = ['Buy Milk']

In Completed List = ['Study Python', 'Exercise']
```

---

# Functions

## save_file()

Saves all tasks to `saved.txt`.

```python
def save_file():
```

### Responsibilities

* Save completed tasks with `[DONE]`
* Save incomplete tasks with `[]`

---

## load_list()

Loads tasks from `saved.txt`.

```python
def load_list():
```

### Responsibilities

* Read file data
* Detect task status
* Populate lists

---

## update_list()

Handles save operation or printing lists.

```python
def update_list():
```

### Responsibilities

* Save data
* Display current tasks

---

# Example saved.txt

```text
Buy Milk [DONE]
Study Python []
Exercise []
```

---

# Example Usage

### Add Task

```text
1.task add
2.task remove
3.Mark as completed
4.Remove Completed Mark
5.Check Completed & In Completed Task

What do you want
1

Task Name
Study Python

1.Save
2.Print only
1
```

---

### Mark Completed

```text
What do you want
3

Task Name
Study Python

1.Save
2.Print only
1
```

---

### View Tasks

```text
What do you want
5
```

Output:

```text
Completed List = ['Study Python']

In Completed List = []
```

---

# Concepts Practiced

This project helps beginners practice:

### Python Lists

```python
append()
remove()
```

### Functions

```python
save_file()
load_list()
update_list()
```

### File Handling

```python
open()
read()
write()
```

### Conditional Statements

```python
if
elif
else
```

### User Input

```python
input()
```

---

# Possible Improvements

Future enhancements:

* Prevent duplicate tasks
* Case-insensitive search
* Task priorities
* Due dates
* Task categories
* Better user interface
* Exception handling for missing files
* Use JSON instead of text files
* Object-Oriented Programming (OOP) version

---

# Known Issue

If `saved.txt` does not exist, the program may raise:

```python
FileNotFoundError
```

Possible fix:

```python
try:
    load_list()
except FileNotFoundError:
    pass
```

---

# Requirements

* Python 3.x

Check version:

```bash
python --version
```

---

# Run The Program

```bash
python todo.py
```

---

# License

This project is open source and available for learning, modification, and personal use.

---

# Author

Created as a Python practice project to learn:

* Lists
* File Handling
* Functions
* Data Persistence
* CLI Application Development
