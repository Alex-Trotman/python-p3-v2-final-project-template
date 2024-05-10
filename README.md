# Phase 3 Project: Task Manager

A command-line application to manage tasks and projects efficiently using Python and the `rich` library for CLI visuals.

## Features

- Create, edit, and delete projects
- Create, edit, and delete tasks within projects
- List and view tasks or projects in rich-format tables
- Prioritize tasks and mark them as completed

## Getting Started

### Prerequisites

- Python 3.8 or newer
- `pipenv` for managing dependencies

### Installation

1. **Fork & Clone the Repository:**
   - Click "Fork" on GitHub to fork the repository to your account.
   - Clone it to your local machine:
   ```bash
   git clone https://github.com/Alex-Trotman/phase-3-project-task-manager.git
   ```
2. **Install Dependencies:**
   - Install all the required packages using 'pipenv'.
   ```bash
   pipenv install
   ```
3. **Activate the Virtual Environment:**
   - Enter the virtual environment to start working on the project.
   ```bash
   pipenv shell
   ```
4. **Run the Application:**
   ```bash
   python lib/cli.py
   ```

## Usage

### Basic Commands

- List Projects: Type 1 to list all projects.
- Open a Project: Type 2 to open and manage tasks within a project.
- Manage Projects: Type 3 to create, edit, or delete projects.
- Exit: Type exit or 0 to close the application.

### Managing Projects

- Create a Project: Select the "Create Project" option to add a new project.
- Edit or Delete: Choose "Edit Project" or "Delete Project" to modify or remove an existing project.

### Managing Tasks

- Create a Task: In the project's task menu, select "Create Task" to add a new task.
- Edit or Delete: Choose "Edit Task" or "Delete Task" to modify or remove an existing task.
- Complete a Task: Mark a task as completed or uncompleted.
