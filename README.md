# FlaskToDo

## Overview

This project is a simple To-Do List application built with Flask and SQLite. It allows users to add, view, and delete tasks.

## Getting Started

Follow these steps to set up and run the project on your local machine.

## Prerequisites

Make sure you have the following installed:

- Python 3.6 or higher

- pip (Python package installer)

1. Cloning the Repository

Open your terminal (or Git Bash).

Navigate to the directory where you want to clone the repository.

Run the following command:

 ```bash
git clone https://github.com/oWarren320/FlaskToDo.git
```

2. Navigate into the project directory:

 ```bash
cd FlaskToDo
```

## Setting Up the Environment

3. Create a virtual environment (recommended):

 ```bash
python -m venv venv
```
4. Activate the virtual environment:

On Windows:

 ```bash
venv\Scripts\activate
```
On macOS/Linux:
 ```bash
source venv/bin/activate
```


5. Running the Application

Initialize the database (if not already done):

 ```bash
flask db upgrade
```
Run the Flask application:

 ```bash
flask run
```
Open your web browser and navigate to http://127.0.0.1:5000 to view the application.

## Usage
1. Add a Task: Enter your task text and click "Add".
2. View Tasks: Tasks will be displayed in the list.
3. Delete a Task: Click the "Delete" button next to the task you want to remove.
