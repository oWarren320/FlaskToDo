# FlaskToDo

Overview
This project is a simple To-Do List application built with Flask and SQLite. It allows users to add, view, and delete tasks.

Getting Started
Follow these steps to set up and run the project on your local machine.

Prerequisites
Make sure you have the following installed:

Python 3.6 or higher
pip (Python package installer)
Cloning the Repository
Open your terminal (or Git Bash).

Navigate to the directory where you want to clone the repository.

Run the following command:

bash
Copy code
git clone https://github.com/oWarren320/FlaskToDo.git
Navigate into the project directory:

bash
Copy code
cd your-repository-name
Setting Up the Environment
Create a virtual environment (recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source venv/bin/activate
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Running the Application
Initialize the database (if not already done):

bash
Copy code
flask db upgrade
Run the Flask application:

bash
Copy code
flask run
Open your web browser and navigate to http://127.0.0.1:5000 to view the application.

Usage
Add a Task: Enter your task text and click "Add".
View Tasks: Tasks will be displayed in the list.
Delete a Task: Click the "Delete" button next to the task you want to remove.
